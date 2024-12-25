"""
PEP 324: https://peps.python.org/pep-0324/

"""

# a new module for starting and communicating with processes.

# Functions for process creation
""" Methods of process creation
1. os.fork(): 不跨平台(Linux & Unix)
2. multiprocessing.Process: 跨平台(Windows & Linux),单个子进程的创建
3. multiprocessing.Pool: 处理并管理多个子进程
3. subprocess: 执行外部命令，与系统命令交互

involved technical terms:
- popen2
- A hook for executing custom code between fork and exec. This can be used for, for exp, changing uid.
- file descriptor redirection: redirect stderr, but not stdout.
- This is not possible with current functions, without using temporary files.
- With the subprocess module, it's possible to control if all open file descriptors should be closed before the new program is executed.
- Support for connecting several subprocesses(shell "pipe")
- `communicate()`: send `stdin` data and read `stdout`,`stderr` data without risking deadlocks.
"""


import os
from multiprocessing import Process, Queue, Pipe, Lock, set_start_method

# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(f'1 -> {type(q.get())}')
#     print(f'2 -> {q.get()}')
#     p.join()


# def pf(conn):
#     conn.send(b"hello")
#     conn.close()
    
# if __name__ == '__main__':
#     pc,cc = Pipe()
#     p = Process(target=pf, args=(cc,))
#     p.start()
#     rec = pc.recv()
#     print(f'result:{rec}, type: {type(rec)}')
#     p.join()


def lf(l, i):
    l.acquire() 

    try:
        print(f'hello world-{i}, pid:{os.getpid()}')
    finally:
        l.release()

import time 

if __name__ == '__main__':
    set_start_method('fork')
    lock = Lock() 
    
    Process(target=lf, args=(lock, 1)).start()
     
    # for num in range(10):
    #     Process(target=lf, args=(lock, num)).start()
    
    # time.sleep(0.1)