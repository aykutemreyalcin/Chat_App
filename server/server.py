from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNETIONS = 10
BUFSIZ = 512

persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast(msg, name):
#send new messages to all clients
    for person in persons:
        client = person.client
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)

def client_communication(person):
#Thread to handle all messages from client
    client = person.client
    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)

    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "")

    while True:
        msg = client.recv(BUFSIZ)

        if msg == bytes("{quit}", "utf8"):
            client.close()
            persons.remove(person)
            broadcast(bytes(f"{name} has left the chat...", "utf8"), "")
            print(f"[DISCONNECTED] {name} disconnected")
            break
        else:
            broadcast(msg, name+": ")
            print(f"{name}: ", msg.decode("utf8"))

def wait_for_connection():
#Wait for connecton from new clients, start new thread once connected
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)

            print(f"[CONNECTION] {addr} connected to the server at {time.ctime()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break

    print("SERVER CRASHED")

if __name__ == "__main__":
    SERVER.listen(MAX_CONNETIONS)
    print("[STARTED] Waiting for connections...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()