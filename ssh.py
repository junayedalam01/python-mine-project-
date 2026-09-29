import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = input("Enter Host :")
user =input("Enter Username : ")
passwed =input("Enter PAssword : ")
try:
    ssh.connect(host, username=user, password=passwed)
    print("ssh connact ..")
    command =input("Enter Command : ")
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())

    ssh.close()
except:
    print("Password or username not mach!...")

