#domain to IP

from termcolor import colored

print(colored("******************** Domain To IP ********************",'green'))
print(colored("*************** Created by Jolhus ***************",'green'))

import socket
import pyfiglet

banner=colored(pyfiglet.figlet_format("IP converter"),'green')

domain_name=input("Enter your target domain: ")

print(banner)

ip=socket.gethostbyname(domain_name)

print("IP For {} : {}".format(domain_name,ip))
