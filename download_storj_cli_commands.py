import os
import sys
import subprocess
from time import sleep
import signal
from datetime import datetime

# set up variables:
bucket_name = "cs740/"
list_command = "~/uplink ls sj://" + bucket_name
download_command = "~/uplink cp sj://" + bucket_name
staging_directory = "~/University_of_Wisconsin/staging_directory/"
capture_directory = "/home/dsmith7789/University_of_Wisconsin/capture_directory/"

# get list of files in the bucket
def get_file_list():
    completed_process = subprocess.run(list_command, shell=True, text=True, capture_output=True)
    output = completed_process.stdout
    line_num = -1
    file_list = list()
    print("\nAcquiring file list...")
    for line in output.splitlines():
        line_num += 1
        if line_num == 0:
            continue
        components = line.split()
        key = components[4] # holds the "KEY" which is the file name
        file_list.append(key)
    print("\nFile list acquired!")
    return file_list

def download_files(file_list):
    # for each file, download
    for file in file_list:
        print("Downloading " + file + " ...")
        full_download_command = download_command + file + " " + staging_directory + file
        os.system(full_download_command)
        print("Download complete!")
    
if __name__ == '__main__':  
    file_size = sys.argv[1] 
    file_list = get_file_list()
    now = datetime.now() # current date and time
    timestamp = now.strftime("%m-%d-%Y_%H%M%S")
    save_file = capture_directory + "Storj_Download_" + file_size + "_" + timestamp + ".pcapng"
    print("Opening Wireshark...")
    p = subprocess.Popen([r"/mnt/c/Program Files/Wireshark/tshark.exe", "-i", "Wi-Fi", "-w", save_file]) 
    sleep(5)
    print('Download start time (record in spreadsheet):' + str(datetime.now(timezone.utc)))
    download_files(file_list)
    print('Download end time (record in spreadsheet):' + str(datetime.now(timezone.utc)))
    sleep(5)
    print("Closing Wireshark.")
    p.send_signal(signal.SIGINT)
    p.wait()
