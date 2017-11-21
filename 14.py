from PIL import Image
from PIL import ImageDraw

im = Image.open("wire/wire.png")
result = Image.new("RGB", (400, 50), "white")
drawer = ImageDraw.Draw(result)

im_size = im.size
im_x = im_size[0]
im_y = im_size[1]

result_size = result.size
result_x = result_size[0]
result_y = result_size[1]

count = 0
x = 0
y = 0
flag = 1
len = 100
while y < result_y:
    while x < len:
        drawer.point((x, y), im.getpixel((count, 0)))
        print("y is {}, x is {}, count is {}".format(y, x, count))
        x += 1
        count += 1
    if flag %4 == 0:
        y += 1
        x = 0
    if flag % 2 == 1:
        len -= 1
    flag += 1

result.show()

"""
1 100
2 99
3 99
4 98

5 98
6 97
"""
