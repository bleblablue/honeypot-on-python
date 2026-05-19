import socket
from datetime import datetime
import threading
#1. ham xu ly thread
def handle_client(client_socket,address):
    try:
        #.data to client
        client_socket.send("login\nusername".encode("utf-8"))
            #nhan username
        username=client_socket.recv(1024).decode().strip()
            #gui password prompt
        client_socket.send("password: ".encode())
            #nhan pw
        password=client_socket.recv(1024).decode().strip()
        #print log
        print(f"USERNAME: {username}")
        print(f"PASSWORD: {password}")
            #them thoi gian vao log
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attacker.log","a") as f:
            f.write(f"IP: {address}\n")
            f.write(f"USERNAME: {username}\n")
            f.write(f"PASSWORD: {password}\n")
            f.write(f"TIME: {time}\n")
            f.write("--------------------------------------\n")
    except Exception as e:
        print(e)
    finally:
        client_socket.close()
    return ;


#2. socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#3. lang nghe tai ip va port
server_socket.bind(("0.0.0.0",3333))
server_socket.listen(5)
print("dang cho ket noi...")
while True:
    client_socket,address=server_socket.accept()
    print(f"ket noi tu: {address}")
#4. tao thread va chay
    thread=threading.Thread(
        target=handle_client,
        args=(client_socket,address)
    )
    thread.daemon=True #neu main process chet thread chet theo
    thread.start()
    
    
    
