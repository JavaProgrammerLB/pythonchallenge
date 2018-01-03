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
    # read_bin_file("copper/white.gif")
    # read_bin_file("channel/channel.zip")
    # read_bin_file("maze/maze.zip")
    # read_bin_file("lake/2.wav")
    # read_bin_file("indian/indian.wav")
    # read_bin_file("indian/result.wav")
    # read_bin_file("maze/maze/mybroken.gif")
    # read_bin_file("lake/lake1.jpg")
    read_bin_file("maze/maze/mybroken.zip")