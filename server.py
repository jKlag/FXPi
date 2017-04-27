import SocketServer
import os

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        """
        Dictionary containing available effects
        """
        EFFECTS = {"DSP":0,"FUZZ":1,"WAH":2,"VIBRATO":3,"DELAY":4}
        while True:
            # self.request is the TCP socket connected to the client
            self.data = self.request.recv(1024).strip()
            print "{} wrote:".format(self.client_address[0])
            print self.data
            dataarr = self.data.split(' ')
            if dataarr[0].upper() in EFFECTS:
                effect = EFFECTS[dataarr[0].upper()]
                cmd = 0
                if dataarr[1].upper() == 'ON':
                    cmd = 1

                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
                os.system("echo '" + str(effect) + ' ' + str(cmd) + ";' | pdsend 3000")
            else:
                self.request.sendall(self.data.upper() + ":\nCommand not recognized")

if __name__ == "__main__":
    HOST, PORT = str(os.system("ip -f inet -o addr show $INTERFACE|cut -d\  -f 7 | cut -d/ -f 1")), 9996
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    os.system("echo '0 1;' | pdsend 3000")
    os.system("echo '1 0;' | pdsend 3000")
    os.system("echo '2 0;' | pdsend 3000")
    os.system("echo '3 0;' | pdsend 3000")
    os.system("echo '4 0;' | pdsend 3000")
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
