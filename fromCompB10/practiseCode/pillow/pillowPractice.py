from PIL import Image, ImageFilter, ImageEnhance
filename = "./beach.jpg"
with Image.open(filename) as image:
    image.load()
# img.show()

# img2 = img.crop((200,500,600,600))
# img2 = img.resize((img.width * 2, img.height * 2))
# img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
# img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
# img2 = img.transpose(Image.TRANSPOSE)
# img2 = img.transpose(Image.TRANSVERSE)
# img2 = img.rotate(45)
# img2 = img.rotate(45, expand=True)
# img2 = img.filter(ImageFilter.BLUR)
# img2 = img.filter(ImageFilter.BoxBlur(5))
# img2 = img.filter(ImageFilter.BoxBlur(20))
# img2 = img.filter(ImageFilter.GaussianBlur(5))
# img2 = img.filter(ImageFilter.EMBOSS)
#img2 = img.filter(ImageFilter.FIND_EDGES)
# img2 = img.filter(ImageFilter.EDGE_ENHANCE)

# img2.show()

# newimg = img2.enhance(5)
# newimg.show()

#global image, imageName
xsize = image.width
ysize = image.height
red, green, blue = image.split()
red = red.filter(ImageFilter.GaussianBlur(10))
green = green.filter(ImageFilter.GaussianBlur(5))
green = green.crop((0,0,xsize-5,ysize-5))
red = red.crop((0, 0, xsize - 10, ysize - 10))
green = green.resize((xsize,ysize))
red = red.resize((xsize, ysize))
enh = ImageEnhance.Brightness(green)
green = enh.enhance(2)
enh = ImageEnhance.Brightness(blue)
blue = enh.enhance(3)
enh = ImageEnhance.Brightness(red)
red = enh.enhance(2)
image = Image.merge("RGB", (red, green, blue))
print("You have run Filter B on", filename)
#cls(1)
image.show()

