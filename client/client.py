from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock

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
        self.lock = Lock()
    
    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()
                if not msg:
                    break
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
                print(f"[{self.client_socket.getsockname()}] {msg}")
            except Exception as e:
                print(f"[ERROR] {e}")
                self.client_socket.close()
                break

    
    def send_message(self, msg):
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            return False
        return True

    def get_messages(self):
        self.lock.acquire()
        messages_copy = self.messages[:]
        self.lock.release()
        return messages_copy


