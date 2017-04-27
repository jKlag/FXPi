import socket
import sys

HOST, PORT = "fxpi.duckdns.org", 9996

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(50)
print "Type <effect> <on/off> to toggle effect"
print "Type \"exit\" to quit"
try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        data = raw_input('Enter Command: ')
        if data == "exit":
            break
        sock.sendall(data + "\n")

        # Receive data from the server and shut down
        received = sock.recv(1024)
        print "TURNED {}".format(received)
finally:
    sock.close()
