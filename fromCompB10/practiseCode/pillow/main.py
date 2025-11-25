from PIL import Image
filename = "images/beach.jpg"
imgfile = Image.open(filename)
# imgfile.show()
# image is being previewed in default image opener app on your os
# opened as png file
# all pillow objects are png file

print(f"{imgfile.width} x {imgfile.height}")
print(f"Total pixels: {imgfile.width * imgfile.height}")

# to crop image from its 1/4 part at last right corner
# imgCropped = imgfile.crop((1600,983,3200,1966))
# imgCropped.show()

# imgResized = imgfile.resize((imgfile.width//4,imgfile.height//4))
# imgResized.show()

imgR, imgG, imgB = image.split()
imgR=imgR.rotate(5)
imgG=imgG.rotate(7)
image=Image.merge("RGB",(imgR, imgG, imgB))