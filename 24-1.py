from PIL import Image, ImageDraw
import constant


def main():
    ary = constant.points
    file_path = "maze/maze.png"
    rs = first_step(ary, file_path)
    points_chrs = second_step(rs)
    third_step(points_chrs)


def first_step(ary, file_path):
    maze = Image.open(file_path)
    way = Image.new("RGBA", maze.size, (255, 255, 255, 255))
    way_drawer = ImageDraw.Draw(way)
    rs = []
    for point in ary:
        point_pixel = maze.getpixel((point))
        rs.append(point_pixel[0])
        way_drawer.point(point, point_pixel)
    print(rs)  # PK\x03\x04\x14\
    return rs


def second_step(rs):
    len_rs = len(rs)
    points = []
    for i in range(len_rs):
        if rs[i] == 0:
            # if i % 2 == 0:
            pass
        else:
            points.append(rs[i])
    points_chrs = ""
    for i in range(len(points)):
        points_chrs += chr(points[i])
    # print(points_chrs)
    points_bytes = points_chrs.encode()
    print(points_bytes)
    return points_bytes


def third_step(points_chrs):
    file = open("maze/maze.zip", "wb")
    file.write(points_chrs)
    print("Done")


if __name__ == "__main__":
    main()
