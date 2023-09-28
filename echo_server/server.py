
import socket 
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 55520

#creat socket

try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    sock.listen()
    print(f"server is up and running at {IP}:{PORT}")
except Exception as e:
    print("error in socket creation",e)
    sys.exit()



#handle the clint

while True:
    try:
        clint,addr = sock.accept()
        print("clint connected from : ",addr[0],":",addr[1])
        while True:
            try:
                msg = clint.recv(1024)
                if not msg:
                    print("no data recived")
                    break
                print(addr[0],":",addr[1],">>",msg.decode("utf-8"))
                client.send(msg)
            except Exception as e:
                print("error in send/receive",e)
                break
    except Exception as e:
       print("error in handling clint",e)
       break
    except KeyboardInterrupt:
        print("closing server")
        break
sock.close()
sys.exit()  







