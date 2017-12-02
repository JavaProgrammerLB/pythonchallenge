import http.cookiejar, urllib.request, urllib.parse
import bz2
import http.cookies


def main():
    cookie_jar = http.cookiejar.CookieJar()
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
    print("pw is {}".format(password))



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


if __name__ == "__main__":
    main()