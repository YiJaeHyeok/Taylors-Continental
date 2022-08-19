from multiprocessing import Process
import receiveArduinoSerial
import automation_Program
    
com = 'COM4'   
port = 9600  
timeout = 1
 

def startSystem():
  if __name__ == '__main__':
    p1 = Process(target=automation_Program.runProgram) 
    p1.start()
    p2 = Process(target=receiveArduinoSerial.arduinoCapture, args=(com,port,timeout))
    p2.start()  
    p1.join()           
    p2.join()  

startSystem() 
   

