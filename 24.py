from PIL import Image
import logging


def main():
    logging.basicConfig(filename="maze/24.log", filemode="w", level=logging.DEBUG,
                        format='%(asctime)s=>%(message)s')
    file_path = "maze/maze.png"
    im = first_step(file_path)
    im_size = im.size
    width = im_size[0]  # 641
    height = im_size[1]  # 641
    # second_step(im, height)
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
    point_ary = [(x, y)]
    way = "0"
    ways = {way: point_ary}
    go_to_end(im, x, y, point_ary, way, ways)


def router(im, points, way, ways):
    logging.info("router start: ways={}".format(ways))
    tmp_way_value = ways[way]
    logging.info("delting way={}".format(way))
    del ways[way]
    for i in range(len(points)):
        point = points[i]
        next_way = str(int(way) + 1 + i)
        logging.info("next_way={}".format(next_way))
        ways[next_way] = tmp_way_value
        x = point[0]
        y = point[1]
        next_point_ary = ways[next_way]
        next_point_ary.append((x, y))
    ways_keys = ways.keys()
    for key in ways_keys:
        now_points = ways[key]
        now_points_tail = now_points[-1]
        x = now_points_tail[0]
        y = now_points_tail[1]
        go_to_end(im, x, y, now_points, key, ways)
    logging.info("router end: ways={}".format(ways))


def go_to_end(im, x, y, point_ary, way, ways):
    logging.info("go_to_end start: ways={}".format(ways))
    points = find_next_point(im, x, y, point_ary)
    if points is None:
        logging.info("delting way={}".format(way))
        del ways[way]
    else:
        len_points = len(points)
        if len_points == 1:
            x = points[0][0]
            y = points[0][1]
            point_ary.append((x, y))
            go_to_end(im, x, y, point_ary, way, ways)
        else:
            router(im, points, way, ways)


def find_next_point(im, x, y, ok_points):
    logging.info("now is ({}, {}) finding next_point".format(x, y))
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
    next_director = {}
    if right_x_pixel is not None and right_x_pixel != (255, 255, 255, 255):
        logging.info("right_x={}, y={}, right_x_pixel={}".format(right_x, y, right_x_pixel))
        points.append(right_point)
    if left_x_pixel is not None and left_x_pixel != (255, 255, 255, 255):
        logging.info("left_x={}, y={}, left_x_pixel={}".format(left_x, y, left_x_pixel))
        points.append(left_point)
    if up_y_pixel is not None and up_y_pixel != (255, 255, 255, 255):
        logging.info("x={}, up_y={}, up_y_pixel={}".format(x, up_y, up_y_pixel))
        points.append(up_point)
    if down_y_pixel is not None and down_y_pixel != (255, 255, 255, 255):
        logging.info("x={}, down_y={}, down_y_pixel={}".format(x, down_y, down_y_pixel))
        points.append(down_point)
    for point in points:
        now_index = ok_points.index((x, y))
        before = ok_points[now_index - 1]
        if before == point:
            logging.info("removing {}".format(point))
            points.remove(point)
    if len(points) < 1:
        logging.info("return None")
        return None
    logging.info("return points={}".format(points))
    return points


if __name__ == "__main__":
    main()
