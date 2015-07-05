import stun
import socket

sip = "0.0.0.0" # interface to listen on (all)
port = 54321 # port to listen on
nat_type, external_ip, external_port = stun.get_ip_info(sip, port)

print nat_type
print external_ip
print external_port

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.settimeout(60.0)
sock.bind((sip, port))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	sent = sock.sendto(data, addr)
