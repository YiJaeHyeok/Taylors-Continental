import serial
import time
import keyboard


def arduinoCapture(com,port,timeout):
    ser = serial.Serial(com, port, timeout=timeout)
    time.sleep(2) 

    while True:
        line = ser.readline()   # read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode strin
            if string == '1':
                time.sleep(3) 
                keyboard.send("space")
                
                #keyboard.press("space" )
                #keyboard.release("space")
        #ser.close()

#arduinoCapture('COM1',9600,1)