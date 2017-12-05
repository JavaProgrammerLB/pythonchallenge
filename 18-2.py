def main():
    file = open("swan/plus.png", "rb")
    bs = []
    while True:
        b = file.read()
        if b:
           bs.append(b)
        else:
            break
    print(bs)


if __name__ == "__main__":
    main()