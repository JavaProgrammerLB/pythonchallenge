import zipfile

z = zipfile.ZipFile("channel/channel.zip", "r")
b = b""


def read_next(file_name):
    global z
    global b
    b += z.getinfo("{}.txt".format(file_name)).comment
    f = open("channel/channel/{}.txt".format(file_name), "r")
    lines = f.readlines()
    for i in range(len(lines)):
        s = lines[i]
        ary = s.split()
        result = ary[-1]
        if result.isdigit():
            read_next(result)
        else:
            pass

read_next(90052)
print(b.decode())
