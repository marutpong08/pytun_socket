# Pystun Socket
Python pystun and socket

UDP
---
  Client 1
    connect to public stun server and get public IP and Port
    
    Run::
      $ python UDP/client1.py
      
  Client 2
    sending UDP packet to client1
    
    Run::
      $ python UDP/client2.py <client1 public IP> <client1 public Port> <message>

