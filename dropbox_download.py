# delete entire folder using dropbox.dropbox.files_delete(path, parent_rev=None)

# recreate folder using dropbox.dropbox.files_create_folder(path, autorename=False)

import dropbox
import sys
import os
import subprocess
from time import sleep
import signal
from datetime import datetime

access_token = 'sl.BU1vnhaxO0LxHXixZfuIA-1rTxiG7Puw3t3_r4-sjyThemws9wfQCa2xh1OS7KLbEPsWjmsIIq-ciQw7bRk1gAe55pCr8vJI-XMwdi7aVCI_A4FjXCbJkp3zalmfKlOH8XA5aPA'
main_path = '/test_dropbox/new_test' # ENTER PATH HERE, starting after home /Dropbox/ directory
staging_directory = "/home/dsmith7789/University_of_Wisconsin/staging_directory/"

def init_connection():
    dbx = dropbox.Dropbox(access_token)
    return dbx

def get_path_list(dbx):
    # get list of files in the main path
    contents_metadata = dbx.files_list_folder(main_path)

    path_list = list()
    for i in range(len(contents_metadata.entries)):
        file_path = contents_metadata.entries[i].path_display
        path_list.append(file_path)
    return path_list

def download_files(dbx, path_list):
    # for each file in the path_list, download it using files_download_to_file(download_path=<local path>, path=<path from path_list>, rev=None)
    for file in path_list:
        file_name = file.split("/")[3]
        local_path = staging_directory + file_name
        dbx.files_download_to_file(download_path=local_path, path=file)

if __name__ == '__main__':
    dbx = init_connection()
    path_list = get_path_list(dbx)
    
    file_size = "200KB"
    now = datetime.now() # current date and time
    timestamp = now.strftime("%m-%d-%Y_%H%M%S")
    save_file = "Dropbox_Download_" + file_size + "_" + timestamp + ".pcapng"
    p = subprocess.Popen(["/mnt/c/Program Files/Wireshark/tshark.exe", "-i", "Wi-Fi", "-w", save_file]) 
    sleep(5)
    download_files(dbx, path_list)
    sleep(5)
    p.send_signal(signal.SIGINT)
    p.terminate()
    sleep(5)
    