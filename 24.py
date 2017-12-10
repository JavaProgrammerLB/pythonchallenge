from PIL import Image, ImageSequence


def main():
    file_path = "maze/maze.png"
    im = first_step(file_path)
    im_size = im.size
    width = im_size[0]  # 641
    height = im_size[1]  # 641
    second_step(im, height)
    start = (639, 0)
    third_step(im, start, width, height)


def first_step(file_path):
    im = Image.open(file_path)
    return im


def second_step(im, height):
    y = 0
    for x in range(height):
        pixel = im.getpixel((x, y))
        if pixel != (255, 255, 255, 255) and pixel != (127, 127, 127, 255):
            print("x={}, y={}, pixel={}".format(x, y, pixel))


def third_step(im, start, width, height):
    x = start[0]
    y = start[1]
    ok_points = [(x, y)]
    one_way(im, start, x, y, ok_points)


def one_way(im, start, x, y, ok_points):
    while True:
        print("ok_points={}".format(ok_points))
        next_points = find_next_point(im, x, y, ok_points)
        print("point=({}, {}),next_point={}".format(x, y, next_points))
        if next_points is None:
            print("break code 1")
            break
        else:
            if len(next_points) == 1:
                x = next_points[0][0]
                y = next_points[0][1]
                ok_points.append((x, y))
            else:
                print("len(next_points)={}".format(len(next_points)))
                print("break code 2")
                break


def find_next_point(im, x, y, ok_points):
    right_x = x + 1
    left_x = x - 1
    up_y = y - 1
    down_y = y + 1
    if right_x > 640:
        right_x_pixel = None
    else:
        right_x_pixel = im.getpixel((right_x, y))
    if left_x < 0:
        left_x_pixel = None
    else:
        left_x_pixel = im.getpixel((left_x, y))
    if up_y < 0:
        up_y_pixel = None
    else:
        up_y_pixel = im.getpixel((x, up_y))
    if down_y > 640:
        down_y_pixel = None
    else:
        down_y_pixel = im.getpixel((x, down_y))
    points = []
    right_point = right_x, y
    left_point = left_x, y
    up_point = x, up_y
    down_point = x, down_y
    if right_x_pixel is not None and right_x_pixel != (255, 255, 255, 255):
        print("right_x={}, y={}, right_x_pixel={}".format(right_x, y, right_x_pixel))
        points.append(right_point)
    if left_x_pixel is not None and left_x_pixel != (255, 255, 255, 255):
        print("left_x={}, y={}, left_x_pixel={}".format(left_x, y, left_x_pixel))
        points.append(left_point)
    if up_y_pixel is not None and up_y_pixel != (255, 255, 255, 255):
        print("x={}, up_y={}, up_y_pixel={}".format(x, up_y, up_y_pixel))
        points.append(up_point)
    if down_y_pixel is not None and down_y_pixel != (255, 255, 255, 255):
        print("x={}, down_y={}, down_y_pixel={}".format(x, down_y, down_y_pixel))
        points.append(down_point)
    print("right_x_pixel={}, left_x_pixel={}, up_y_pixel={}, down_y_pixel={}".format(right_x_pixel, left_x_pixel,
                                                                                     up_y_pixel, down_y_pixel))
    for point in points:
        if point in ok_points:
            points.remove(point)
    if len(points) < 1:
        print("points为None，x={}, y={}".format(x, y))
        return None
    return points


if __name__ == "__main__":
    main()
