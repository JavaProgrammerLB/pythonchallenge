if __name__ == "__main__":
    file1 = open("swan/left.patch", "r")
    file2 = open("swan/liubei.txt", "w")
    while True:
        line = file1.readline()
        if not line:
            break
        if line.startswith("+") or line.startswith("-"):
            file2.write(line)
