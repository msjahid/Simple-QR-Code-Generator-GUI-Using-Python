import qrcode
from PIL import Image

class QRCode:
    def generate_qr_code(self, data):
        try:
            img = qrcode.make(data)
            img = img.resize((490, 490), Image.ANTIALIAS)
            img.save('qcode.png')
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False