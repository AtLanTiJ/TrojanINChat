import socket, subprocess, threading, os, time


def listen():
    s = socket.socket(socket.AF_INET6)
    s.bind(('::', 4445))
    print('\033[34m等待连接....\033[0m')
    s.listen()
    chanel, client = s.accept()
    with open(f'./log/{time.strftime("%Y-%m-%d")}.log', mode='a+') as f:
        f.write(f'A host connect with me at {time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    lis_return.append(chanel)


def server():
    thread = threading.Thread(target=listen)
    thread.start()
    thread.join()
    chanel = lis_return[-1]
    c_name = chanel.recv(1024).decode('utf-8')
    print(f'\033[34m{c_name}已连接!\033[0m')
    my_info = os.popen('whoami').read()
    chanel.send(my_info.encode('utf-8'))
    while True:
        try:
            receive = chanel.recv(10240).decode('utf-8')
            print(f'{c_name}：{receive}')
            reply = input("我：")
            chanel.send(reply.encode('utf-8'))
        except Exception as e:
            print('\033[31m对方已断开！\033[0m')
            server()

def cite():
    subprocess.run('./dist/getip.exe')
    subprocess.run('./dist/core.exe')


if __name__ == '__main__':
    lis_return = []
    threading.Thread(target=cite).start()
    server()
