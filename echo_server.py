import socket

HOST = 'localhost'
PORT = 1337

# Create TCP socket and listen for connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

# Accept new connection
connection, address = sock.accept()
print 'Connected by', address

# Receive data and reply
while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.send(data)

connection.close()