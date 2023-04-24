import binascii
import os

from pathlib import Path
from images_extractor import ImagesExtractor
from encode import Encoder
from AES import AESCipher
from qr_generator import QR
from pdf_template import PdfTemplate
from ocultar import TextEncoder


while (1):

    print("[1] Encode")
    print("[2] Decode")
    print("[3] Exit")

    option = input("Choose one of the options above: ")

    if option == "1":

        path = str(Path.cwd()) + '/images/'

        path_coldplay_image = path + 'coldplay_image.png'
        path_coldplay_qr = path + 'coldplay_qr.png'

        #1. Leemos el contenido de un fichero que queremos ocultar
        print("Encoding")

        file_name_to_hide = input("Introduce the file name which content you want to encode: ")
        with open(file_name_to_hide, 'r') as file:
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
        user_key = input("Introduce a key to cipher: ")
        AESCipher.init(user_key)
        random_key_ciphered = AESCipher.encrypt(random_key_str).decode()
        print("Random key ciphered:", random_key_ciphered)

        #5. Metemos la clave cifrada en un QR que generamos
        qr_name_path = path + "qr_random_key_ciphered.png"
        QR.generate_qr(random_key_ciphered, qr_name_path)

        #6. Meter el QR generado dentro del QR que redirecciona a la web de Coldplay


        img_visible_path = path + 'coldplay_qr.png'
        img_hiden_path = qr_name_path 
        output_path = path + 'qr_coldplay_hidden.png'
        Encoder.hide_image(img_visible_path, img_hiden_path, output_path)
        print("Ocultado el QR")

        #7. Ocultar el contenido del fichero en la imagen principal del PDF
        path_coldplay_image_hidden = path + 'coldplay_image_hidden.png'
        TextEncoder.ocultar_texto(ciphered_content, path_coldplay_image, path_coldplay_image_hidden)

        #8. Generamos el PDF con el QR que contiene el otro QR y la imagen donde vamos a ocultar el mensaje principal
        pdf_name = input("Introduce the PDF name to generate: ")
        path_coldplay_image_hidden = path + 'coldplay_image_hidden.png'
        path_qr_coldplay_hidden = path + 'qr_coldplay_hidden.png'
        PdfTemplate.create(pdf_name, path_coldplay_image_hidden, path_qr_coldplay_hidden)

        print("El contenido del archivo que has propocionado se ha ocultado en el PDF creado.")

        # Remove tmp files
        os.remove(path_coldplay_image_hidden)
        os.remove(path_qr_coldplay_hidden)
        os.remove(qr_name_path)

    elif option == "2":
        print("Decoding")


    else:
        exit()











