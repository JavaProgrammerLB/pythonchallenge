import zlib
import bz2


def main():
    first_step()


def first_step():
    file = open("game/package.pack", "rb")
    bs = file.read()
    result = ""
    while True:
        if bs.startswith(b"x\x9c"):
            bs = zlib.decompress(bs)
            result += " "
        elif bs.startswith(b"BZ"):
            bs = bz2.decompress(bs)
            result += "#"
        elif bs.endswith(b"\x9cx"):
            bs = bs[::-1]
            result += "\n"
        else:
            break
    print(result)


if __name__ == "__main__":
    main()
