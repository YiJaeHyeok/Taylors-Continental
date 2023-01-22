import serial
import time

def arduinoCapture():
    ser = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)
    
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode strin
        return string

    ser.close()

#print(arduinoCapture())