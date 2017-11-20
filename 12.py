all = open("evil/evil2.gfx", "rb")
content = all.read()
all.close()

for i in range(5):
    file = open("evil/{}.jpg".format(i), "wb")
    file.write(content[i::5])
    file.close()