# bof-fuzzer
This is a buffer overflow fuzzer written in Python. A few lines should be modified to make this work for what you're testing:

## Line 10 
``` while(size < 2000):   ```
 - This starts the while loop. This will keep the loop going until the buffer reaches a length of 2,000 characters. If you want to test up to a higher number, change this value.

## Line 16 
``` content = "username=" + inputBuffer + "&password=A" ```
 - This contains the string that will be submitted to the application. This should be modified to match the expected input of the application you're testing. For example, the last application that I tested with this was expecting a POST request that looked like "username=something&password=something".

## Line 20
``` buffer += "Host: 10.11.0.22\r\n"  ```
 - This contains the IP address of the application being tested. Modify this to match your desired address.
 
 ## Line 26
 ``` buffer += "Referer: http://10.11.0.22/login\r\n" ```
  - This contains the address of the page that should be sending you here. Adjust as needed.
  
## Line 36
``` s.connect(("10.11.0.22", 80)) ```
 - This contains the IP address and port (80) of the application being tested. Modify this to match your desired address and port.
