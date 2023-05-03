# PDF-stego

A Python tool to hide information inside different elements in a PDF. The tool has two options: ENCODE and DECODE. Available on Linux and Windows!

## Installation 🛠

```bash
sudo apt-get updade
sudo apt-get install python3

git clone https://github.com/borjaRivera/PDF-stego.git

cd PDF-stego

pip install -r requirements.txt
```

## Usage
```bash
sudo python3 main.py
```

## Encode
This method basically generates a PDF event ticket where the hidden information is inserted in different elements of it. It is divided into several steps:
1. Reading the information to be hidden: The tool reads the information to be hidden from a file.
2. Generating a random key: A random key is generated, which will be used to encrypt the information to be hidden.
3. Encrypting the information: The tool encrypts the information using the Advanced Encryption Standard (AES) 128 encryption algorithm, which is a symmetric encryption algorithm that uses a 128-bit key to ensure the confidentiality of the information. This key is the random key generated previously
4. Generates a random PIN code of 4 digits for the user in order to Authz.
5. Hiding the encrypted information: The encrypted information is then hidden within the image placed in the body of the event ticket using a LSB method (explained above). 
6. Generating a QR code for the random key: A QR code is generated for the random key,
7. Store the QR code of the random key within the QR code that redirects to the singer's website. This is done to ensure that the key is hidden and can only be accessed by someone who has the QR code.
8. Generates the PDF file that contains the image, the QR code of the website, and the PIN code. In that step a 4-digit PIN code is encoded as blanks within the PDF text (to be more specific inside the table that contains the information related with the event). This ensures that the user who wants to extract the information is authorized to do so and protects against unauthorized access or extraction of the hidden information. If the user enters the wrong PIN code three times, the PDF file will be deleted.



## Decode
This method basically reads a PDF event ticket where the hidden information is inserted in different elements of it and extracts the hidden message. It can be broken down into several steps:
1. Asks the user for the PDF filename that wants to decode
2. Extract the authz PIN code stored in the table of the information related with the event. To do this we read the contents of the PDF document and split it into an array of strings, where each element represents a line of text in the document. Then we access those parts of the array where the blanks are encoded (“Fecha: ”, “Hora: ”, “Lugar: ”, “Precio: ”). It will be used to compare it with the PIN code introduced by the user.
3. Asks the user to introduce the PIN code and provides a limited number of attempts to enter the correct PIN code. Once the correct PIN code is entered, the random key is decrypted and the hidden information is extracted from the PDF file. If the user exceeds the maximum number of attempts to enter the correct PIN code, the PDF file is deleted to protect the hidden information from unauthorized access.
4. Extract the body image and the QR code from the PDF file.
5. Extract hidden QR code ( the one that stores the random key) rom the visible QR code (the ones that redirects to Coldplay’s website)
6. Read the hidden QR code to obtain the random key for the decryption of the information hidden in the image.
7. Extract the hidden content from the body image. First we extract the hidden content from an image file. Specifically, we read an image file and extract the least significant bit (LSB) of the red, green, and blue pixel values for each pixel in the image. These LSB values are then combined to form binary bytes, which are converted to ASCII characters. The extracted ASCII characters are concatenated to form the hidden message that was previously encrypted and hidden within the image file. The code reads the pixels of the image one by one, and stops when it reaches a final character that signals the end of the hidden message. Finally, the decrypted message is returned as a string.
8. Decrypts the content that was hidden in the image. For the decryption we have used AES 128 
9. Show hidden message in console and writes the decrypted content in a file.


## Authors & Contributors
Borja Rivera González,
Alejandro Rivera Horrillo,
Mario Villapalos Campeño,
Javier Rodrigo Martín

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.


