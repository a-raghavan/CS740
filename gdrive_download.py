from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import subprocess
from time import sleep
import signal
from datetime import datetime, timezone
from pathlib import Path
import io

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        results = service.files().list(
            q="'19inVWXczgkmKNYnPOQ9WhtsEf2kRbfF3' in parents", pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            return
        i = 0
        for item in items:
            p = subprocess.Popen(["/Applications/Wireshark.app/Contents/MacOS/tshark", "-i", "en0", "-w", "200KB_single_file_download_" +str(i)+".pcapng"])
            sleep(5)
            print('start time #' + str(i) + str(datetime.now(timezone.utc)))

            file_id = item['id']
            request = service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download {int(status.progress() * 100)}.')
            
            with open(item['name'], "wb") as f:
                f.write(file.getbuffer())

            print('end time #' + str(i) + str(datetime.now(timezone.utc)))
            sleep(5)
            p.send_signal(signal.SIGINT)
            p.terminate()
            i += 1

    except HttpError as error:
        file = None
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
    
