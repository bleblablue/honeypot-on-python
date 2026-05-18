import socket
# 1. khai bao host va port cua server
host="127.0.0.1" #ip cua server
port=2222 # port cua server
#2. open socket (ipv4,tcp)
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#3. connect to server
client_socket.connect((host, port));
#4. send data
mess="siuuuuu"
client_socket.sendall(mess.encode("utf-8"))
#5.nhan du lieu tu server
data=client_socket.recv(200)
print("nhan tu server: ", data.decode("utf-8"))
#6.close
client_socket.close()   