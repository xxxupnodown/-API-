import serial
import serial.tools.list_ports

def start_port(ports, speed, timex):  
    ser = serial.Serial()
    ser.port = ports
    ser.baudrate = speed
    ser.timeout = timex
    ser.open()
    return ser
    
def open_serial():
    result = start_port("COM5", 9600, 1)
    #     return start_port(com, 9600, 1)
    # else:
    #     return False
    return result
    
def getData(obj):
    return obj.readline().decode()

def port_close(port):
    port.close()
    
    