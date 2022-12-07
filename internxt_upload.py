from time import sleep
import signal
import subprocess
from shutil import copy

if __name__ == '__main__':
    # for e in expts:
    p = subprocess.Popen(["/Applications/Wireshark.app/Contents/MacOS/tshark", "-i", "en0", "-w", "test.pcapng"])
    sleep(5)
    # for n in num_uploads:
    copy("../dataset/Expt1/200KB_expt/200KB_expt_0/200KB_1", "/Users/akshay/Internxt/Family/200KB_1")
    sleep(5)
    p.send_signal(signal.SIGINT)
    p.terminate()
