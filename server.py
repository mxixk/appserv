import socket

server_sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

server_sck.bind('127.0.0.1',54444)
server_sck.listen(10)








