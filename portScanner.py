# Basic port scanner. This was a little project that I did to learn about some basic
# functionality in python and get used to the syntax. This isn't particularly fast as
# it doesn't use multi-threading. This is only to be used on your own network/on devices
# that you own! I am not responsible if you use this script and set off some corporate networks
# IDS.

import socket
import sys
import time

portList = set()


def dump_to_file():
    for val in portList:
        file = open("ScanResults.txt", "w")
        file.write("Open port: " + str(val))


if len(sys.argv) > 1:
    target_ip = sys.argv[1]
else:
    print("Usage: <target-ip> [<start range of port>] [<end range of port>]")
    sys.exit()

if len(sys.argv) > 3:
    port_low = sys.argv[2]
    port_high = sys.argv[3]
else:
    print("No port range given, using default which is to scan all ports (1-65535)")
    port_low = 1
    port_high = 65536

print("Starting port scan")
startTime = time.localtime()

try:
    for i in range(int(port_low), int(port_high)):
        sock = socket.socket()
        socket.setdefaulttimeout(0.0001)  # for speed
        connection = sock.connect_ex((target_ip, i))
        if connection == 0:
            print("Port " + str(i) + " is open!")
            portList.add(i)
        sock.close()
except socket.gaierror:
    print("ERROR: Unable to resolve IP address" + " " + str(target_ip))
    sys.exit()
except KeyboardInterrupt:
    endTime = time.localtime()
    print("Port scan cancelled. Dumping results to file and shutting down.")
    print("Port scan took: ", end="")
    print(abs(endTime.tm_sec - startTime.tm_sec), end="")
    print(" seconds")
    dump_to_file()
    sys.exit()

endTime2 = time.localtime()

if len(portList) == 0:
    print("No open ports found. Shutting down")
    print("Port scan took: ", end="")
    print(abs(endTime.tm_sec - startTime.tm_sec), end="")
    print(" seconds")
    sys.exit()

print("Port scanner completed. Results dumped to file.")
print("Port scan took: ", end="")
print(abs(endTime.tm_sec - startTime.tm_sec), end="")
print(" seconds")
dump_to_file()
