# Example script for Cmd protocol
# tags: CMD, protocol, Pyserial

import serial

print("AppCMD for Python")

ser = serial.Serial()

ser.baudrate = 19200
ser.port = 'COM4'
ser.timeout = 0.1 #in seconds

ser.open()
print("Port Name:",ser.name)         
print("IsOpen:",ser.is_open)        

msg = [0x01, 0x23, 0x11, 0xaa]
print("send:", ','.join('{:02X}'.format(x) for x in msg))
ser.write(msg)

received = ser.readline()
print("received:", ','.join('{:02X}'.format(x) for x in received))

ser.close()


