import pyqrcode 
import png
from pyqrcode import QRCode

alamatLink = str(input("Masukkan alamat link yang anda inginkan: "))
url = pyqrcode.create(alamatLink)
url.png('myqr.png', scale=8)