import numpy as np


def main():
    first_ogid()


def first_ogid():
    x, y = np.ogrid[1:4:1, 1:5:2]
    print(x)
    print(y)
    x, y = np.ogrid[1:4:3j, 1:5:2j]
    print(x)
    print(y)
    x=np.ogrid[1:5:2]
    print(x)


if __name__ == "__main__":
    main()
