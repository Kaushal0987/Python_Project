import qrcode

data = 'don\'t forget to do your lab-work'

# img = qrcode.make(data)

# img.save('C:/Users/DELL/Downloads/pyProject/my_qrcode.png')

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')

img.save('C:/Users/DELL/Downloads/pyProject/myqrcode.png')
