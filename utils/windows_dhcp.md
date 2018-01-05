
1. Download DHCP Server for Windows. It is a 100kB download available here. http://www.dhcpserver.de/cms/
2. Go to the IPv4 properties page of the Ethernet adapter and set a fixed IP address, say 192.168.2.1
3. Run the DHCP Server Wizard (downloaded above)
4. Select the Ethernet adapter from the list shown
5. Save the configuration file and start up the DHCP Server
6. Click the 'Continue as tray app' button in the server control panel.
7. Boot up the Raspberry Pi
8. A popup notification shows the IP address assigned by the DHCP server to the Raspberry Pi.
9. Use a SSH client, like PuTTy, to connect to the IP address shown
