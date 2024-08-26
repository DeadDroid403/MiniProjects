#! /usr/bin/python3
import paramiko

def command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port=port, username=user, password=passwd)
    except Exception as e:
        print(e)
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print("--------output---------")
        for line in output:
            print(line.strip())

if __name__ == "__main__":
    import getpass
    user = input("enter username:- ")
    passwd = getpass.getpass("enter pass:- ")
    ip = input("Enter IP Address Here:- ")
    port = 22
    while True:
        cmd = input(">> ")
        command(ip,port,user,passwd,cmd)
        if cmd == "exit":
            break
    print("bye")
