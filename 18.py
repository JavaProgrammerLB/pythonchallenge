import difflib


def main():
    left, right = first_step()
    diff = second_step(left, right)
    third_step(diff)


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
    diff = difflib.ndiff(left.splitlines(keepends=True), right.splitlines(keepends=True))
    result = "".join(diff)
    return result


def third_step(diff):
    plus = open("swan/plus.png", "wb")
    subtraction = open("swan/subtraction.png", "wb")
    space = open("swan/space.png", "wb")
    lines = diff.split("\n")
    for line in lines:
        if len(line) > 0:
            first_byte = line[0]
            if first_byte == "+":
                write_file(plus, line)
            elif first_byte == "-":
                write_file(subtraction, line)
            elif first_byte == " ":
                write_file(space, line)


def write_file(file, strings):
    sub_strings = strings[2:]
    ary = sub_strings.split(" ")
    for point in ary:
        if point.isalnum():
            b = bytes.fromhex(point)
            file.write(b)


if __name__ == "__main__":
    main()