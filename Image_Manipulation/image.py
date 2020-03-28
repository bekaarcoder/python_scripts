from PIL import Image, ImageFilter

img = Image.open('./images/daft.jpg')
print(f"Size Before --> {img.size}")

# filtered_img = img.filter(ImageFilter.GaussianBlur)
# filtered_img.save("blur.png", 'png')

# convert_img = img.convert('L')
# convert_img.save("grey.png", 'png')
# convert_img.show()

# to keep aspect ratio
img.thumbnail((250, 250))
img.save('thumbnail.png', 'png')
print(f"Size After --> {img.size}")