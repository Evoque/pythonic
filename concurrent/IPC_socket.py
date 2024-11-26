

'''
通过socket，实现进程间的通信
'''

import socket
import os
import time

pid = os.getpid()
print('[Current pid] ', pid)

# 测试主进程中实现两个socket通信
rs, ws = socket.socketpair()

child_pid = os.fork()

if child_pid == 0:
    pid = os.getpid()
    print(pid, '[child before send] ')
    ws.send(b'Hello from child process')
    print(pid, '[after child send] ')
    # time.sleep(0.1)
    # ws.send(b'Hello from child process 11')
    print(pid, '[after child ws close] ')
    ws.close()
    # time.sleep(0.1)

if  child_pid != 0:
    ws.close()
    while True:
        print( pid, '[Before Receive]')
        receive_str = rs.recv(1024)
        print( pid, '[Receive]', '--', receive_str)
        time.sleep(2)
        
# rs.close()

if child_pid == 0:
    print(pid, '[child end]')
    # ws.close()
else:
    
    print(pid, '[parent end] ') 
    os.waitpid(child_pid, 0)


# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket.bind(('127.0.0.1', 12350))
# serversocket.listen()

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('127.0.0.1', 12350))

# server_client_socket, ar = serversocket.accept()

# client_socket.send(b'Send MSG!')
# print('[After Sending]')
# client_socket.close()

# recv = server_client_socket.recv(1024)
# print('[After Receiving]', recv)
# recv = server_client_socket.recv(1024)
# print('[After Receiving]', recv)
# recv = server_client_socket.recv(1024)
# print('[After Receiving]', recv)
# recv = server_client_socket.recv(1024)
# print('[After Receiving]', recv)