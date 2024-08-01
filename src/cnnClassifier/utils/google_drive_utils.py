import io
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

class GoogleDriveService:
    def __init__(self, credentials_info):
        self.creds = service_account.Credentials.from_service_account_info(credentials_info)
        self.service = build('drive', 'v3', credentials=self.creds)
    
    def list_files(self, folder_id, mime_type='image/'):
        query = f"'{folder_id}' in parents and mimeType contains '{mime_type}'"
        return self._list_items(query)
    
    def list_subfolders(self, folder_id):
        query = f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'"
        return self._list_items(query)

    def _list_items(self, query):
        result = []
        page_token = None
        while True:
            try:
                response = self.service.files().list(
                    q=query,
                    fields="nextPageToken, files(id, name)",
                    pageToken=page_token
                ).execute()

                result.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break
            except HttpError as error:
                print(f'An error occurred: {error}')
                break
        return result

    def download_file(self, file_id, file_name, local_dir):
        subfolder_name = 'Normal' if 'normal' in file_name.lower() else 'Stone' if 'stone' in file_name.lower() else 'Tumor' if 'tumor' in file_name.lower() else 'Cyst' if 'cyst' in file_name.lower() else 'Other'
        subfolder_path = os.path.join(local_dir, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        request = self.service.files().get_media(fileId=file_id)
        file_path = os.path.join(subfolder_path, file_name)

        with io.FileIO(file_path, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download {file_name} {int(status.progress() * 100)}%.")
