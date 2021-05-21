import _pickle as pickle  # for faster serialization
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.11"  # To be changed to your local IP address
        self.port = 8999
        self.addr = (self.host, self.port)

    def connect(self):
        self.client.connect(self.addr)
        data = self.client.recv(2048 * 4)
        return pickle.loads(data)

    def disconnect(self):
        self.client.close()

    def send(self, data):

        try:
            self.client.send(pickle.dumps(data))
            return True
        
        except socket.error as e:
            print(e)
            return False

    def recive(self):
        reply = self.client.recv(2048 * 4)

        try:
            reply = pickle.loads(reply)
        except Exception as e:
            print(e)

        return reply
