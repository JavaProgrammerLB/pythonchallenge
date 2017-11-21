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
while y < result_y:
    while x < result_x:
        drawer.point((x, y), im.getpixel((count, 0)))
        print("y is {}, x is {}, count is {}".format(y, x, count))
        x += 1
        count += 1
    if y % 2 == 0:
        result_x -= 1
    y += 1
    x = 0


result.show()