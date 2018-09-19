from PIL import Image
from PIL import ImageSequence


def main():
    pic_path = "ufo/mandelbrot.gif"
    first_step(pic_path)


def first_step(input):
    imgbase = Image.open('ufo/mandelbrot.gif')
    img = imgbase.copy()
    left = 0.34
    top = 0.57 + 0.027
    width = 0.036
    height = 0.027
    max = 128
    diff = []
    for j in range(imgbase.size[1]):
        for i in range(imgbase.size[0]):
            point0 = complex(left + i * width / imgbase.size[0], top - (1 + j) * height / imgbase.size[1])
            point = 0 + 0j
            for k in range(max):
                point = point ** 2 + point0
                if point.imag ** 2 + point.real ** 2 > 4:
                    break
            img.putpixel((i, j), k)
            if k != imgbase.getpixel((i, j)):
                diff.append(k - imgbase.getpixel((i, j)))
    img.save('ufo/out31.png')
    img2 = Image.new('1', (23, 73))
    img2.putdata([i < 0 for i in diff])
    img2.save('ufo/out31_2.png')


if __name__ == "__main__":
    main()
