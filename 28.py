import download_file

from PIL import Image


def main():
    url = "http://www.pythonchallenge.com/pc/ring/bell.png"
    file_path = "ring/bell.png"
    username = "repeat"
    password = "switch"
    # first_step(url, file_path, username, password)
    second_step(file_path)


def first_step(url, file_path, username, password):
    download_file.download_with_auth(url, file_path, username, password)


def second_step(file_path):
    im = Image.open(file_path)
    green_channel = 1
    green_data = im.getdata(green_channel)
    datas = list(green_data)
    datas_len = len(datas)
    assert datas_len % 2 == 0
    message = ""
    for i in range(int(datas_len / 2)):
        index = 2 * i
        left = datas[index]
        right = datas[index + 1]
        abs_left_min_right = abs(left - right)
        if abs_left_min_right != 42:
            message += chr(abs_left_min_right)
    print(message)


if __name__ == "__main__":
    main()
