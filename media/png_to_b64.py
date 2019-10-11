"""
Purpose:     Convert PNG image to b64 string for shields.io custom logos
             ?logo=data:image/png;base64,<ENCODED_IMAGE_STRING>
"""


import base64
import sys

filename = sys.argv[1]
with open(filename, "rb") as encode_me:
    b64str = base64.b64encode(encode_me.read())

print(b64str)
