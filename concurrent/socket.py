# coding: utf-8

import os
import sys
import socket
import math

def task(min, max):
    r = 0.0
    for i in range(min, max):
        r += 1.0 / (2 * i + 1) ** 2
    return r



def main(n, section_num = 10):
    childs = {}
    section = n / section_num
    for i in range(section_num):
        min = section * i
        max = min + section
        
        rs, ws = socket.socketpair()
        pid = os.fork()
        if pid > 0:
            childs[pid] = rs
            ws.close()
        else:
            rs.close()
            s = task(min, max)
            ws.send(str(s))
            ws.close()
            sys.exit(0)
    sums = []
    for pid, rs in childs.items():
        sums.append(float(rs.recv(1024)))
        rs.close()
        os.waitpid(pid, 0)
    return math.sqrt(sum(sums) * 8)
        
    pass


if __name__ == "__main__":
    main(1000 * 10000)
