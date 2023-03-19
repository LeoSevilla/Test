#!/usr/bin/env python

import socket
import sys

channel = "#psicologia"
server = "irc.chateamos.org"       
botnick = "BotLeo_"


data= "USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n"
data2 = "NICK "+ botnick +"\n"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("connecting to:"+server)
irc.connect((server, 6667))
irc.send(data.encode())
irc.send(data2.encode())


while 1:
    text=irc.recv(2040).decode("ISO-8859-15")
    print (text)

    if text.find("PING") != -1:
        data3="PONG " + text.split() [1] + "\r\n"
        irc.send(data3.encode())

    if text.find('422') != -1:
        data4= "JOIN "+ channel +"\n"
        irc.send(data4.encode())

    if text.find(':!hi') !=-1:
        t = text.split(':!hi') #Si pones el comando !hi te responde con Hello
        to = t[1].strip()
        data='PRIVMSG '+channel+' :Hello '+str(to)+'! \r\n'
        #data='PRIVMSG '+channel+' :Hello! \r\n'
        irc.send(data.encode())
        sys.exit(0)


