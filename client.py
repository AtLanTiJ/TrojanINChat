import socket, os

def client(IP):
    s = socket.socket(socket.AF_INET6)
    s.connect((IP, 4445))
    c_name = os.popen('whoami').read().split('\\')[-1].strip()
    s.send(c_name.encode())
    ser_info = s.recv(1024).decode('utf-8')
    print(f'对方信息：{ser_info}')
    while True:
        message = input("我：")
        s.send(message.encode())
        receive = s.recv(10240).decode('utf-8')
        print(f"服务器回复：{receive}")


if __name__ == '__main__':
    IP = input('目标IP:')
    client(IP)