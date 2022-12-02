# credit https://stackoverflow.com/questions/23894221/upload-file-to-my-dropbox-from-python-script

''' Arguments:
1. staging directory - a folder on your local computer that has all the files you want
to upload
2. iterations - how many times you want to upload the files 
    TODO implement iterations
'''
import dropbox
import sys
import os

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
    num_args = len(sys.argv)
    print(num_args)
    if (num_args != 3):
        print("Error: Incorrect arguments. Usage: python dropbox_upload.py [staging directory] [iterations]")
        exit()
    staging_directory = sys.argv[1]
    iterations = sys.argv[2]

    access_token = 'sl.BUMEirroBypSv1afRshqA7Y8BkeE3Eh_q1RvYwqDIWdDk8MCpo-No98PG-Izpu0d2D204yM7WUfJ60ZizbyQLs6LcrK1HiAwdtePMApCfnsARgz8OhCVRM_2usu3-trmUv2A-eo'
    transferData = TransferData(access_token)

    for filename in os.listdir(staging_directory):
        file_from = os.path.join(staging_directory, filename)
        file_to = '/test_dropbox/new_test/' + filename  # The full path to upload the file to, including the file name
        transferData.upload_file(file_from, file_to)

    #file_from = r'C:\temp\200KB_1'
    #file_to = '/test_dropbox/new_test'  # The full path to upload the file to, including the file name

    # API v2
    #transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()