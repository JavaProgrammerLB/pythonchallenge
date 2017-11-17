from PIL import Image

im = Image.open("smarty/oxygen.png")

start_x = 0
end_x = 608

start_y = 43
end_y = 52
y=50


start_x = 5
end_x = 607
result = chr(115)
# print("0,50 - (115, 115, 115, 255)")
for x in range(start_x, end_x, 7):
    # print("{},{} - {}".format(x, y, im.getpixel((x, y))))
    c = im.getpixel((x, y))[0]
    result += chr(c)

result2 = ""
ary = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in range(len(ary)):
    result2 += chr(ary[i])

print(result)
print(result2)