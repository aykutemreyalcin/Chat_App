from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class Client:

    HOST = "localhost"
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFSIZ = 512

    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
    
    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()
                self.messages.append(msg)
                print(msg)
            except Exception as e:
                print(f"{e}")
                self.client_socket.close()
                break
    
    def send_message(self, msg):
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            return False
        return True

    def get_messages(self):
        return self.messages

aykut = Client("aykut")
while True:
    msg = input()
    if not aykut.send_message(msg):
        break