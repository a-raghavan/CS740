"""
Clear the staging directory on the local computer.
Make room to download files from remote storage - Dropbox or Storj (or anything really).
credit to: https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
"""

import os, shutil
folder = '/home/dsmith7789/University_of_Wisconsin/staging_directory/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))