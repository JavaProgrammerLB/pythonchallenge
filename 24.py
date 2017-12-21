from PIL import Image
import logging
import logging.handlers


class Way:
    def __init__(self, pasts):
        self.pasts = pasts


def main():
    file_path = "maze/maze.png"
    logger = set_logger()
    points_pixels, width, height = first_step(file_path)
    # second_step(points_pixels, height)
    start = (639, 0)
    # third_step(start, points_pixels, logger)


def set_logger():
    log_file_path = "maze/log/mylog.log"
    handler = logging.handlers.RotatingFileHandler(log_file_path, maxBytes=1024 * 1024, backupCount=10000)
    fmt = "%(asctime)s=>%(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger("maze/log/mylog")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


def first_step(file_path):
    im = Image.open(file_path)
    size = im.size
    width = size[0]
    height = size[1]
    points_pixels = {}
    for x in range(width):
        for y in range(height):
            points_pixels[("{}_{}".format(x, y))] = im.getpixel((x, y))
    return points_pixels, width, height


def second_step(points_pixels, height):
    y = 0
    for x in range(height):
        pixel = points_pixels["{}_{}".format(x, y)]
        if pixel != (255, 255, 255, 255) and pixel != (127, 127, 127, 255):
            print("x={}, y={}, pixel={}".format(x, y, pixel))


def third_step(start, points_pixels, logger):
    x = start[0]
    y = start[1]
    pasts = [(x, y)]
    ways = []
    way = Way(pasts)
    ways.append(way)
    while True:
        if len(ways) == 0:
            break
        else:
            now_way = ways[-1]
            now_way_pasts = now_way.pasts
            print("len(ways)={}, now_ways_pasts={}".format(len(ways), now_way_pasts))
            if len(ways) == 1:
                logger.info("now_ways_pasts={}".format(now_way_pasts))
            x = now_way_pasts[-1][0]
            y = now_way_pasts[-1][1]
            if y > 638:
                logger.info("now_way={}, now_way's pasts={}".format(now_way, now_way.pasts))
                if y == 640:
                    break
            points = find_next_point(points_pixels, x, y, now_way_pasts, logger)
            if points is None:
                ways.remove(now_way)
            else:
                len_points = len(points)
                if len_points == 1:
                    next_point = points[0]
                    next_point_x = next_point[0]
                    next_point_y = next_point[1]
                    now_way_pasts.append((next_point_x, next_point_y))
                elif len_points > 1:
                    for point in points:
                        new_way = Way([])
                        new_way_pasts = new_way.pasts
                        new_way_pasts.extend(now_way_pasts)
                        new_way_pasts.append(point)
                        ways.append(new_way)
                    ways.remove(now_way)


def find_next_point(points_pixels, x, y, past, logger):
    right_x = x + 1
    left_x = x - 1
    up_y = y - 1
    down_y = y + 1
    if right_x > 640:
        right_x_pixel = None
    else:
        right_x_pixel = get_pixel(right_x, y, points_pixels)
    if left_x < 0:
        left_x_pixel = None
    else:
        left_x_pixel = get_pixel(left_x, y, points_pixels)
    if up_y < 0:
        up_y_pixel = None
    else:
        up_y_pixel = get_pixel(x, up_y, points_pixels)
    if down_y > 640:
        down_y_pixel = None
    else:
        down_y_pixel = get_pixel(x, down_y, points_pixels)
    points = []
    right_point = right_x, y
    left_point = left_x, y
    up_point = x, up_y
    down_point = x, down_y
    if right_x_pixel is not None and right_x_pixel != (255, 255, 255, 255):
        points.append(right_point)
    if left_x_pixel is not None and left_x_pixel != (255, 255, 255, 255):
        points.append(left_point)
    if up_y_pixel is not None and up_y_pixel != (255, 255, 255, 255):
        points.append(up_point)
    if down_y_pixel is not None and down_y_pixel != (255, 255, 255, 255):
        points.append(down_point)
    for point in points:
        now_index = past.index((x, y))
        before = past[now_index - 1]
        if before == point:
            points.remove(point)
    if len(points) < 1:
        return None
    return points


def get_pixel(x, y, points_pixels):
    return points_pixels["{}_{}".format(x, y)]


if __name__ == "__main__":
    main()
