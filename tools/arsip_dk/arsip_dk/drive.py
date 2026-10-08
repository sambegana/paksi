"""Akses Google Drive API v3 untuk Shared Drive.

Kredensial yang diterima (dicek berurutan):
  1. DK_SERVICE_ACCOUNT_JSON  — isi JSON service account (cocok untuk environment secret)
  2. GOOGLE_APPLICATION_CREDENTIALS — path ke file JSON service account
  3. OAuth desktop client: file credentials.json (atau path di DK_OAUTH_CLIENT);
     browser terbuka sekali untuk login, token disimpan di token_<mode>.json

API key biasa (berawalan "AIza...") TIDAK bisa membuka Shared Drive privat.
"""

import json
import os
import re
import threading

from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPE_BACA = ["https://www.googleapis.com/auth/drive.readonly"]
SCOPE_TULIS = ["https://www.googleapis.com/auth/drive"]

MIME_FOLDER = "application/vnd.google-apps.folder"

FIELD_FILE = (
    "id,name,mimeType,size,md5Checksum,createdTime,modifiedTime,parents,description,"
    "hasThumbnail,webViewLink,"
    "imageMediaMetadata(time,width,height,cameraMake,cameraModel,location),"
    "videoMediaMetadata(width,height,durationMillis)"
)

_kunci_token = threading.Lock()


class DriveError(RuntimeError):
    pass


def kredensial(tulis=False):
    scopes = SCOPE_TULIS if tulis else SCOPE_BACA
    isi_sa = os.environ.get("DK_SERVICE_ACCOUNT_JSON")
    file_sa = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if isi_sa:
        return service_account.Credentials.from_service_account_info(json.loads(isi_sa), scopes=scopes)
    if file_sa:
        return service_account.Credentials.from_service_account_file(file_sa, scopes=scopes)

    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    klien = os.environ.get("DK_OAUTH_CLIENT", "credentials.json")
    if not os.path.exists(klien):
        raise DriveError(
            "Kredensial Google tidak ditemukan. Set DK_SERVICE_ACCOUNT_JSON / "
            "GOOGLE_APPLICATION_CREDENTIALS untuk service account, atau taruh file OAuth "
            f"client desktop di {klien!r}. Lihat README.md bagian 'Kredensial Google'."
        )
    path_token = f"token_{'tulis' if tulis else 'baca'}.json"
    cred = None
    if os.path.exists(path_token):
        cred = Credentials.from_authorized_user_file(path_token, scopes)
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
    if not cred or not cred.valid:
        cred = InstalledAppFlow.from_client_secrets_file(klien, scopes).run_local_server(port=0)
    with open(path_token, "w") as f:
        f.write(cred.to_json())
    return cred


def layanan(cred):
    return build("drive", "v3", credentials=cred, cache_discovery=False)


def token_segar(cred):
    """Token akses yang masih berlaku (dipakai ffmpeg yang tidak paham OAuth)."""
    with _kunci_token:
        if not cred.valid:
            cred.refresh(Request())
        return cred.token


def sesi_http(cred):
    return AuthorizedSession(cred)


def cari_shared_drive(svc, nama):
    aman = nama.replace("\\", "\\\\").replace("'", "\\'")
    hasil, token = [], None
    while True:
        r = svc.drives().list(q=f"name = '{aman}'", pageSize=100, pageToken=token,
                              fields="nextPageToken,drives(id,name)").execute(num_retries=5)
        hasil += r.get("drives", [])
        token = r.get("nextPageToken")
        if not token:
            break
    if not hasil:
        raise DriveError(
            f"Shared Drive bernama {nama!r} tidak terlihat oleh akun ini. Jika memakai service "
            "account, tambahkan email service account sebagai anggota Shared Drive tersebut "
            "(Content manager untuk tahap terapkan, Viewer cukup untuk audit)."
        )
    if len(hasil) > 1:
        daftar = ", ".join(d["id"] for d in hasil)
        raise DriveError(f"Ada {len(hasil)} Shared Drive bernama {nama!r} ({daftar}); pakai --drive-id.")
    return hasil[0]["id"]


def daftar_semua(svc, drive_id):
    """Semua file & folder (tidak termasuk sampah) di satu Shared Drive."""
    hasil, token = [], None
    while True:
        r = svc.files().list(
            corpora="drive", driveId=drive_id, includeItemsFromAllDrives=True,
            supportsAllDrives=True, q="trashed = false", pageSize=1000, pageToken=token,
            fields=f"nextPageToken,files({FIELD_FILE})",
        ).execute(num_retries=5)
        hasil += r.get("files", [])
        token = r.get("nextPageToken")
        if not token:
            return hasil


def path_folder(item, folder_by_id, drive_id):
    """Rangkai path folder induk: 'Kegiatan 2023/Penanaman'."""
    bagian, induk, terlihat = [], (item.get("parents") or [None])[0], set()
    while induk and induk != drive_id and induk in folder_by_id and induk not in terlihat:
        terlihat.add(induk)
        f = folder_by_id[induk]
        bagian.append(f["name"])
        induk = (f.get("parents") or [None])[0]
    return "/".join(reversed(bagian))


def url_media(file_id):
    return f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&supportsAllDrives=true"


def link_thumbnail(svc, file_id, sisi=1600):
    """thumbnailLink kedaluwarsa dalam hitungan jam, jadi selalu diambil ulang."""
    r = svc.files().get(fileId=file_id, fields="thumbnailLink", supportsAllDrives=True).execute(num_retries=5)
    link = r.get("thumbnailLink")
    if not link:
        return None
    return re.sub(r"=s\d+$", f"=s{sisi}", link) if re.search(r"=s\d+$", link) else link
