import datetime
import logging
import subprocess


def check_devices(host, port):
    cmd = ["adb", "devices", "-l"]
    out = subprocess.check_output(cmd)
    logging.debug(out)

def connect(host,port):
    cmd = ["adb", "connect", "%s:%s" % (host,port) ]
    out = subprocess.check_output(cmd)
    logging.debug(out)

def screencap(filename = "screencap.png"):
    cmd = "scripts/adb_screencaps.sh screencaps/%s" % filename
    logging.debug(cmd)
    subprocess.check_output(cmd, shell=True)

def click(pt):
    cmd = ["adb", "shell", "input", "tap", pt[0], pt[1]]
    subprocess.check_output(cmd)


def swipe(start, end, time=1500):
    cmd = ["adb", "shell", "input", "swipe", str(start[0]), str(start[1]),
           str(end[0]), str(end[1]), str(time)]
    logging.debug(cmd)
    out = subprocess.check_output(cmd)
    logging.debug(out)

if __name__=='__main__':
    host = "192.168.0.10"
    port = 5555
    FORMAT = "%(asctime)-15s [%(levelname)-6s] %(filename)s:%(lineno)3d  %(message)s"
    logging.basicConfig(format=FORMAT, level=10)

    logging.info("connecting to a android emulator")
    connect(host, port)

    logging.info("listing devices")
    check_devices(host, port)

    logging.info("taking screencap")
    now = datetime.datetime.now()
    screencap(now.strftime("%y%m%d_%H%M%S")+".png")