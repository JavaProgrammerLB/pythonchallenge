def read_bin_file(file_path):
    file = open(file_path, "rb")
    bs = []
    while True:
        b = file.read()
        if b:
           bs.append(b)
        else:
            break
    print(bs)


if __name__ == "__main__":
    read_bin_file("copper/white.gif")