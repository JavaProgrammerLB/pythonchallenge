import requests


def download_with_auth(url, file_path, username, password):
    auth = (username, password)
    res = requests.get(url, auth=auth)
    write_file(res, file_path)


def download(url, file_path):
    res = requests.get(url)
    write_file(res, file_path)


def write_file(res, file_path):
    res_content = res.content
    file = open(file_path, "wb")
    file.write(res_content)
    print("Done result={}".format(file_path))
