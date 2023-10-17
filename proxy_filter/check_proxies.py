
import threading
import queue
import requests
import time


def check_proxies():
    q = queue.Queue()
    valid_proxies = []

    # Reading the free_proxy_list file and store the proxies in a queue
    with open('free_proxy_list.txt', 'r') as file:
        proxies = file.read().split('\n')
        for proxy in proxies:
            q.put(proxy)

    # Checking if response time of each proxy is good and valid
    def check_proxy():
        while not q.empty():
            proxy = q.get()
            try:
                response = requests.get(
                    "https://www.daraz.com.bd/", timeout=30, proxies={"http": proxy, "https": proxy})
            except:
                continue
            # If everything is ok then add the proxy in valid proxy list
            if response.status_code == 200:
                valid_proxies.append(proxy)

    # Running 100 threads to check to proxies quickly
    for _ in range(100):
        threading.Thread(target=check_proxy).start()

    while threading.active_count() > 1:
        time.sleep(5)

    '''
    Write the valid_proxy list in proxy_list.txt file in our scrapy project.
    So that we can fetch valid proxies from our project quickly.
    '''
    with open('../tech_product_scraper/tech_product_scraper/proxy_list.txt', 'w') as file:
        for item in valid_proxies:
            file.write(item + "\n")

    return 'Done'


if __name__ == "__main__":
    check_proxies()
