import serial

class ComChannel:

    def __init__(self, port, baudrate, reveivedTiemout_sec, maxReceiveBuffer):
        self.maxReceiveBuffer = maxReceiveBuffer
        self.ser = serial.Serial(port=port,baudrate=baudrate,timeout=reveivedTiemout_sec)

    def open(self):
        pass

    def portName(self):
        return self.ser.port

    def isOpen(self):
        return self.ser.is_open

    def set_timeout(self, timeout):
        # Establecer un tiempo de espera para operaciones de lectura o escritura
        pass

    def send(self, data):
        return self.ser.write(data)

    def receive(self):
        return self.ser.read(self.maxReceiveBuffer)
       
    def close(self):
        self.ser.close

