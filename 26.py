import hashlib


def main():
    file_path = "maze/maze/mybroken.zip"
    result_file_path = "maze/maze/my.zip"
    email_md5 = "bbb8b499a0eef99b52c7f13f4e78c24b"
    # first_step(file_path)
    second_step(email_md5, file_path, result_file_path)


def first_step(file_path):
    file = open(file_path, "rb")
    get_bytes_md5(file.read())


def second_step(target, file_path, result_file_path):
    file = open(file_path, "rb")
    bs = file.read()
    finished = False
    for i in range(len(bs)):
        for j in range(256):
            bs_head = bs[: i]
            bs_center = chr(j).encode("latin1")
            bs_tail = bs[i + 1:]
            new_bs = bs_head + bs_center + bs_tail
            now = get_bytes_md5(new_bs)
            if now == target:
                result_file = open(result_file_path, "wb")
                result_file.write(bs)
                print("Done! result={}".format(result_file_path))
                finished = True
                break
        if finished:
            break


def get_bytes_md5(hex_string):
    mymd5 = hashlib.md5()
    mymd5.update(hex_string)
    hexdigest = mymd5.hexdigest()
    return hexdigest


if __name__ == "__main__":
    main()
