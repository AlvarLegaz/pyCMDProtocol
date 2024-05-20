import serial

class CommChannel:
    def __init__(self, port, baudrate, reveivedTiemout_sec):

        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.timeout = reveivedTiemout #in seconds

    def connect():
        self.ser.open()
        pass

    def set_timeout(self, timeout):
        # Establecer un tiempo de espera para operaciones de lectura o escritura
        pass

    def send(self, data):
        # Enviar datos a través del canal
        pass

    def receive(self, buffer_size):
        # Recibir datos del canal
        pass

    def open(self):
        # Abrir el canal (si es necesario)
        pass

    def close(self):
        # Cerrar el canal y liberar recursos
        pass

# Ejemplo de uso
if __name__ == "__main__":
    channel = CommChannel("COM4",9600,0.1)
    channel.connect()

