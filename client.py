from socket import *

server = 'localhost'
serverP = 179
client = socket(AF_INET, SOCK_STREAM)
client.connect((server, serverP))
messageS = "a"

year="0"

while messageS != "exit":
    messageS=input("Enter exit if want to quit else enter any key to continue: ")
    client.send( messageS.encode())
    if(messageS=="exit"):
        messageR = client.recv(1024)
        print(messageR.decode())
        continue;
    
    year = input("Enter the year: ")
    
    
    client.send(year.encode())
    messageR = client.recv(1024)
    print(messageR.decode())
print("bye!")
client.close()
