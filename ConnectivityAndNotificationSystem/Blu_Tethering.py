#######Change this file based on Bluetooth Pairing
# package required for 'pand' command
sudo apt-get install bluez-compat
 
# connect to phone and sets up network interface
sudo pand --connect 0E:C9:35:42:E6:E9 -n
 
# show networks
ifconfig
bnep0     Link encap:Ethernet  HWaddr 00:4d:9c:2a:47:94  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:12 (12.0 B)  TX bytes:60 (60.0 B)

 
# set dhclient to use bnep0 
sudo dhclient bnep0
 
# test internet connectivity
ping www.google.com
