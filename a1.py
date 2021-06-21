import os
import socket                   # Import socket module
import time
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.
a = 0
s.connect(("192.168.0.111", 80))
while True:
    
    with open('received_file', 'wb') as f:
        
        data = s.recv(int(1))
        
        if not data:
            break
        # write data to a file
        
        if(int.from_bytes(data, "big")-48 == 1 and a == 0):
            os.system("python c1")
            os.system("python capture/aws_send_image.py")
            os.system("python capture/face_r.py")
            time.sleep(1)
            g = open("result.txt", "r")
            if(g.read(5) == '1'):
                s.send("1".encode())
            print("done")
            a = 1
        if(int.from_bytes(data, "big")-48 == 0 and a == 1):
            a = 0
        f.write(data)
        

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
