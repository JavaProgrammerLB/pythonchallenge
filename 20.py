import requests
import zipfile


def main():
    url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
    auth = ("butter", "fly")
    # first_step(url, auth)
    # second_step(url, auth)
    # third_step(url, auth)
    # fourth_step(hint)
    # five_step(url, auth)
    # six_step(url, auth)
    seven_step("fence/1152983631.zip")


def first_step(url, auth):
    res = requests.get(url, auth=auth)
    res_header = res.headers
    res_content = res.content
    print("res_header is {}, res_content is {}".format(res_header, res_content))
    # 'Content-Range': 'bytes 0-30202/2123456789


def second_step(url, auth):
    start = 0
    while True:
        print("start is {}".format(start))
        if start >= 2123456789:
            break
        headers = {"RANGE": "bytes={}-".format(start)}
        res = requests.get(url, auth=auth, headers=headers)
        res_headers = res.headers
        res_content_range = res_headers.get("Content-Range")
        if res_content_range is not None:
            begin, end = get_start_end(res_content_range)
            print("===================== {} ========================".format(start))
            print("res_content is {}".format(res.content))
            print("res_heads is {}".format(res.headers))
            print("res_raw is {}".format(res.raw))
            print("res_text is {}".format(res.text))
            print("res_cookies is {}".format(res.cookies))
            print("=================================================")
            start = int(end)
        else:
            start += 1


def get_start_end(st):
    bscount_sum = st[6:]
    start_to_end = bscount_sum.split("/")[0]
    start = start_to_end.split("-")[0]
    end = start_to_end.split("-")[1]
    print("start is {}, end is {}".format(start, end))
    return start, end


def third_step(url, auth):
    request_url_with_range(url, auth, 2123456789)
    # esrever ni emankcin wen ruoy si drowssap eht


def request_url_with_range(url, auth, num):
    headers = {"RANGE": "bytes={}-".format(num)}
    res = requests.get(url, auth=auth, headers=headers)
    print("=================================================")
    print("res_content is {}".format(res.content))
    print("res_heads is {}".format(res.headers))
    print("res_raw is {}".format(res.raw))
    print("res_text is {}".format(res.text))
    print("res_cookies is {}".format(res.cookies))
    print("=================================================")


def fourth_step(hint):
    result = ""
    for i in range(len(hint) - 1, -1, -1):
        result += hint[i]
    print(result)
    return result
    # the password is your new nickname in reverse


def five_step(url, auth):
    request_url_with_range(url, auth, 2123456743)
    # and it is hiding at 1152983631.


def six_step(url, auth):
    headers = {"RANGE": "bytes={}-".format(1152983631)}
    res = requests.get(url, auth=auth, headers=headers)
    print(res.content)
    file = open("fence/1152983631.zip", "wb")
    file.write(res.content)
    print("finished")


def seven_step(file_path):
    with zipfile.ZipFile(file_path) as myzip:
        pwd = fourth_step("invader")
        print(pwd)
        files = myzip.filelist
        for file in files:
            with myzip.open(file.filename, pwd=pwd.encode()) as tem_file:
                print(tem_file.read())


if __name__ == "__main__":
    main()
