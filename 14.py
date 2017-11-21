from PIL import Image
from PIL import ImageDraw

im = Image.open("wire/wire.png")
result = Image.new("RGB", (100, 100), "white")
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
len_x = result_x
len_y = result_y
while y < len_y:
    while x < len_x:
        # print("x={}, y={}, count={}".format(x, y, count))
        drawer.point((x, y), im.getpixel((count,0)))
        x += 1
        count += 1
    x -= 1
    len_x -= 1
    y += 1
    while y < len_y:
        # print("x={}, y={}, count={}".format(x, y, count))
        drawer.point((x, y), im.getpixel((count,0)))
        y += 1
        count += 1
    y -= 1
    len_y -= 1
    x -= 1
    while x >= result_x - len_x - 1:
        # print("x={}, y={}, count={}".format(x, y, count))
        drawer.point((x, y), im.getpixel((count,0)))
        x -= 1
        count += 1
    x += 1
    y -= 1
    while y >= result_y - len_y:
        # print("x={}, y={}, count={}, result_y={}, len_y={}".format(x, y, count, result_y, len_y))
        drawer.point((x, y), im.getpixel((count,0)))
        y -= 1
        count += 1
    y += 1
    x += 1

result.show()
result.save("wire/cat.png")