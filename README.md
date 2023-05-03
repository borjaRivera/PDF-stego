# PDF-stego

A Python tool to hide information inside different elements in a PDF. The tool has two options: ENCODE and DECODE.

## Installation 🛠

```bash
sudo apt-get updade
sudo apt-get install python3

git clone https://github.com/borjaRivera/PDF-stego.git

pip install -r requirements.txt

## Usage
```bash
sudo python3 main.py


## Encode
The ENCODE option generates a PDF simulating a Coldplay concert ticket with some information about it, an image and a QR. The application reads the content inside a plaintext file which is wanted to be hidden.
The content must be ciphered before being stored in the PDF, so the program generates a 16 character random key and cipher it using AES-128 and stores the data using LSB in the image of the ticket generated. 
To preserve that random key for future decodings, the application generates a QR which stores it and then, that QR is hidden inside the visible QR in the PDF ticket. 
In order to secure the process of enconding and decoding information, during the decoding option, it is generated a Verification PIN and it is given to the user. That Verification PIN will be requested in the decoding option to get the hidden information.

## Decode
In the DECODE option, user must provide the PDF name which contains the secret encoded on it and then, specify the Verification PIN which was generated during the encoding. If the PIN is correct, the message will be shown to him.

## Authors & Contributors
Borja Rivera González
Alejandro Rivera Horrillo
Mario Villapalos Campeño
Javier Rodrigo Martín

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.


