import socket
from datetime import datetime
import threading
import random
import time
attempts={}
login=["Permission denied","Authentication failed","Login incorrect","Welcome Ubuntu"]
#them blacklist ip de ngan chan brute force cua hydra
black_list_ip=set()
#1. ham xu ly thread
def handle_client(client_socket,address):
    #detect brute force 
    ip=address[0]
    if ip in black_list_ip:
        client_socket.send("YOU ARE BANNED!\n".encode())
        client_socket.close()
        return
    if ip not in attempts:
        attempts[ip]=1
    else:
        attempts[ip]+=1
    print(f"{ip} attempted {attempts[ip]} times")
    #block neu qua nhieu lan
        #canh bao
    if 10<attempts[ip]<=50:
        print(f"[ALERT] BRUTE FORCE FROM {ip}")
    elif attempts[ip]>50:
        print(f"BAN ip {ip}, it has been blacklisted!")
        black_list_ip.add(ip) #them ip vao black list
        client_socket.send("Too many requests\nYOU ARE BLOCKED".encode())
        client_socket.close()
        return 
    try:
        #fake ssh banner
        client_socket.send("SSH-2.0-OpenSSH_8.2p1 Ubuntu\r\nlogin\nusername: ".encode())
                #\r\n end of line chuan
        #.data to client
            #nhan username
        username=client_socket.recv(1024).decode().strip()
            #gui password prompt
        client_socket.send("password: ".encode()) 
        time.sleep(0.2)
            #nhan pw
        password=client_socket.recv(1024).decode().strip()
            #random dang nhap thanh cong hoac that bai
        client_socket.send((random.choice(login)+"\n").encode())
        time.sleep(0.2)
        #print log
        print(f"USERNAME: {username}")
        print(f"PASSWORD: {password}")
            #them thoi gian vao log
        t=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attacker.log","a") as f:
            f.write(f"IP: {address}\n")
            f.write(f"USERNAME: {username}\n")
            f.write(f"PASSWORD: {password}\n")
            f.write(f"TIME: {t}\n")
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
    
    
    
