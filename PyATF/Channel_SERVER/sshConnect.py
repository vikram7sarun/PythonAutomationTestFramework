import paramiko



p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect("",port=22,username="",password="")
stdin ,stdout , stderr = p.exec_command("")
opt =stdout.readlines()
opt ="".join(opt)
print(opt)

