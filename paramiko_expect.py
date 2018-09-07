from paramiko_expect import SSHClientInteraction
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="192.168.113.254",username="",password="",allow_agent=False,look_for_keys=False)

with SSHClientInteraction(ssh,timeout=1,display=True) as chan:
    chan.expect("<S5700-edu>")
    
    chan.send("sys\ndis acl 3301\nc1\n")
    
    chan.expect("\[S5700-edu\]c1")

# chan = ssh.invoke_shell()
# chan.setblocking(True)
# chan.send("sys\ndis acl 3301\n")


# while True:
#     try:
#         res1 = chan.recv(9999)
#     except Exception as e:
#         break



# print(res1)


# chan.close()
ssh.close()
