from time import sleep
import signal
import subprocess


if __name__ == '__main__':
    # for e in expts:
    p = subprocess.Popen(["/Applications/Wireshark.app/Contents/MacOS/tshark", "-i", "en0", "-w", "test.pcapng"])
    sleep(5)
    def signal_handler(sig, frame):
        p.send_signal(signal.SIGINT)
        p.terminate()
    
    signal.signal(signal.SIGINT, signal_handler)
    # start time 
    pdash = subprocess.Popen(["/Applications/Internxt Drive.app/Contents/MacOS/Internxt Drive"])
    signal.pause()
    # wait for interrupt from user


    # for n in num_uploads:

    
