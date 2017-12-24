import requests


def main():
    seed = "http://www.pythonchallenge.com/pc/hex/"
    file_path = "lake/"
    first_step(seed, file_path)


def first_step(seed, file_path):
    for i in range(2, 26):
        url = seed + str(i) + ".wav"
        file_name = file_path + str(i) + ".wav"
        download_a_file(url, file_name)


def download_a_file(url, file_name):
    res = requests.get(url)
    bs = res.content
    file = open(file_name, "wb")
    file.write(bs)
    print("Download {}".format(file_name))


if __name__ == "__main__":
    main()
