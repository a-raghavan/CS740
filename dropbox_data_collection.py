"""
Upload:
Prompt for iterations
Prompt for file_size as string
For each iteration:
    Upload
    Clear
    download
"""

import subprocess

### ACCESS TOKEN - may need updating ###
access_token = "sl.BVFSfrb155Z07R9nvDNxkVbuLuvamei8XcjILd2FNy26jRxrzpiEtVjFKV3ew0W7qd_zcy6T9qmdEG3rqRL6XVl6awcUJvc3vLT5z7_PrZ3UEVxmdDjZSyxx9ZvuhaQ9riDuYIU"

file_size = input("What size are the files in the staging directory?: ")
experiment_count = input("How many times do you want to run the experiment?: ")
iterations = int(experiment_count)
print("Running experiments for " + file_size + " files for a total of " + experiment_count + " experiments.")
for i in range(iterations):
    print("\n\n################ Starting experiment ", i, " ################")
    print("\n\nBegin Uploading Files...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/dropbox_upload.py", file_size, access_token])
    print("\n\nFinished Uploading Files.")
    print("\n\nClearing staging directory...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/clear_staging_directory.py"])
    print("\n\nStaging Directory Clear.")
    print("\n\nBegin Downloading Files...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/dropbox_download.py", file_size, access_token])
    print("\n\nFinished Uploading Files.")
    print("\n\nClearing Dropbox directory...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/clear_dropbox_directory.py", access_token])
    print("\n\nDropbox Directory Clear.")
print("\n\n################ ALL EXPERIMENTS COMPLETE!  ################")
