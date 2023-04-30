import qrcode

class QR:
    
    """
    Here we use this function to generate a QR Code from a given text and the name of the file
    """
    def generate_qr(text, name):
        # Crear un objeto QRCode con la información introducida por el usuario
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)

        # Crear una imagen del QR
        imagen_qr = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen del QR en un archivo PNG
        imagen_qr.save(name)

#if __name__ == '__main__':
#	QR.generate_qr("hola me llamo Paco", "test_bisbal.png")