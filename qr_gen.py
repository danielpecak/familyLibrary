#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generating QR codes with a certain message

# # # Put one image on the top of another
# https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python
from PIL import Image
import subprocess
import qrcode
import sys
# # # https://medium.com/geekculture/generate-qr-codes-from-images-using-python-60e669653440
# from PIL import Image
# import requests
#
# # im = Image.open(requests.get(img_url, stream=True).raw)
# im = Image.open('owl.png')
# min_width_height = min(im.size)
# im = im.crop(((im.size[0] - min_width_height)/2, (im.size[1] - min_width_height)/2, min_width_height, min_width_height))
# im.save('image_source.png')
#
# im1 = im.resize((186,186), Image.Resampling.LANCZOS)
# im1.save('image_186x186.png')
#
# im2 = im.resize((93,93), Image.Resampling.LANCZOS)
# im2.save('image_93x93.png')




MESSAGE="https://danielpecak.github.io/lib.html#"

# img = qr.make_image(fill_color="white", back_color="black")
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")
for i in range(2):
    qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
    )
    code = MESSAGE+str(i)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    # Load the background template image
    background_image = Image.open("graph/big.png")

    # Create a new white image with 1440x900 dimensions
    # existing_image = img#Image.open("graph/000.png")

    # Calculate the center position for the existing image
    # NOTE BUG for some reason img.width != img.height
    x = (background_image.width  - img.height) // 2 + 20
    y = (background_image.height - img.height) // 2 + 140

    # Paste the existing image onto the new white image at the center position
    background_image.paste(img, (x, y))

    # Save the new image as a PNG file
    # background_image.save("graph/new_wallpaper.png")
    background_image.save('graph/'+str(i).zfill(3)+'.png')
    # img.save('graph/'+str(i).zfill(3)+'.png')






sys.exit()
for i in range(2):
    code = MESSAGE+str(i)
    subprocess.Popen('qr "'+code+'" > graph/'+str(i).zfill(3)+'.png ', shell=True).wait()



def update():
    """
Function goes throug all the books in database and generates new qr codes.
    """
    pass
