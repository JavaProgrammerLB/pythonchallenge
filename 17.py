from http.cookiejar import CookieJar
import urllib.parse
import bz2
import requests


def main():
    first_step()
    # second_step()


def first_step():
    cookie_jar = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    ary = []
    next_number = open_url(cookie_jar, opener, "12345", ary)
    while True:
        if int(next_number) > 0:
            next_number = open_url(cookie_jar, opener, next_number, ary)
        else:
            break
    encoded_string = "".join(ary)
    print("ary length is {}".format(len(ary)))
    print("bs is {}", encoded_string)
    password = bz2.decompress(str.encode(encoded_string, "latin1"))
    print("{}".format(password.decode()))


def open_url(cookie_jar, opener, number, ary):
    url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    next_number = request_url(cookie_jar, opener, url_base + number, ary)
    return next_number


def request_url(cookie_jar, opener, url, ary):
    response = opener.open(url)
    for item in cookie_jar:
        print("{} {}".format(item.name, item.value))
        value = item.value
        b = urllib.parse.unquote_plus(value, "latin1")
        ary.append(b)
    print("ary is {}".format(ary))
    data = response.read()
    ary = data.decode()
    next_number = find_next_number(ary)
    return next_number


def find_next_number(doc):
    flag = "and the next busynothing is "
    length = len(flag)
    if flag in doc:
        index = doc.index(flag)
    else:
        return "-1"
    number = doc[index + length:]
    return number


def second_step():
    php_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    cookies = {"info":"the flowers are on their way"}
    res = requests.get(php_url, cookies=cookies)
    response_doc = res.text
    print(response_doc)


if __name__ == "__main__":
    main()