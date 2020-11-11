#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generating QR codes with a certain message

import subprocess
import qrcode

MESSAGE="https://danielpecak.github.io/lib.html#"

for i in range(10):
    code = MESSAGE+str(i)
    subprocess.Popen('qr "'+code+'" > graph/'+str(i).zfill(3)+'.png ', shell=True).wait()





