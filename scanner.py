# python3 scanner.py <ip> -> usage

import sys
import socket
from datetime import datetime 

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
    print("Invalid amount of arguments.")
    print("Syntax : python3 scanner.py <ip>")

# add a pretty banner 

print("-" * 50)
print("Scanning target"+target)
print("Time started : "+ str(datetime.now()))

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indcator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program...")
    sys.exit()

except socket.gaierror:
    print("HOSTNAME could not be resolved")
    sys.exit()

except socket.error:
    print("Could'nt connect to server")
    sys.exit()

