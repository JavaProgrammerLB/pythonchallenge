import this


def main():
    this_this = first_step()
    hint = "va gur snpr bs jung?"
    second_step(hint, this_this)


def first_step():
    return this.s


def second_step(hint, this_this):
    hint_ary = hint.split(" ")
    len_hint_ary = []
    for element in hint_ary:
        len_hint_ary.append(len(element))
    print(len_hint_ary)

    lines_of_this = str(this_this).split("\n")
    print(lines_of_this)
    len_str_in_line = []
    for line in lines_of_this:
        str_in_line = line.split(" ")
        for str_ele in str_in_line:
            len_str_in_line.append(len(str_ele))
        print(len_str_in_line)
        len_str_in_line = []


if __name__ == "__main__":
    main()
