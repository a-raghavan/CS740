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

file_size = input("What size are the files in the staging directory?: ")
experiment_count = input("How many times do you want to run the experiment?: ")
iterations = int(experiment_count)
print("Running experiments for " + file_size + " files for a total of " + experiment_count + " experiments.")
for i in range(iterations):
    print("\n\n################ Starting experiment ", i, " ################")
    print("\n\nBegin Uploading Files...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/upload_storj_cli_commands.py", file_size])
    print("\n\nFinished Uploading Files.")
    print("\n\nClearing staging directory...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/clear_staging_directory.py"])
    print("\n\nStaging Directory Clear.")
    print("\n\nBegin Downloading Files...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/download_storj_cli_commands.py", file_size])
    print("\n\nFinished Uploading Files.")
    print("\n\nClearing Storj directory...")
    subprocess.run(["python3", "/home/dsmith7789/University_of_Wisconsin/Github/CS740/clear_storj_directory.py"])
    print("\n\nStorj Directory Clear.")
print("\n\n################ ALL EXPERIMENTS COMPLETE!  ################")
