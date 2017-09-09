import subprocess
import logging

def check_devices(host, port):
    cmd = ["adb", "devices", "-l"]
    out = subprocess.check_output(cmd)

def connect(host,port):
    cmd = ["adb", "connect", "%s:%s" % (host,port) ]
    subprocess.check_output(cmd)

def screencap(filename = "screencap.png"):
    cmd = "adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > %s" % filename
    subprocess.check_output(cmd, shell=True)

def click(pt):
    cmd = ["adb", "shell", "tap", pt[0], pt[1]]
    subprocess.check_output(cmd)

def swipe(start, end):
    cmd = ["adb", "shell", start[0], start[1], end[0], end[1]]
    subprocess.check_output(cmd)

if __name__=='__main__':
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=20)


if __name__=='__main__':
    pass