import requests
import wave


def main():
    seed = "http://www.pythonchallenge.com/pc/hex/"
    file_path = "lake/"
    auth = ("butter", "fly")
    # first_step(seed, file_path, auth)
    bs = second_step()
    third_step(bs)


def first_step(seed, file_path, auth):
    for i in range(1, 26):
        url = seed + "lake" + str(i) + ".wav"
        file_name = file_path + str(i) + ".wav"
        download_a_file(url, file_name, auth)


def download_a_file(url, file_name, auth):
    res = requests.get(url, auth=auth)
    bs = res.content
    file = open(file_name, "wb")
    file.write(bs)
    print("Download {}".format(file_name))


def second_step():
    bsAry = []
    for i in range(1, 26):
        lake = wave.open("lake/{}.wav".format(i), "rb")
        bs = lake.readframes(lake.getnframes())
        print(bs)
        bsAry.append(bs)
        lake.close()
    return bsAry


def third_step(bs):
    result_file = wave.open("lake/result.wav", "wb")
    src_file = wave.open("lake/1.wav", "rb")
    nframes = src_file.getnframes()
    result_file.setnchannels(src_file.getnchannels())
    result_file.setsampwidth(src_file.getsampwidth())
    result_file.setframerate(src_file.getframerate())
    result_file.setnframes(nframes * 25)
    for i in range(len(bs)):
        b = bs[i]
        result_file.writeframesraw(b)
    src_file.close()
    result_file.close()
    print("Done")


if __name__ == "__main__":
    main()
