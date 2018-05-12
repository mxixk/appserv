import socket


cl_sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl_sck.connect(('127.0.0.1',54444))
cl_sck.sendall(b'BAAAAB')
data = cl_sck.recv(1024)
cl_sck.close()
print('Received',repr(data))
