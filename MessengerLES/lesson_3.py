from socket import socket, SOCK_STREAM, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import subprocess

from _socket import SO_BROADCAST


def server_TCP():
    SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
    SERVER_SOCKET.bind(('', 7777))
    SERVER_SOCKET.listen(2)
    try:
        while True:
            CLIENT_SOCKET, CLIENT_ADDR = SERVER_SOCKET.accept()
            DATA = CLIENT_SOCKET.recv(4096)
            CLIENT_SOCKET.send("Сообщение клиенту".encode("utf-8"))
            CLIENT_SOCKET.close()
    finally:
        SERVER_SOCKET.close()


def client_TCP():
    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect(('localhost', 7777))
    CLIENT_SOCKET.send("Сообщение серверу".encode("utf-8"))
    DATA = CLIENT_SOCKET.recv(4096).decode('utf-8')
    CLIENT_SOCKET.close()


def server_UDP():
    SERVER_SOCKET = socket(AF_INET, SOCK_DGRAM)
    SERVER_SOCKET.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    SERVER_SOCKET.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    SERVER_SOCKET.bind(('', 7777))
    try:
        while True:
            msg, addr = SERVER_SOCKET.recvfrom(1024)
            msg.decode('utf-8')
            SERVER_SOCKET.sendto('answer'.encode('utf-8'))
    finally:
        SERVER_SOCKET.close()


def client_UDP():
    CLIENT_SOCKET = socket(AF_INET, SOCK_DGRAM)
    CLIENT_SOCKET.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    try:
        CLIENT_SOCKET.sendto('Сообщение серверу'.encode('utf-8'), ('localhos', 7777))
        msg, addr = CLIENT_SOCKET.recvfrom(1024)
        msg.decode('utf-8')
    finally:
        CLIENT_SOCKET.close()


if __name__ == '__main__':
    PROCESS = []
    num_process = 6
    while True:
        ACTION = input('q-выход; x-закрыть все окна; s-запустить сервер и клиент')
        if ACTION == 'q':
            break
        elif ACTION == 's':
            PROCESS.append(subprocess.Popen('python client_TCP()',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
            for consol in range(num_process):
                PROCESS.append(subprocess.Popen('python client_TCP()',
                                                creationflags=subprocess.CREATE_NEW_CONSOLE))
        elif ACTION == 'x':
            while PROCESS:
                PROCESS.pop().kill()
