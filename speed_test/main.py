#!/usr/bin/python3
import speedtest

#create a speedtest object. Can do a download, upload or evaluate the ping
test=speedtest.Speedtest()

#---------This is just the setup
print("[+]Loading server list")
test.get_servers() # -> get list of servers available for speedtest

print("Choosing best Server...\n")
best=test.get_best_server()  #choose best server

print(f"found:{best['host']}\n Located in {best['country']}")


#--------Now lets do a speedtest i.e Download and Upload
print("\nPerforming download test....")
download_result=test.download()

print("\nPerforming Upload test....")
upload_result=test.upload()

ping_result=test.results.ping

#we convert the speed test results to mbps, if you want in kbps divide with 1024 ones.'.2f' refers to the decimal places we want
print(f"Download Speed: {download_result/1024/1024:.2f} Mbit/s")
print(f"Upload Speed: {upload_result/1024/1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")



"""
python .\main.py
[+]Loading server list
Choosing best Server...

found:speedtest.telkom.co.ke:8080
 Located in Kenya

Performing download test....

Performing Upload test....
Download Speed: 0.62 Mbit/s
Upload Speed: 5.08 Mbit/s
Ping: 59.09 ms
"""