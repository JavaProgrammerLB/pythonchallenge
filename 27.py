import download_file

from PIL import Image
from PIL import ImageSequence


def main():
    file_name = "zigzag.gif"
    url = "http://www.pythonchallenge.com/pc/hex/{}".format(file_name)
    file_path = "zigzag/{}".format(file_name)
    user = "butter"
    password = "fly"
    # first_step(url, file_path, user, password)
    second_step(file_path)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    im = Image.open(file_path)
    for frame in ImageSequence.Iterator(im):
        width, height = frame.size
        for x in range(width):
            for y in range(height):
                pixel = frame.getpixel((x, y))
                print(pixel, end=" ")
            print(" ")


if __name__ == "__main__":
    main()
