#client for echo server using TCP in python
import socket
import sys

IP = socket.gethostbyname("192.168.56.1" )        #socket.gethostname())
PORT = 54321

#creat socket

try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP,PORT))
    
    print(f"client is connecting")
except Exception as e:
    print("error in socket creation",e)
    sys.exit()



#client operations

while True:
    try:
      input_massage = input("enter here: ")
      sock.send(input_massage.encode("utf-8"))
      recv_msg = sock.recv(1024)
      if not recv_msg:
          print("no massage reeived")
          break
      print("echo>>",recv_msg.decode("utf-8"))
    except Exception as e:
       print("error in handling clint",e)
       break
    except KeyboardInterrupt:
        print("closing server")
        break
sock.close()
sys.exit()  







