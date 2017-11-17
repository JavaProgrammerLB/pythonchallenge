import pickle

src = open('pickle/banner.p', 'rb')
result = pickle.load(src)


def print_ary(ary, s):
    for i in range(len(ary)):
        element = ary[i]
        s = ""
        for i in range(len(element)):
            sub_element = element[i]
            s += sub_element[0] * sub_element[1]
        print(s)


print_ary(result, "")

