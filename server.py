import socket

server_sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
server_sck.bind(('127.0.0.1',54444))
server_sck.listen(10)
cl_sck, cl_adr = server_sck.accept()

#print(cl_sck, cl_adr)
while True:
    data = cl_sck.recv(1024)
    cl_sck.sendall(bytes('q for finish', encoding = 'utf-8'))
    print(data)
    if data == b'q\r\n':
        break
    if not data:
        break
    cl_sck.sendall(data)





