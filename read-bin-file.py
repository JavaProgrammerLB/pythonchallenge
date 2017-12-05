def read_bin_file():
    file = open("evil/0.jpg", "rb")
    bs = []
    while True:
        b = file.read()
        if b:
           bs.append(b)
        else:
            break
    print(bs)


if __name__ == "__main__":
    read_bin_file()