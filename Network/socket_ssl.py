#!/usr/bin/python3
import ssl
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

secure_socket=ssl.wrap_socket(sock)
data=bytearray()
domain=input("Enter Target domain>> ")
try:
	secure_socket.connect((domain, 443))
	print(secure_socket.cipher())
	secure_socket.write(b"GET / HTTP/1.1 \r\n")
	secure_socket.write(b"Host: www.google.com\n\n")

	data=secure_socket.read()
	print(data.decode("utf-8"))

except Exception as error:
	print("Exception: ", error)

'''
Enter Target domain>> google.com
('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)
HTTP/1.1 200 OK
Date: Thu, 20 Feb 2025 21:17:07 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-IjsNFBFAJ7k8pzgkcXOxlQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Accept-CH: Sec-CH-Prefers-Color-Scheme
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: AEC=AVcja2eE9Z0PQPeU2Qpe0dPlIRNptrj-Y_PKDeWpF760AUPGEtNqXW_YNQ; expires=Tue, 19-Aug-2025 21:17:07 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
Set-Cookie: NID=521=TX4uHXGVPMI_uqEjaVgI00PgbEAHiWmsBQm87lRSU9xbyyG2brtQRlIkqIve4HYvyu5s4_benUYF36lEeqVrlrbHhM9wyrLucG3w0HQEpnaFGlj1N6Dl8qXiqQ4kmzAblwqEnHM0yUJNlKGp5pPPISP_FfTH4FcJazxyAIbMiwqRTMDDBBExM0SWyv-g9q1ORIGh8tsS4v0r; expires=Fri, 22-Aug-2025 21:17:07 GMT; path=/; domain=.goog
'''
