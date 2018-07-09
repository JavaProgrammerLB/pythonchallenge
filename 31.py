from PIL import Image
from PIL import ImageSequence
import numpy as np
import matplotlib.pyplot as plt


def main():
    pic_path = "ufo/mandelbrot.gif"
    # first_step(pic_path)
    # second_step()
    # plt.imshow(mandelbrot(1000, 1000))
    # plt.show()
    numPyVersion()


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
            print(im.getpixel((x, y)), end=" ")
        print()


def second_step():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.dtype)
    print(a.itemsize)
    print(type(a))

    b = np.array([6, 7, 8])
    print(b)
    print(b.shape)
    pass


def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime


def numPyVersion():
    print(np.version.version)


if __name__ == "__main__":
    main()
