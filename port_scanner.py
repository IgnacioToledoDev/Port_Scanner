import nmap
import os
os.system('clear')


#Variables of the scanner
indicate_target = input("UL OR IP FOR SCANNER PORTS: ") #URL OR IP
first_port = int(input('first port '))
last_port = int(input('last port for the scanner: '))

#List
list_ports = []
port = first_port

list_ports.append(first_port)
list_ports.append(last_port)


    
#functions
def add_ports(ports):
    port = ports[0]
    if port <= ports.pop():
        port += 1
        list_ports.append(port)
        list_ports.sort()
    else:
        return list_ports

add_ports([first_port, last_port])
print(list_ports)

#def get_open_ports(target, ports): 




#called function
#get_open_ports(indicate_target, [first_port, last_port])
