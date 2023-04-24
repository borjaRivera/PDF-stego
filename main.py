import binascii
import os
#from pdf_template import PdfTemplate
#from images_extractor import ImagesExtractor
from encode import Encoder
from AES import AESCipher
from qr_generator import QR

#PdfTemplate.create()
#ImagesExtractor.extract("invoice.pdf")

while (1):

    print("[1] Encode")
    print("[2] Decode")
    print("[3] Exit")

    option = input("Choose one of the options above: ")

    if option == "1":

        #1. Leemos el contenido de un fichero que queremos ocultar
        print("Encoding")
        with open('test.txt', 'r') as file:
            content = file.read()
        
        #2. Generamos una clave aleatoria
        random_key = os.urandom(16)
        random_key_str = binascii.hexlify(random_key).decode('utf-8')
        print("Random key:", random_key_str)

        #3. Ciframos el contenido del fichero con esa clave aleatoria
        AESCipher.init(random_key_str)
        ciphered_content = AESCipher.encrypt(content).decode()
        print("Ciphered content with key", ciphered_content)

        #4. Ciframos la clave aleatoria con una clave que introduce el usuario
        user_key = input("Introduce a key to cipher:")
        AESCipher.init(user_key)
        random_key_ciphered = AESCipher.encrypt(random_key_str).decode()
        print("Random key ciphered:", random_key_ciphered)

        #5. Metemos la clave cifrada en un QR que generamos
        qr_name = "qr_random_key_ciphered.png"
        QR.generate_qr(random_key_ciphered, qr_name)
        print("Funciona generar el QR")

        #6. Meter el QR generado dentro del QR que redirecciona a la web de Coldplay
        img_visible_path = "./qr_coldplay_5.png"
        img_hiden_path = "./" + qr_name 
        output_path = "qr_coldplay_hidden.png"
        Encoder.hide_image(img_visible_path, img_hiden_path, output_path)

        print("Ocultado el QR")

    

    elif option == "2":
        print("Decoding")


    else:
        exit()











