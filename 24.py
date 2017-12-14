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
    way = "0"
    max_key = int(way)
    ok_points = [(x, y)]
    ok_points_dic = {way: ok_points}
    one_way(im, x, y, ok_points_dic, max_key)


def one_way(im, x, y, ok_points_dic, max_key):
    while True:
        logging.debug("ok_points_dic={}".format(ok_points_dic))
        keys = ok_points_dic.keys()
        to_be_delete = set()
        to_be_add_dict = dict()
        for way in keys:
            way_ok_points = ok_points_dic.get(way)
            next_points = find_next_point(im, x, y, way_ok_points, way)
            if next_points is None:
                logging.debug("break code 1")
                to_be_delete.add(way)
                logging.debug("add way={} to be delete, because next_points is None".format(way))
                break
            else:
                for point in next_points:
                    max_key += 1
                    to_be_delete.add(way)
                    logging.debug("add way={}to to be delete, because create a new one={}".format(way, max_key))
                    to_be_add_dict[str(max_key)] = way_ok_points
                    x = point[0]
                    y = point[1]
                    new_points = to_be_add_dict.get(str(max_key))
                    new_points.append((x, y))
                    to_be_add_dict[str(max_key)] = new_points
        for key in to_be_add_dict.keys():
            ok_points_dic[key] = to_be_add_dict[key]
        for element in to_be_delete:
            del ok_points_dic[element]


def find_next_point(im, x, y, ok_points, way):
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
    logging.debug("way={}, x={}, y={}, right_x_pixel={}, left_x_pixel={}, up_y_pixel={}, down_y_pixel={}".format(way, x, y, right_x_pixel, left_x_pixel,
                                                                                     up_y_pixel, down_y_pixel))
    for point in points:
        now_index = ok_points.index((x, y))
        before = ok_points[now_index - 1]
        if before == point:
            points.remove(point)
    if len(points) < 1:
        # print("points为None，x={}, y={}".format(x, y))
        return None
    return points


if __name__ == "__main__":
    main()
