import math
import statistics
import threading
import time

import requests


ALL_THREAD_NUM = 10000
TIMEOUT_THREAD_NUM = ALL_THREAD_NUM // 5
TIMEOUT_THREAD_NUM = ALL_THREAD_NUM
THREAD_LIST = list()
no_timeout_cost_time_list = list()
timeout_cost_time_list = list()
resp_code_list = list()

url_list = [
    "http://192.168.9.99/agw/v1/req/test/timeout",
    "http://192.168.9.99/agw/v1/req/test"
]


def worker(url: str, cost_time_list: list):
    start = time.time()
    res = requests.get(url)
    # print(res.status_code, res.json())
    if res.status_code == 200:
        resp_code_list.append(1)
        cost_time_list.append(time.time() - start)
    else:
        resp_code_list.append(0)


for i in range(ALL_THREAD_NUM):
    if i < TIMEOUT_THREAD_NUM:
        t_url = url_list[0]
        t_cost_time_list = timeout_cost_time_list
    else:
        continue
        t_url = url_list[1]
        t_cost_time_list = no_timeout_cost_time_list
    t = threading.Thread(target=worker, name=f"MyThread_{i}", args=(t_url, t_cost_time_list))
    THREAD_LIST.append(t)
    t.start()


for thread in THREAD_LIST:
    thread.join()


print("【timeout_cost_time_list】", timeout_cost_time_list)
print(ALL_THREAD_NUM, sum(resp_code_list))
print("【timeout_cost_time_list 平均】", round(statistics.mean((timeout_cost_time_list)), 2))
# print("【no_timeout_cost_time_list】", no_timeout_cost_time_list)
# print("【no_timeout_cost_time_list 平均】", round(statistics.mean(no_timeout_cost_time_list), 2))