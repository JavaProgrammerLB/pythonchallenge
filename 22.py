from PIL import Image, ImageDraw


def main():
    im, width, height = first_step()
    second_step(im, width, height)


def first_step():
    im = Image.open("copper/white.gif")
    size = im.size
    width = size[0]
    height = size[1]
    return im, width, height


def second_step(im, width, height):
    pass


if __name__ == "__main__":
    main()
