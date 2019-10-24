import os
import subprocess


ip = input("IP address? ")
print ("Scanning IP Address: " + ip)

subnet = ip.split(".")

FNULL = open(os.devnull, 'w')

processes = []

for x in range(1, 255):
    ip2 = subnet[0]+"." + subnet[1] + "." + subnet[2] + "." + str(x)
    process = subprocess.Popen(
        ['ping', '-n', '1', '-w', '500', ip2], stdout=FNULL, stderr=subprocess.STDOUT)
    processes.append((ip2, process))

for ip2, process in processes:
    response = process.wait()
    if response == 0:
        print(ip2, 'is up!')
    # else:
    #     print(ip2, 'is down!')
