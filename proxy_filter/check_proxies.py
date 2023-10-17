
import threading
import queue
import requests
import time


def check_proxies():
    q = queue.Queue()
    valid_proxies = []

    with open('free_proxy_list.txt', 'r') as file:
        proxies = file.read().split('\n')
        for proxy in proxies:
            q.put(proxy)

    def check_proxy():
        while not q.empty():
            proxy = q.get()
            try:
                response = requests.get(
                    "https://www.daraz.com.bd/", timeout=30, proxies={"http": proxy, "https": proxy})
            except:
                continue
            if response.status_code == 200:
                valid_proxies.append(proxy)

    for _ in range(100):
        threading.Thread(target=check_proxy).start()

    while threading.active_count() > 1:
        time.sleep(5)

    with open('../darazscraper/darazscraper/proxy_list.txt', 'w') as file:
        for item in valid_proxies:
            file.write(item + "\n")

    return 'Done'


if __name__ == "__main__":
    check_proxies()
