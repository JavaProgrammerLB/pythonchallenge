from PIL import Image


def main():
    im, width, height = open_a_picture("swan/balloons.jpg")
    get_pixels_rgb(im, 0, 0, 10, 10)
    print()
    get_pixels_rgb(im, int(width / 2), 0, int(width / 2) + 10, 10)


def open_a_picture(dir):
    im = Image.open(dir)
    size = im.size
    width = size[0]
    height = size[1]
    print("balloons'width is {}, balloons'height is {}".format(width, height))
    return im, width, height


def get_pixels_rgb(im, start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            print(im.getpixel((x, y)), end=" ")
        print("")


if __name__ == "__main__":
    main()