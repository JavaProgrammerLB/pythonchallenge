from concurrent import futures


def foo(x, y):
    print("{}-{}={}".format(y, x, y - x ))
    return y - x


def main():
    with futures.ProcessPoolExecutor() as pool:
        pool.map(foo, [1, 2, 3], [4, 7, 1000])


if __name__ == '__main__':
    main()
