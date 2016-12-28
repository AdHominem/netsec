import socket

HOST = 'localhost'
PORT = 1337

# Create TCP socket and connect to the given host
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Prompt for message and send it
message = raw_input()
sock.send(message)

# Receive the reply
data = sock.recv(1024)
sock.close()
print 'Recieved: ', repr(data)