import this


def main():
    hint = "va gur snpr bs jung?"
    first_step(hint)
    hint2 = "in the face of what?"
    second_step("va gur snpr bs")


def first_step(hint):
    rot13(hint)


def rot13(s):
    result = ""
    for c in s:
        if c.isalpha():
            ord_c = ord(c)
            ord_c_plus_13 = ord(c) + 13
            if ord_c >= ord("a") and ord_c <= ord("z"):
                if ord_c_plus_13 > ord("z"):
                    c = chr(ord_c_plus_13 - 26)
                else:
                    c = chr(ord_c_plus_13)
            elif ord_c >= ord("A") and ord_c <= ord("Z"):
                if ord_c_plus_13 > ord("Z"):
                    c = chr(ord_c_plus_13 - 26)
                else:
                    c = chr(ord_c_plus_13)
        result += c
    return result


def second_step(hint2):
    this_content = this.s
    lines = this_content.split("\n")
    for line in lines:
        if hint2 in line.lower():
            print(rot13(line))


if __name__ == "__main__":
    main()
