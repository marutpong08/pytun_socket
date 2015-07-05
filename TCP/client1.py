import stun
import socket
import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    sip = "0.0.0.0" # interface to listen on (all)
    port = 54322 # port to listen on
    nat_type, external_ip, external_port = stun.get_ip_info(sip, port)

    print nat_type
    print external_ip
    print external_port

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((sip, port), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
