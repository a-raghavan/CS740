import os
import sys
import subprocess
from time import sleep
import signal
from datetime import datetime

staging_directory = "/home/dsmith7789/University_of_Wisconsin/staging_directory/"
capture_directory = "/home/dsmith7789/University_of_Wisconsin/capture_directory/"
bucket_name = "cs740"

def upload_files():
    for filename in os.listdir(staging_directory):
        upload_file = os.path.join(staging_directory, filename)
        print("\nUploading " + str(filename) + " ...")
        command = "~/uplink cp " + upload_file + " sj://" + bucket_name
        os.system(command)
        print("\nUpload complete!")

if __name__ == '__main__':   
    file_size = sys.argv[1]
    now = datetime.now() # current date and time
    timestamp = now.strftime("%m-%d-%Y_%H%M%S")
    save_file = capture_directory + "Storj_Upload_" + file_size + "_" + timestamp + ".pcapng"
    print("Opening Wireshark...")
    p = subprocess.Popen([r"/mnt/c/Program Files/Wireshark/tshark.exe", "-i", "Wi-Fi", "-w", save_file]) 
    sleep(5)
    print('Upload start time (record in spreadsheet):' + str(datetime.now(timezone.utc)))
    upload_files()
    print('Upload end time (record in spreadsheet):' + str(datetime.now(timezone.utc)))
    sleep(5)
    print("Closing Wireshark.")
    p.send_signal(signal.SIGINT)
    p.wait()
