import download_file
import bz2


def main():
    url = "http://www.pythonchallenge.com/pc/ring/guido.html"
    file_path = "silent/guido.html"
    user = "repeat"
    password = "switch"
    # first_step(url, file_path, user, password)
    second_step(file_path)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    file = open(file_path, "r")
    count = 0
    result = ""
    while True:
        count += 1
        line = file.readline()
        if line:
            if count >= 13:
                result += chr(len(line) - 1)
        else:
            break
    print("result = " + result)
    dec_result = bz2.decompress(result.encode("latin1"))
    print(dec_result)


if __name__ == "__main__":
    main()
