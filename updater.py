#!/usr/bin/python3

import subprocess
import paramiko

def update_apache(hostname,username,password):
    try:
        host = hostname
        port = 22
        username = username
        password = password

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        
        stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')
        print(stdout.read().decode())
        print(stderr.read().decode())
        
        stdin, stdout, stderr = ssh.exec_command('dpkg -l')
        apache_installed = stdout.read().decode()
        if "apache2" in apache_installed:
            stdin, stdout, stderr = ssh.exec_command('sudo apt install --only-upgrade apache2 -y')
            print(stdout.read().decode())
            print(stderr.read().decode())
            ssh.exec_command('sudo systemctl restart apache2')
                  
        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")


def update_nginx(hostname, username, password):
    try:
        host = hostname
        port = 22
        username = username
        password = password

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')
        print(stdout.read().decode())
        print(stderr.read().decode())

        stdin, stdout, stderr = ssh.exec_command('dpkg -l')
        nginx_installed = stdout.read().decode()
        if "nginx" in nginx_installed:
            stdin, stdout, stderr = ssh.exec_command('sudo apt install --only-upgrade nginx -y')
            print(stdout.read().decode())
            print(stderr.read().decode())
            ssh.exec_command('sudo systemctl restart nginx')

        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    choice = input("Which system would you like to update? (A)pache, (N)ginx, (I)is: ")

    if choice in ["A", "Apache", "apache"]:
        hostname = input("Give the hostname/ip_address of the machine: ")
        username = input("Give the username to connect to the machine: ")
        password = input("Give the user password: ")
        update_apache(hostname, username, password)
    elif choice in ["N", "Nginx", "nginx"]:
        hostname = input("Give the hostname/ip_address of the machine: ")
        username = input("Give the username to connect to the machine: ")
        password = input("Give the user password: ")
        update_nginx(hostname, username, password)
    else:
        print("Invalid choice. Please select either Apache or Nginx.")