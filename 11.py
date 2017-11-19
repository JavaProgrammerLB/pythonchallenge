from PIL import Image
from PIL import ImageDraw

im = Image.open("cave/cave.jpg")
size = im.size
width = size[0]
height = size[1]

odd_and_even = Image.new("RGB", [width, height], (0xff, 0xff, 0xff))
drawer = ImageDraw.Draw(odd_and_even)

for x in range(0, width, 2):
    for y in range(0, height, 2):
        drawer.point((x, y), im.getpixel((x, y)))

for x in range(1, width, 2):
    for y in range(1, height, 2):
        drawer.point((x, y), im.getpixel((x, y)))

odd_and_even.show()