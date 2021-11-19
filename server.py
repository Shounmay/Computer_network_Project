from socket import *
import mysql.connector


    
serverP = 179
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverP))
serverSocket.listen(1)
while True:
    connection, addr = serverSocket.accept()
    messageR = "a"
    country="india"
    year="0"
    value=0
    while messageR != "exit":
        messageR=connection.recv(1024).decode()
        if(messageR=="exit"):
            connection.send(("Thanks fopr visiting us!!!").encode())
            print(messageR)
            break
        
        year = connection.recv(1024).decode()
        
        mydb=mysql.connector.connect(host="localhost",database='project',user="root",                              passwd="1234",port="13306")

        mycursor=mydb.cursor()

       

        

        final="select * from carbon_data_one where year="+str(year)

        mycursor.execute(final)

        for i in mycursor:
                value=i[2]
                country=i[1]
        
        print(messageR)
        
        
        
        connection.send(("Country with highest carbon-emmission in the year " + str(year)+" is "+country+" with a value of: "+str(value)).encode())
       

connection.close()
    