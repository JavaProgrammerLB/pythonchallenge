import download_file

from PIL import Image


def main():
    file_name = "zigzag.gif"
    url = "http://www.pythonchallenge.com/pc/hex/{}".format(file_name)
    file_path = "zigzag/{}".format(file_name)
    user = "butter"
    password = "fly"
    # first_step(url, file_path, user, password)
    raw, result = second_step(file_path)
    raw_ary, result_ary = third_step(raw, result)
    fourth_step(raw_ary, result_ary)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    im = Image.open(file_path)
    raw = im.tobytes()
    palette = im.getpalette()[::3]
    index = "".join([chr(i) for i in range(len(palette))])
    value = "".join([chr(palette[i]) for i in range(len(palette))])
    table = str.maketrans(index, value)
    result = raw.decode("latin1").translate(table).encode("latin1")
    return raw, result


def third_step(raw, result):
    raw_ary = []
    result_ary = []
    assert len(raw) == len(result)
    l = len(raw)
    for i in range(l):
        raw_ary.append(raw[i])
        result_ary.append(result[i])
    return raw_ary, result_ary


def fourth_step(raw_ary, result_ary):
    pass


if __name__ == "__main__":
    main()
