from concurrent.futures import ThreadPoolExecutor
import requests


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


def req(pool):
    URLS = ["https://www.baidu.com", "http://www.qq.com", "https://www.tencent.com"]
    results = pool.map(task, URLS)
    for result in results:
        print("{}, {}".format(result.url, len(result.content)))


def insert_dic(dic, key, value):
    dic[key] = value


def remove_dic(dic, key):
    del dic[key]


def start_operation(dic, pool):
    pool.submit(insert_dic, dic, "hello", "world")


def main():
    pool = ThreadPoolExecutor(max_workers=3)
    # req(pool)
    dic = {}
    start_operation(dic, pool)
    print(dic)


if __name__ == '__main__':
    main()
