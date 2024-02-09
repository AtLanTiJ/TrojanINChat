import socket, time

def client(IP):
    s = socket.socket(socket.AF_INET6)
    s.connect((IP, 5556))
    f = open(f'./log/{time.strftime("%Y-%m-%d")}.log', mode='a+')
    while True:
        message = input("输入：")
        s.send(message.encode())
        receive = s.recv(10240).decode('utf-8')
        f.write(f'\n\n{time.strftime("%Y-%m-%d %H:%M:%S")} commend:{message}\n{receive}')
        print(f"{receive}")


if __name__ == '__main__':
    IP = input('目标IP:')
    client(IP)