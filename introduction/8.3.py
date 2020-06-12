
from PIL import Image, ImageFilter, ImageEnhance

mice_img = Image.open('mice.jpg')

grayscale = mice_img.convert('L')
grayscale.show()

edge_detect = mice_img.filter(ImageFilter.FIND_EDGES)
edge_detect.show()

contrast = ImageEnhance.Contrast(mice_img).enhance(1.5)
contrast.show()

bright = ImageEnhance.Brightness(contrast).enhance(2)
bright.show()
