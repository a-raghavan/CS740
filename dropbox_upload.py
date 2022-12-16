# credit https://stackoverflow.com/questions/23894221/upload-file-to-my-dropbox-from-python-script

''' Arguments:
1. staging directory - a folder on your local computer that has all the files you want
to upload
2. iterations - how many times you want to upload the files 
3. prefix - What the pcap file names should start with. They are automatically numbered by the iteration nummber.
'''
import dropbox
import sys
import os

import subprocess
from time import sleep
import signal
from datetime import datetime

access_token = sys.argv[2]
staging_directory = "/home/dsmith7789/University_of_Wisconsin/staging_directory/"
capture_directory = "/home/dsmith7789/University_of_Wisconsin/capture_directory/"

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            print("Uploading " + str(file_from) + " ...")
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
            print("Upload complete!")

def main():
    transferData = TransferData(access_token)

    for filename in os.listdir(staging_directory):
        file_from = os.path.join(staging_directory, filename)
        file_to = '/test_dropbox/new_test/' + filename  # The full path to upload the file to, including the file name
        transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    file_size = sys.argv[1]
    #file_size = "200KB"
    now = datetime.now() # current date and time
    timestamp = now.strftime("%m-%d-%Y_%H%M%S")
    save_file = capture_directory + "Dropbox_Upload_" + file_size + "_" + timestamp + ".pcapng"
    print("Opening Wireshark...")
    p = subprocess.Popen([r"/mnt/c/Program Files/Wireshark/tshark.exe", "-i", "Wi-Fi", "-w", save_file])
    sleep(5)
    main()
    sleep(5)
    print("Closing Wireshark.")
    p.send_signal(signal.SIGINT)
    p.wait()