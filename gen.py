import random
import ctypes

def sizeToStr(size):
    if size == 200*1024:
        return "200KB"
    elif size == 100*1024*1024:
        return "100MB"
    elif size == 2*1024*1024:
        return "2MB"
    elif size == 2*1024*1024*1024:
        return "2GB"

def createFile(size, quantity):

    for file_idx in range(quantity):
        f = open(sizeToStr(size)+"_"+str(file_idx), "wb")
        
        for i in range(size):
            a = random.randint(0,255)
            mychar = ctypes.c_ubyte(a)
            f.write(bytes(mychar))
            
        f.close()

for i in range(1):
    # createFile(200*1024, 100)
    # createFile(100*1024*1024, 100)
    # createFile(2*1024*1024, 100)
    createFile(2*1024*1024*1024, 1)
    
    
