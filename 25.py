import requests
import wave
from PIL import Image
from PIL import ImageDraw


def main():
    seed = "http://www.pythonchallenge.com/pc/hex/"
    file_path = "lake/"
    auth = ("butter", "fly")
    # first_step(seed, file_path, auth)
    # bss = second_step()
    # all_pixel = third_step(bss)
    # fourth_step(all_pixel)
    fifth_step()


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


def third_step2(bss):
    result_file = wave.open("lake/result.wav", "wb")
    src_file = wave.open("lake/1.wav", "rb")
    nframes = src_file.getnframes()
    result_file.setnchannels(src_file.getnchannels())
    result_file.setsampwidth(src_file.getsampwidth())
    result_file.setframerate(src_file.getframerate())
    result_file.setnframes(nframes * 25)
    for i in range(len(bss)):
        bs = bss[i]
        result_file.writeframesraw(bs)
    src_file.close()
    result_file.close()
    print("Done")


def third_step(bss):
    all_pixel = []
    for i in range(len(bss)):
        bs = bss[i]
        bs_len = len(bs)
        j = 0
        pixels = []
        while True:
            if j >= bs_len:
                break;
            x = bs[j]
            j += 1
            if j >= bs_len:
                break;
            y = bs[j]
            j += 1
            if j >= bs_len:
                break;
            z = bs[j]
            j += 1
            pixel = (x, y, z)
            pixels.append(pixel)
        all_pixel.append(pixels)
    print(all_pixel)
    return all_pixel


def fourth_step(all_pixel):
    for i in range(len(all_pixel)):
        im = Image.new("RGB", (60, 60))
        drawer = ImageDraw.Draw(im)
        pixels = all_pixel[i]
        count = 0
        for x in range(60):
            for y in range(60):
                print("drawing i={}, count={}, x={}, y={}".format(i, count, x, y))
                drawer.point((x, y), pixels[count])
                count += 1
        im.save("lake/pic/{}.png".format(i))


def fifth_step():
    im = Image.new("RGB", (300, 300))
    for i in range(25):
        x = (i // 5) * 60
        y = (i % 5) * 60
        im_tmp = Image.open("lake/pic/{}.png".format(i))
        im.paste(im_tmp, (x, y))
        print("i={}, x={}, y={}".format(i, x, y))
    im.save("lake/pic/result.png")


if __name__ == "__main__":
    main()
