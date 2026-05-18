import socket
#1. socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2. lang nghe tai ip va port
server_socket.bind(("0.0.0.0",3333))
server_socket.listen(5)
print("dang cho ket noi...")
while True:
    client_socket,address=server_socket.accept()
    print(f"ket noi tu: {address}")
    #3.data to client
    client_socket.send("login\nusername".encode("utf-8"))
        #nhan username
    username=client_socket.recv(1024).decode()
        #gui password prompt
    client_socket.send("password: ".encode())
        #nhan pw
    password=client_socket.recv(1024).decode()
    #print log
    print(username)
    print(password)
    client_socket.close()
