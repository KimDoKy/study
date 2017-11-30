import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('czarcie.com', 22, 'ubuntu', key_filename='/home/your_user/.ssh/id_rsa')

stdin, stdout, stderr = ssh.exec_command('ls -l /home')

for line in stdout:
    print(line, end="")

ssh.close()
