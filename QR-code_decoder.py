from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/DELL/Downloads/pyProject/myqrcode.png')

result = decode(img)

print(result)
