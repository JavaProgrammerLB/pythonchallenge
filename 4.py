import requests

def getNext(arg):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    params = "nothing={}".format(arg)
    res = requests.get(url, params)
    cont = res.text
    print(cont)
    ary = cont.split(' ')
    next_arg = ary[-1]
    if next_arg.isdigit():
        print(next_arg)
        getNext(next_arg)
    else:
        print("result is: {}".format(next_arg))


getNext(12345)