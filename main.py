import math

from PIL import Image


def handle_pixel(x, y):
    return im.getpixel((x, y))[3] != 0 if isinstance(im.getpixel((x, y)), tuple) else im.getpixel((x, y)) != 0


while True:
    path_to_file = input("Введите полный путь к файлу (в него же будет сохранен результат): ").replace("\"", "")
    im = Image.open(path_to_file)
    for y in range(im.height):
        if any(handle_pixel(x, y) for x in range(im.width)):
            im = im.crop((0, y, im.width, im.height))
            break
    for y in range(im.height - 1, -1, -1):
        if any(handle_pixel(x, y) for x in range(im.width)):
            im = im.crop((0, 0, im.width, y + 1))
            break
    for x in range(im.width):
        if any(handle_pixel(x, y) for y in range(im.height)):
            im = im.crop((x, 0, im.width, im.height))
            break
    for x in range(im.width - 1, -1, -1):
        if any(handle_pixel(x, y) for y in range(im.height)):
            im = im.crop((0, 0, x + 1, im.height))
            break
    if True:  # доводить до квадрата?
        if im.height > im.width:
            d = (im.height - im.width) / 2
            im = im.crop((-math.floor(d), 0, im.width + math.ceil(d), im.height))
        if im.width > im.height:
            d = (im.width - im.height) / 2
            im = im.crop((0, -math.floor(d), im.width, im.height + math.ceil(d)))
    if False:  # доводить до квадрата 512x512
        if im.width < 512:
            d = (512 - im.width) / 2
            im = im.crop((-math.floor(d), 0, im.width + math.ceil(d), im.height))
        if im.height < 512:
            d = (512 - im.height) / 2
            im = im.crop((0, -math.floor(d), im.width, im.height + math.ceil(d)))
    im.save(path_to_file)
    print("Готово")
