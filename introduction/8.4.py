# Custom manipulation
from PIL import Image

dave_img = Image.open('dave_2017.jpg')
dave_img.show()
width, height = dave_img.size
for x in range(width):
    for y in range(height):
        pixel_coordinate = (x, y)
        r, g, b = dave_img.getpixel(pixel_coordinate)

        negative_color = (255 - r, 255 - g, 255 - b)
        dave_img.putpixel(pixel_coordinate, negative_color)

dave_img.show()
