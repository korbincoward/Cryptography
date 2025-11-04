import socket
HOST = 'socket.cryptocat.uk'
PORT = 4453

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

buffer = 1024
received = s.recv(1024) 
print(received) 
sendmsg = b'{"option": "get_flag"}'
s.send(sendmsg)
received = s.recv(1024) 
print(received)
s.close()
