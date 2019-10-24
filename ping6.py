import socket
import os
import sys

up_ip = []  # list to store the ip-addresses of server online
for x in range(254):  # here range is 0-100. You can change the range according to your comfort
    server_ip = '192.168.1.' + str(x)
    rep = os.system('ping -n 1 ' + server_ip)

    if rep == 0:
        # upip.append(server_ip)
        print ('*******************Server Is Up****************\n')
    else:
        print ('server is down \n')

print (up_ip)
