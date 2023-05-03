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
In the DECODE option, user must provide the PDF name which contains the secret encoded on it and then, specify the Verification PIN which was generated during the encoding. If the PIN is correct, the message will be shown to him.

## Authors & Contributors
Borja Rivera González,
Alejandro Rivera Horrillo,
Mario Villapalos Campeño,
Javier Rodrigo Martín

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.


