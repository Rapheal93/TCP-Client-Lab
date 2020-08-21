import socket

targetHost = "127.0.0.1"
targetPort = 9999


# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((targetHost, targetPort))


# send some data

data = "AABBBCCCC"

client.send(data.encode())

# receive some data

response = client.recv(4096)

client.close()

print("Received ", response.decode())
