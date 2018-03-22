import download_file
import csv
from PIL import Image
from PIL import ImageDraw


def main():
    url = "http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv"
    file_path = "relax/yankeedoodle.csv"
    pic_path = "relax/hint.png"
    user = "repeat"
    password = "switch"
    # first_step(url, file_path, user, password)
    floats = second_step(file_path)
    points = third_step(floats)
    fourth_step(points, pic_path)
    an = fifth_step(floats)
    sixth_step(an)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    with open(file_path, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        floats = []
        for row in spamreader:
            for i in range(len(row)):
                floatStr = row[i][0:-1]
                floats.append(float(floatStr))
        return floats


def third_step(input):
    points = []
    for i in range(len(input)):
        point = input[i] * 0x100
        points.append(int(point))
    return points


def fourth_step(input, path):
    width = 139
    height = 53
    im = Image.new("P", (width, height))
    drawer = ImageDraw.Draw(im)
    counter = 0
    for x in range(width):
        for y in range(height):
            drawer.point((x, y), input[counter])
            counter += 1
    im.save(path)


def fifth_step(input):
    an = []
    x = "0"
    y = "0"
    z = "0"
    for i in range(len(input)):
        if i % 3 == 0:
            if len(str(input[i])) > 5:
                x = str(input[i])[5]
        elif i % 3 == 1:
            if len(str(input[i])) > 5:
                y = str(input[i])[5]
        elif i % 3 == 2:
            if len(str(input[i])) > 6:
                z = str(input[i])[6]
            an.append(int(x + y + z))
            x = "0"
            y = "0"
            z = "0"
    return an


def sixth_step(input):
    result = ""
    for i in range(len(input)):
        value = chr(input[i])
        result += value
    print(result)


if __name__ == "__main__":
    main()
