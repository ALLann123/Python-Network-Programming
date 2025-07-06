#!/usr/bin/python3

import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='192.168.1.101', port=22, username='kali', password='kali')

stdin, stdout, stderr = ssh_client.exec_command("ifconfig")

print(stdout.readlines())
print(stderr.readlines())


"""
 python .\try_ssh.py
['ai\n', 'bash.sh\n', 'black_python\n', 'ctf_pico\n', 'cve-2021-31630\n', 'Desktop\n', 'Documents\n', 'Downloads\n', 'github\n', 'github_two\n', 'hacked.txt\n', 'hello_me.txt\n', 'let_try.sh\n', 'make_challenge\n', 'Music\n', 'Own.The.Net (1).ovpn\n', 'Pictures\n', 'Public\n', 'steg\n', 'Templates\n', 'try_hack_me\n', 'Videos\n', 'wewe.txt\n']
[]
(venv) PS J:\Capture_The_Flag\connect_terminal> python .\try_ssh.py
['eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n', '        inet 192.168.1.101  netmask 255.255.255.0  broadcast 192.168.1.255\n', '        inet6 fe80::a00:27ff:fe8c:2bfe  prefixlen 64  scopeid 0x20<link>\n', '        ether 08:00:27:8c:2b:fe  txqueuelen 1000  (Ethernet)\n', '        RX packets 5259  bytes 508935 (497.0 KiB)\n', '        RX errors 0  
dropped 0  overruns 0  frame 0\n', '        TX packets 5799  bytes 561723 (548.5 KiB)\n', '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n', '\n', 'lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536\n', '        inet 127.0.0.1  netmask 255.0.0.0\n', '        inet6 ::1  prefixlen 128  scopeid 0x10<host>\n', '        loop  txqueuelen 1000  (Local Loopback)\n', '        RX packets 2005  bytes 84284 (82.3 KiB)\n', '        RX errors 0  dropped 0  overruns 0  frame 0\n', '        TX packets 2005  bytes 84284 (82.3 KiB)\n', '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n', '\n']
[]
(venv) PS J:\Capture_The_Flag\connect_terminal> 
"""
