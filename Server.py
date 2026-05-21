import socket
from datetime import datetime
import threading
import random
attempts={}
login=["Permission denied","Authentication failed","Login incorrect","Welcome Ubuntu"]
#1. ham xu ly thread
def handle_client(client_socket,address):
    #detect brute force 
    ip=address[0]
    if ip not in attempts:
        attempts[ip]=1
    else:
        attempts[ip]+=1
    print(f"{ip} attempted {attempts[ip]} times")
    
    try:
        #fake ssh banner
        client_socket.send("SSH-2.0-OpenSSH_8.2p1 Ubuntu\r\n".encode()) 
                #\r\n end of line chuan
        #.data to client
        client_socket.send("login\nusername: ".encode("utf-8"))
            #nhan username
        username=client_socket.recv(1024).decode().strip()
            #gui password prompt
        client_socket.send("password: ".encode()) 
            #nhan pw
        password=client_socket.recv(1024).decode().strip()
            #random dang nhap thanh cong hoac that bai
        client_socket.send((random.choice(login)+"\n").encode())
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
    return 


#2. socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 #dung lai port cu neu tat server va bat lai 
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #level socket option, ten option, bat option
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
    
    
    
