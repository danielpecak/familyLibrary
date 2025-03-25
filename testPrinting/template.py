#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:08:35 2023
@author: mluerig
"""

#%% imports

import os
import copy
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageOps


#%% setup

## config QR code area
box_size = 16
font_size = 30

## dummy qr code for up to 4 digits to get width/height
text = "9999"
qr = qrcode.QRCode(version=1,box_size=box_size,border=1)
qr.add_data(text)
qr.make(fit=True)
qr_code = qr.make_image(fill='black', back_color='white')
W, H = copy.deepcopy(qr_code.size)
# font = ImageFont.truetype("arial.ttf", font_size)
font = ImageFont.load_default()

## config A4 page
max_idx = 1000
max_width, max_height = 2480, 3508

## start index
idx = 0

#%% run

## loop until max number is reached
while idx < max_idx:

    ## start index for page
    idx_curr = idx + 1

    ## new page
    a4_page = Image.new('RGB', (max_width ,max_height), 'white')

    ## page width/height control
    for i in range(100, max_width, W*2 + 26):
        if i + W*2 + 20 > max_width:
            continue
        for j in range(100, max_height, H + 23):
            if j + H + 20 > max_height:
                continue

            ## index counter
            idx +=1
            text = str(copy.deepcopy(idx))

            ## qr code
            qr = qrcode.QRCode(version=1,box_size=box_size,border=1)
            qr.add_data(text)
            qr.make(fit=True)
            qr_code = qr.make_image(fill='black', back_color='white')

            ## number tag
            tag = Image.new("RGBA", (W, H), "white")
            draw = ImageDraw.Draw(tag)
            _, _, w, h = draw.textbbox((0,0), text=text)
            draw.text(((W-w)/4,(H-h)/2.5), text, font=font, fill="black")

            ## merge
            dst = Image.new('RGB', (qr_code.size[0] + tag.size[1], qr_code.size[0]))
            dst.paste(qr_code, (0, 0))
            dst.paste(tag, (qr_code.size[0], 0))
            dst = ImageOps.expand(dst, border=1, fill=(0,0,0))

            ## add to A4 page
            a4_page.paste(dst, (i,j))

    ## save to pdf
    a4_page.save(r"QR_codes_{}-{}.pdf".format(idx_curr, idx), format='pdf', quality=100)

    ## progress
    print("DONE {}-{}".format(idx_curr, idx))
