import os
import subprocess

# set up variables:
bucket_name = "cs740/"
list_command = "~/uplink ls sj://" + bucket_name
download_command = "~/uplink cp sj://" + bucket_name
target_directory = "~/University_of_Wisconsin/staging_directory/"

# get list of files in the bucket

completed_process = subprocess.run(list_command, shell=True, text=True, capture_output=True)
output = completed_process.stdout
line_num = -1
file_list = list()
for line in output.splitlines():
    line_num += 1
    if line_num == 0:
        continue
    components = line.split()
    key = components[4] # holds the "KEY" which is the file name
    file_list.append(key)

# open wireshark

# for each file, download
for file in file_list:
    full_download_command = download_command + file + " " + target_directory + file
    os.system(full_download_command)
    