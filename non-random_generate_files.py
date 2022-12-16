import random
from datetime import datetime

staging_directory = "/home/dsmith7789/University_of_Wisconsin/staging_directory/"

def gen_files(file_bytes, num_files, words):
    if file_bytes == (2048*100):
        size = "200KB"
    elif file_bytes == (2*1024*1024):
        size = "2MB"
    elif file_bytes == (100*1024*1024):
        size = "100MB"
    elif file_bytes == (500*1024*1024):
        size = "500MB"
    elif file_bytes == (2*1024*1024*1024):
        size = "2GB"
    else:
        size = "unspecified"

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M")

    for i in range(num_files):
        temp = ""
        string_size = 0
        while (string_size < file_bytes):
            selected = random.choice(words)
            temp += selected + " "
            string_size += len(selected) + 1
            print(string_size, file_bytes)
        
        # write from in memory object to file
        final_filename = staging_directory + size + "_" + str(i) + "_" + timestamp  # example: filename = 200KB_1
        with open(final_filename,'w') as final_file:
            final_file.write(temp)


def main():
    with open('/home/dsmith7789/University_of_Wisconsin/English_words.txt','r') as source_file:
        words = source_file.read().splitlines()
            
        # 100 x 200 KB - PDFs
        #gen_files(2048*100, 100, words)

        # 100 x 2 MB - photos taken on phone
        #gen_files((2*1024*1024), 100, words)

        # 1 x 500 MB - for comparison of random vs words
        gen_files((500*1024*1024), 1, words)
        
        # 1 x 2 GB - HD movies
        gen_files((2*1024*1024*1024), 1, words)

if __name__ == "__main__":
    main() 