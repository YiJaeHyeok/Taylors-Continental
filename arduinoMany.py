import serial
import time
import keyboard
'''
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

while True:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode strin
        if string == '1':
            time.sleep(3) 
            keyboard.send("space" )
    #  ser.close()
'''



def arduinoCapture():
    ser = serial.Serial('COM4', 9600, timeout=1)
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

#arduinoCapture()
