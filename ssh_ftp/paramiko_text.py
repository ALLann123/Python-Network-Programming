#!/usr/bin/python3
import paramiko
import socket

#get user data
host = input("Enter the IP>> ")
name = input("Enter username: ")
pass_word = input("What is the password? ")

try:
	ssh_client=paramiko.SSHClient()
	paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
	#The following lines add the server key automatically to the know_hosts file
	ssh_client.load_system_host_keys()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	response=ssh_client.connect(host, port=22, username=name, password=pass_word)
	print(f"[+]Connected to host {host} on port 22: ", response)
	security_options=transport.get_security_options()
	print(security_options.kex)
	print(security_options.ciphers)
except Exception as e:
	print(f"Error: {e}")  # Handle exceptions and print error messages


'''
python paramiko_test.py         
Enter the IP>> 127.0.0.1
Enter username: kali
What is the password? kali
DEBUG:paramiko.transport:starting thread (client mode): 0xdf83e30
DEBUG:paramiko.transport:Local version/idstring: SSH-2.0-paramiko_3.4.0
DEBUG:paramiko.transport:Remote version/idstring: SSH-2.0-OpenSSH_9.7p1 Debian-7
INFO:paramiko.transport:Connected (version 2.0, client OpenSSH_9.7p1)
DEBUG:paramiko.transport:=== Key exchange possibilities ===
DEBUG:paramiko.transport:kex algos: sntrup761x25519-sha512@openssh.com, curve25519-sha256, curve25519-sha256@libssh.org, ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521, diffie-hellman-group-exchange-sha256, diffie-hellman-group16-sha512, diffie-hellman-group18-sha512, diffie-hellman-group14-sha256, ext-info-s, kex-strict-s-v00@openssh.com
DEBUG:paramiko.transport:server key: rsa-sha2-512, rsa-sha2-256, ecdsa-sha2-nistp256, ssh-ed25519
DEBUG:paramiko.transport:client encrypt: chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr, aes128-gcm@openssh.com, aes256-gcm@openssh.com
DEBUG:paramiko.transport:server encrypt: chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr, aes128-gcm@openssh.com, aes256-gcm@openssh.com
DEBUG:paramiko.transport:client mac: umac-64-etm@openssh.com, umac-128-etm@openssh.com, hmac-sha2-256-etm@openssh.com, hmac-sha2-512-etm@openssh.com, hmac-sha1-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, hmac-sha2-256, hmac-sha2-512, hmac-sha1
DEBUG:paramiko.transport:server mac: umac-64-etm@openssh.com, umac-128-etm@openssh.com, hmac-sha2-256-etm@openssh.com, hmac-sha2-512-etm@openssh.com, hmac-sha1-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, hmac-sha2-256, hmac-sha2-512, hmac-sha1
DEBUG:paramiko.transport:client compress: none, zlib@openssh.com
DEBUG:paramiko.transport:server compress: none, zlib@openssh.com
DEBUG:paramiko.transport:client lang: <none>
DEBUG:paramiko.transport:server lang: <none>
DEBUG:paramiko.transport:kex follows: False
DEBUG:paramiko.transport:=== Key exchange agreements ===
DEBUG:paramiko.transport:Strict kex mode: True
DEBUG:paramiko.transport:Kex: curve25519-sha256@libssh.org
DEBUG:paramiko.transport:HostKey: ssh-ed25519
DEBUG:paramiko.transport:Cipher: aes128-ctr
DEBUG:paramiko.transport:MAC: hmac-sha2-256
DEBUG:paramiko.transport:Compression: none
DEBUG:paramiko.transport:=== End of kex handshake ===
DEBUG:paramiko.transport:Resetting outbound seqno after NEWKEYS due to strict mode
DEBUG:paramiko.transport:kex engine KexCurve25519 specified hash_algo <built-in function openssl_sha256>
DEBUG:paramiko.transport:Switch to new keys ...
DEBUG:paramiko.transport:Resetting inbound seqno after NEWKEYS due to strict mode
DEBUG:paramiko.transport:Got EXT_INFO: {'server-sig-algs': b'ssh-ed25519,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,rsa-sha2-512,rsa-sha2-256', 'publickey-hostbound@openssh.com': b'0', 'ping@openssh.com': b'0'}
DEBUG:paramiko.transport:userauth is OK
INFO:paramiko.transport:Authentication (password) successful!
[+]Connected to host 127.0.0.1 on port 22:  None
Error: name 'transport' is not defined
'''
