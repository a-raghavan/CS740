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

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)

def main():
    staging_directory = sys.argv[1]

    #access_token = 'sl.BUMEirroBypSv1afRshqA7Y8BkeE3Eh_q1RvYwqDIWdDk8MCpo-No98PG-Izpu0d2D204yM7WUfJ60ZizbyQLs6LcrK1HiAwdtePMApCfnsARgz8OhCVRM_2usu3-trmUv2A-eo'
    access_token = 'sl.BUhDbJSi60zpxyRq9V_Hr0bY1DcCB0FGrP1WvKL71BIEEI4U-ayVdf6qMZ3hByvE4C-PPL3_bjc6IFTnYsqLrPbB25ZB8HFYkapJYCkR7-z7mI1HTzraOrNA11pcGVMfbaGjEak'
    transferData = TransferData(access_token)

    for filename in os.listdir(staging_directory):
        file_from = os.path.join(staging_directory, filename)
        file_to = '/test_dropbox/new_test/' + filename  # The full path to upload the file to, including the file name
        transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    num_args = len(sys.argv)
    if (num_args != 4):
        print("Error: Incorrect arguments. Usage: python dropbox_upload.py [staging directory] [iterations] [prefix]")
        exit()
    iterations = int(sys.argv[2])
    prefix = sys.argv[3]
    #iterations = 3 # for debug purpose only
    for i in range(iterations):
        save_file = prefix + "_" + str(i) + ".pcapng"
        p = subprocess.Popen([r"C:\Program Files\Wireshark\tshark.exe", "-i", "Wi-Fi", "-w", save_file], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP) 
        sleep(5)
        main()
        sleep(5)
        p.send_signal(signal.CTRL_C_EVENT)
        p.terminate()