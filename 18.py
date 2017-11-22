from PIL import Image
from PIL import ImageDraw
import logging


def load_a_picture(path):
    im = Image.open(path)
    size = im.size
    logging.info("size is {}, mode is: {}".format(size, im.mode))
    return im


def get_pixel_array(im, left_x, right_x, up_y, down_y):
    ary = []
    for x in range(left_x, right_x):
        for y in range(up_y, down_y):
                ary.append(im.getpixel((x, y)))
    return ary


def create_new_ary(ary1, ary2):
    ary = []
    for i in range(len(ary1)):
        r1, g1, b1 = ary1[i]
        r2, g2, b2 = ary2[i]
        r, g, b = r1 - r2, g1 - g2, b1 - b2
        t = (r, g ,b)
        ary.append(t)
    return ary


def analysis_ary(rgbs):
    for i in range(len(rgbs)):
        print(rgbs[i])


def create_new_picture(pixels, width, height):
    result = Image.new(mode="RGB", size=(width, height))
    drawer = ImageDraw.Draw(result)
    count = 0
    for x in range(width):
        for y in range(height):
            drawer.point((x, y), fill = pixels[count])
            count += 1
    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    im = load_a_picture("swan/balloons.jpg")
    size = im.size
    width = size[0]
    height = size[1]
    ary1 = get_pixel_array(im, 0, int(width / 2), 0, height)
    ary2 = get_pixel_array(im, int(width / 2), width, 0 , height)
    logging.info("len(ary1) is: {}".format(len(ary1)))
    logging.info("len(ary2) is: {}".format(len(ary2)))
    ary = create_new_ary(ary1, ary2)
    analysis_ary(ary)
    result = create_new_picture(ary, int(width / 2), height)
    result.show()