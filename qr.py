# QR Generator

import pyqrcode
import png
from pyqrcode import QRCode

inp = input('Enter the stuff you want in qrcode: ')  # Ask input form user.

qrCode = pyqrcode.create(inp)  # Generates QRcode.

qrCode.png('myqr.png', scale=8)
