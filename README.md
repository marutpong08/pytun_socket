# Pystun Socket
Python pystun and socket

UDP
---
  Client 1
    A STUN client for connecting to public stun server and getting public IP and Port.
    It's a UDP server.
    
    
        $ python UDP/client1.py
      
  Client 2
    Sending a UDP packet to client1 with following arguments
    
    
        $ python UDP/client2.py <client1 public IP> <client1 public Port> <message>

