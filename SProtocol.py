import ComChannel

HEAD_SIZE = 4

CLEAN = 0X00
CIPHER = 0X01
SIGNED = 0X02

class SProtocol:

    def __init__(self, channel, source):
        self.channelName = channel
        self.source = source

        if self.channelName == "COM":
            self.channelDefined = True
            baudrate = 19200
            port = 'COM4'
            timeout = 0.5 #in seconds
            maxReceiveBuffer = 32
            self.channel = ComChannel.ComChannel(port, baudrate, timeout, maxReceiveBuffer)
        else:
            raise TypeError("Channel not implemented")

    def getChannelName(self):
        return self.channelName

    def  open(self):
        return self.channel.open()
        
    def isOpen(self):
        return self.channel.isOpen()
        
    def send_clean(self, msg, destination):
        
        dataLen = len(msg)
        head = [destination, self.source, CLEAN, dataLen]
        frame = head + msg

        print("msg:", ','.join('{:02X}'.format(x) for x in msg))
        print("frame:", ','.join('{:02X}'.format(x) for x in frame))

        return self.channel.send(frame)

    def receive_clean(self):
        received  = self.channel.receive()  
        destination =  received[0]
        source = received[1]
        mode = received[2]
        dataLen = received[3]
        if (destination == self.source and mode == CLEAN):
            msg = received[4:]
            return msg
        else:
            raise TypeError("Wrong received frame")    

    def close(self):
        return self.channel.close()  
