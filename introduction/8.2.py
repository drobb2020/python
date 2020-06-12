from PIL import Image


def resize_images(image_names, new_size=(200, 200)):

    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_"+image_name)


# images = ["giraffe.jpg", "python.jpg", "mice.jpg"]
# resize_images(images)

# Crop
python_img = Image.open("python.jpg")
# python_img.show()
python_img = python_img.crop((622, 630, 1991, 1661))
# python_img = python_img.rotate(90)
python_img.show()
# python_img = python_img.save("cropped_"+python_img)
