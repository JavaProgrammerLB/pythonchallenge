import difflib


def main():
    left, right = first_step()
    second_step(left, right)


def first_step():
    deltas = open("swan/deltas", 'r')
    left = ""
    right = ""
    while True:
        line = deltas.readline()
        if line:
            left += line[:53]
            left += "\n"
            right += line[56:]
        else:
            break
    return left, right


def second_step(left, right):
    pass


if __name__ == "__main__":
    main()