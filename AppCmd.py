# Example script for Cmd protocol
# tags: CMD, protocol, Pyserial

import SProtocol

print("AppCMD for Python")

sourceAddress = (0x01)
destinationAddress = (0x01)

protocol = SProtocol.SProtocol("COM",sourceAddress)
protocol.open()

print("Channel Name:", protocol.getChannelName())         
print("IsOpen:",protocol.isOpen())        

msg = [0x01, 0x23, 0x11, 0x0a, 0x00, 0x51]
protocol.send_clean(msg, destinationAddress)

received = protocol.receive_clean()
print("received:", ','.join('{:02X}'.format(x) for x in received))

protocol.close()
