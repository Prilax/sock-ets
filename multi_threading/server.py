import socket
import threading
import sys

IP = "192.168.56.1" #socket.gethostbyname(socket.gethostname())
PORT = 54321

def server_socker():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((IP,PORT))
        sock.listen()
        print(f"server is up and running at {IP}:{PORT}")
        return sock
    except Exception as e:
        print("error -server socket -",e)
        sys.exit()

def client_handle(client,addr):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                print("no message")
                break
            print(f"{addr[0]}:{addr[1]}>>{msg.decode('utf-8')}")
            client.send("message recived".encode("utf-8")) 
        except Exception as e:
            print(f"Error - connection client - ",e)
            break  
        except KeyboardInterrupt:
            print(f"{addr[0]}:{addr[1]} is closed")
            break     

def connect_client(sock):
    while True:
        try:
            client, addr = sock.accept()
            print(f"[+] {addr[0]}:{addr[1]} connected")
            client_thread = threading.Thread(target = client_handle,args=(client,addr))
            client_thread.start()
            print(f"[Active clients] = {threading.active_count()-1}")
        except Exception as e:
            print(f"Error - connection client - ",e)
            break
        except KeyboardInterrupt:
            break
    print("Closing server")
    sock.close()                
    sys.exit()  

if __name__ == "__main__":
    s=server_socker()
    connect_client(s)