
import subprocess
target = 0
up = 0
down = 0
while (target < 255):
        ip = "192.168.1." + str(target)
        output = subprocess.Popen(
            ["ping", "-n", "1", ip], stdout=subprocess.PIPE).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
                print ('Host ' + ip + " is offline or unavailable")
                down += 1
        else:
                print ("Host " + ip + " is online")
                up += 1

        target = target+1


print ("A total of " + str(up+down) + " hosts were scanned.")
print (str(up) + " hosts were alive, and " + str(down) + " hosts were unreachable. ")
quit()
