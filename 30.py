import download_file
import csv


def main():
    url = "http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv"
    file_path = "relax/yankeedoodle.csv"
    user = "repeat"
    password = "switch"
    # first_step(url, file_path, user, password)
    second_step(file_path)


def first_step(url, file_path, user, password):
    download_file.download_with_auth(url, file_path, user, password)


def second_step(file_path):
    with open(file_path, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(" ".join(row))


if __name__ == "__main__":
    main()
