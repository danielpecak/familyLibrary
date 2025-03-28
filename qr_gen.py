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
MESSAGE="https://danielpecak.github.io/lib.html#danielpecak.github.io/lib.html#"

def generateQR(MESSAGE,filename,version=None):
    """
Generates QR code with MESSAGE message and saves it at FILENAME.
    """
    qr = qrcode.QRCode(
    version=version,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=2,
    )
    qr.add_data(MESSAGE)
    qr.make(fit=None)
    img = qr.make_image(fill_color="black", back_color="white")
    # Load the background template image
    background_image = Image.open("graph/big.png")

    # Calculate the center position for the existing image
    # NOTE BUG for some reason img.width != img.height
    x = (background_image.width  - img.height) // 2 + 20
    y = (background_image.height - img.height) // 2 + 140
    # Paste the existing image onto the new white image at the center position
    background_image.paste(img, (x, y))

    # Save the new image as a PNG file
    background_image.save(filename)
    img.save(filename+"_pure")


def testingQRs():
    """
    Generates an array of QR codes with different version
    and with different sizes
    """
    # TODO: version: 10,14,18,22,26,30,34
    # TODO: size [mm]: 9,12,15,18,21,24,27,30
    for ver in [5,6,7,8,9]:
        filename = 'testing2/'+str(ver)+'.pdf'
        print(filename)
        generateQR(MESSAGE,filename,version=ver)
    pass

def onePDFwithQRs():
    """
    Glue together QRs into one pdf file for printing.
    """
    pass

testingQRs()

sys.exit()


def update():
    """
Function goes throug all the books in database and generates new qr codes.
    """
    pass




# img = qr.make_image(fill_color="white", back_color="black")
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")
for i in range(1):
    code = MESSAGE+str(i)
    filename = 'graph/'+str(i).zfill(3)+'.pdf'
    generateQR(code,filename)
