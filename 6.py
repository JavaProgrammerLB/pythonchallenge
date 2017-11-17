def read_next(file_name):
    f = open("channel/channel/{}.txt".format(file_name), "r")
    lines = f.readlines()
    for i in range(len(lines)):
        s = lines[i]
        print(s)
        ary = s.split()
        result = ary[-1]
        if result.isdigit():
            read_next(result)
        else:
            pass


read_next(90052)