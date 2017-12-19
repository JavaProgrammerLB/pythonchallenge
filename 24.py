from PIL import Image


def main():
    file_path = "maze/maze.png"
    first_step(file_path)


def first_step(file_path):
    im = Image.open(file_path)
    size = im.size
    width = size[0]
    height = size[1]


if __name__ == "__main__":
    main()
