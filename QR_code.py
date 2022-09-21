import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://zelka.org/details.php?id=647906&hit=1'
url = pyqrcode.create(address)
url.png('example_qr.png', scale=8)