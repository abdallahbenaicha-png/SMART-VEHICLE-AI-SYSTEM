import serial

gps = serial.Serial("/dev/ttyAMA0", 9600)

def read_gps():
    while True:
        line = gps.readline()
        print("📍", line.decode(errors="ignore"))
