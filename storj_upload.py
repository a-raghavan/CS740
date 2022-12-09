# credit: https://github.com/storj-thirdparty/uplink-python
# goobox??
# pylint: disable=too-many-arguments
""" example project for storj-python binding shows how to use binding for various tasks. """

''' Arguments:
1. staging directory - a folder on your local computer that has all the files you want
to upload
2. iterations - how many times you want to upload the files 
3. prefix - What the pcap file names should start with. They are automatically numbered by the iteration nummber.
'''

from datetime import datetime

from uplink_python.errors import StorjException, BucketNotEmptyError, BucketNotFoundError
from uplink_python.module_classes import ListObjectsOptions, Permission, SharePrefix
from uplink_python.uplink import Uplink

import sys
import os
import subprocess
from time import sleep
import signal

def transfer_data(file, iteration):
    # Storj configuration information
    MY_API_KEY = "1dfJFuTm5EL5YJUqBARc9z6TboNHsxTpmdxRAHyAguSuy6XuB1HEny1uih3gmGS1rwqi6KFfz8tVS4PuvhxZ2zEhSg9ZYYWmorYYY31aQ9NAJzokvM4n"
    MY_SATELLITE = "12EayRS2V1kEsWESU9QMRseFhdxYxKicsiFmxrsLZHeLUtdps3S@us1.storj.io:7777"
    MY_BUCKET = "cs740"
    MY_STORJ_UPLOAD_PATH = file + "_" + str(iteration) # the path on Storj: "(optional): path / (required): filename"
    MY_ENCRYPTION_PASSPHRASE = "Dante"
        # Source and destination path and file name for testing
    SRC_FULL_FILENAME = file


    # try-except block to catch any storj exception
    try:
        # create an object of Uplink class
        uplink = Uplink()

        # function calls
        # request access using passphrase
        print("\nRequesting Access using passphrase...")
        access = uplink.request_access_with_passphrase(MY_SATELLITE, MY_API_KEY,
                                                       MY_ENCRYPTION_PASSPHRASE)
        print("Request Access: SUCCESS!")
        #

        # open Storj project
        print("\nOpening the Storj project, corresponding to the parsed Access...")
        project = access.open_project()
        print("Desired Storj project: OPENED!")
        #

        # as an example of 'put' , lets read and upload a local file
        # upload file/object
        print("\nUploading data...")
        # get handle of file to be uploaded
        file_handle = open(SRC_FULL_FILENAME, 'r+b')
        # get upload handle to specified bucket and upload file path
        upload = project.upload_object(MY_BUCKET, MY_STORJ_UPLOAD_PATH)
        #
        # upload file on storj
        upload.write_file(file_handle)
        #
        # commit the upload
        upload.commit()
        # close file handle
        file_handle.close()
        print("Upload: COMPLETE!")
        #

        #
        # close given project using handle
        print("\nClosing Storj project...")
        project.close()
        print("Project CLOSED!")
        #

    except StorjException as exception:
        print("Exception Caught: ", exception.details)
    pass

def main():
    staging_directory = sys.argv[1]
    iteration = 0
    for filename in os.listdir(staging_directory):
        file = str(os.path.join(staging_directory, filename))
        transfer_data(file, iteration)
        iteration += 1
    

if __name__ == "__main__":
    num_args = len(sys.argv)
    if (num_args != 4):
        print("Error: Incorrect arguments. Usage: python storj_upload.py [staging directory] [iterations] [prefix]")
        exit()
    iterations = int(sys.argv[2])
    prefix = sys.argv[3]
    #iterations = 3 # for debug purpose only
    for i in range(iterations):
        save_file = prefix + "_" + str(i) + ".pcapng"
        p = subprocess.Popen([r"/mnt/c/Program Files/Wireshark/tshark.exe", "-i", "Wi-Fi", "-w", save_file]) 
        sleep(5)
        main()
        sleep(5)
        #p.send_signal(signal.CTRL_C_EVENT)
        p.send_signal(signal.SIGINT)
        p.terminate()

