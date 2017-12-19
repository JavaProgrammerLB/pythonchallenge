from queue import Queue

def main():
    first_step()


def first_step():
    q = Queue()
    q.put('a')
    q.put('b')
    print(q.get())


if __name__ == "__main__":
    main()
