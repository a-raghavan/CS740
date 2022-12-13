"""
Clear the dropbox directory on the local computer.
Make room to upload files from local storage.
credit to: https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
"""

# delete entire folder using dropbox.dropbox.files_delete(path, parent_rev=None)

# recreate folder using dropbox.dropbox.files_create_folder(path, autorename=False)

import dropbox
import sys
import os

def main():
    access_token = 'sl.BU3HIIsoipTNOg6Ikiq6MyX7m0p1AhI9o05C9TgqgXk0SP52tzz2k1gSm1Tkf9RNDQ2Ag7y6LTR4QLN-xJMin-KWxqKpGcVEzaQmCul1nTYiLdEN1sCCGCIkI9_mZEXcLSY0qFY'
    path = '/test_dropbox/new_test' # ENTER PATH HERE, starting after home /Dropbox/ directory
    dbx = dropbox.Dropbox(access_token)
    dbx.files_delete(path)
    dbx.files_create_folder(path)

if __name__ == '__main__':
    main()