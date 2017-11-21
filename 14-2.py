from PIL import Image
from PIL import ImageDraw


im = Image.open("wire/wire.png")
size = im.size
width = size[0]
height = size[1]
count = 0
for x in range(width):
    for y in range(height):
        print(("x:{}, y:{}, : {}").format(x, y, im.getpixel((x, y))))
        count += 1
print(count)
