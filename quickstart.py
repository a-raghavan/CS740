from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

import subprocess
from time import sleep
import signal
from datetime import datetime, timezone
from pathlib import Path

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
        

        # expts
        directory = Path("../dataset/Expt1/200KB_expt/200KB_expt_1/").glob('*')
        i = 0
        for file in directory:
            if i == 10:
                break
            p = subprocess.Popen(["/Applications/Wireshark.app/Contents/MacOS/tshark", "-i", "en0", "-w", "200KB_single_file_upload_" +str(i)+".pcapng"])
            sleep(5)
            
            # multiple files in an expt
            print('start time #' + str(i) + str(datetime.now(timezone.utc)))
            filename = str(file)
            file_metadata = {'name': os.path.basename(filename)}
            media = MediaFileUpload(filename, mimetype='application/octet-stream')
            file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
            
            print('end time #' + str(i) + str(datetime.now(timezone.utc)))
            print(F'File ID: {file.get("id")}')
            
            sleep(5)
            p.send_signal(signal.SIGINT)
            p.terminate()
            i += 1

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        file = None
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
    
