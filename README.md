# Python Socket Chat Application

This is a simple multi-client chat application implemented in Python using sockets and threads. Clients can connect to the server, send messages to each other, and gracefully disconnect.

---

## Project Structure

```
├── client.py       # Client implementation
├── server.py       # Server implementation
├── person.py       # Represents connected clients
├── test.py         # Example usage with 3 simulated clients
```

---

## Getting Started

### Prerequisites

- Python 3.x

No external dependencies are required.

### Running the Server

```bash
python server.py
```

You should see:
```
[STARTED] Waiting for connections...
```

### Running Clients

Each client can be launched in a separate terminal or programmatically as in `test.py`:

```bash
python test.py
```

This will:
- Connect 3 clients
- Send some test messages
- Simulate proper quitting behavior

---

## Features

- Multi-client support with threading
- Name-based identification
- Message broadcasting
- Clean disconnection
- Thread-safe message storage on client side

---

## Code Overview

### `person.py`

Defines a `Person` class that holds:
- `addr`: IP address of the connected client
- `client`: The socket object
- `name`: Set after connection

### `server.py`

- Accepts new connections
- Starts a thread per client
- Receives messages and broadcasts to all clients
- Handles disconnection cleanly

### `client.py`

- Connects to server
- Sends initial name
- Receives and stores messages using thread and lock
- Sends messages including `{quit}` to exit

### `test.py`

- Simulates a chat session with 3 clients
- Sends a few messages
- Ends all sessions cleanly

---

## Notes

- Both server and clients use `localhost` and port `5500`. You can change these in the code.
- Messages are UTF-8 encoded.
- `{quit}` command is used to signal exit.

---
