import download_file
import read_bin_file

from PIL import Image


def main():
    url = "http://www.pythonchallenge.com/pc/hex/zigzag.jpg"
    file_path = "zigzag/zigzag.jpg"
    user = "butter"
    password = "fly"
    # first_step(url, file_path, user, password)
    # second_step(file_path)
    third_step(file_path)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    ary = read_bin_file.read_bin_file(file_path)
    print(ary)


def third_step(file_path):
    im = Image.open(file_path)
    print(im)
    width, height = im.size


if __name__ == "__main__":
    main()
