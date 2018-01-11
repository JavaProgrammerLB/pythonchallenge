import download_file

from PIL import Image
import bz2
import py2keywords


def main():
    file_name = "zigzag.gif"
    url = "http://www.pythonchallenge.com/pc/hex/{}".format(file_name)
    file_path = "zigzag/{}".format(file_name)
    user = "butter"
    password = "fly"
    # first_step(url, file_path, user, password)
    im, raw, result = second_step(file_path)
    raw_ary, result_ary = third_step(raw, result)
    raw_str, result, index = fourth_step(raw_ary, result_ary)
    hint_path = "zigzag/{}".format("hint.png")
    five_step(im, index, hint_path)
    six_step(raw_str)


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
    return im, raw, result


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
    zero = raw_ary.pop(0)
    raw_ary.append(zero)
    assert len(raw_ary) == len(result_ary)
    raw = []
    result = []
    index = []
    for i in range(len(raw_ary)):
        raw_i = raw_ary[i]
        result_i = result_ary[i]
        if raw_i != result_i:
            raw.append(raw_i)
            result.append(result_i)
            index.append(i)
    raw_str = b""
    for i in range(len(raw)):
        raw_str += chr(raw[i]).encode("latin1")
    return raw_str, result, index


def five_step(im, index, hint_path):
    im2 = Image.new("RGB", im.size)
    colors = [(255, 255, 255)] * (im2.size[0] * im2.size[1])
    for i in index:
        colors[i] = (0, 0, 255)
    im2.putdata(colors)
    im2.save(hint_path)
    print("Hint in {}".format(hint_path))


def six_step(raw_str):
    raw_dec = bz2.decompress(raw_str)
    strs = raw_dec.decode("latin1").split(" ")
    results = set()
    for i in range(len(strs)):
        s = strs[i]
        if not s in py2keywords.kwlist:
            results.add(s)
    print(results)


if __name__ == "__main__":
    main()
