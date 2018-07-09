from PIL import Image
from PIL import ImageSequence


def main():
    pic_path = "ufo/mandelbrot.gif"
    first_step(pic_path)


def first_step(input):
    im = Image.open(input)
    print(im.size)
    counter = 0
    for frame in ImageSequence.Iterator(im):
        counter += 1
    print(counter)
    width = 640
    height = 480
    for x in range(width):
        for y in range(height):
            print(im.getpixel((x, y)), end = " ")
        print()


if __name__ == "__main__":
    main()
