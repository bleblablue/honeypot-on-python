import socket
#1. socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2. lang nghe tai ip va port
server_socket.bind(("0.0.0.0",2222))
server_socket.listen(5)
print("dang cho ket noi...")
while True:
    client_socket,address=server_socket.accept()
    print("ket noi tu: {address}")
    #3.data to client
    client_socket.send("connect successfull".encode("utf-8"))
    client_socket.close
