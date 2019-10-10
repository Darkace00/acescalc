import socket

target_host = "www.edsgarage.eu"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("Get / HTTP/1.1\r\nHost: edsgarage.eu\r\n\r\n")

response = client.recv(4096)

print (response)
