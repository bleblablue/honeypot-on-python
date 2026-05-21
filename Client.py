import socket
# 1. khai bao host va port cua server
host="127.0.0.1" #ip cua server
port=3333 # port cua server
#2. open socket (ipv4,tcp)
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#3. connect to server
client_socket.connect((host, port));
#4. nhan tu server
    # banner
data = client_socket.recv(1024)
print(data.decode())
    # login prompt
data = client_socket.recv(1024)
print(data.decode())
#user nhap
username=input()
#5.gui len server
client_socket.send(username.strip().encode())
#6. pw tuong tu
data=client_socket.recv(1024)
print(data.decode())
password=input()
client_socket.send(password.strip().encode())
data=client_socket.recv(1024)
print(data.decode())
#7.close
client_socket.close()