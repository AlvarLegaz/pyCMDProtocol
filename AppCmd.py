# Example script for Cmd protocol
# tags: CMD, protocol, Pyserial

import serial
import ComChannel

print("AppCMD for Python")

ser = serial.Serial()

baudrate = 19200
port = 'COM4'
timeout = 0.1 #in seconds

channel = ComChannel.ComChannel(port, baudrate, timeout)
channel.open()

print("Port Name:",channel.portName())         
print("IsOpen:",channel.isOpen())        

msg = [0x01, 0x23, 0x11, 0xaa, 0x00, 0x51]
print("send:", ','.join('{:02X}'.format(x) for x in msg))
channel.send(msg)

received = channel.receive()
print("received:", ','.join('{:02X}'.format(x) for x in received))

channel.close()
