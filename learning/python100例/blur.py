from PIL import Image, ImageFilter

im = Image.open('stuff.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
