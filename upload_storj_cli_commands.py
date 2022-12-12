import os

staging_directory = "/home/dsmith7789/University_of_Wisconsin/staging_directory/"
bucket_name = "cs740"
for filename in os.listdir(staging_directory):
        upload_file = os.path.join(staging_directory, filename)
        command = "../../../uplink cp " + upload_file + " sj://" + bucket_name
        os.system(command)