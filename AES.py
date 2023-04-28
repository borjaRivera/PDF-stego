import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher():
    
    """
    A class for encrypting and decrypting bytes using the AES algorithm in CBC mode.
    """
    def init(key):
        AESCipher.bs = AES.block_size  # AES block size
        AESCipher.key = hashlib.sha256(key.encode()).digest() # The key is derived from the provided key by a hash function

    def encrypt(raw):
        """
        Encrypts the provided bytes using AES CBC mode and returns the encrypted output.
        """
        raw = AESCipher._pad(raw)  # Performs padding of the input string so that it has a length that is a multiple of the AES block size
        iv = Random.new().read(AES.block_size) # Generates a random initialization vector (IV)
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv) # Encrypts the string using AES CBC mode
        return base64.b64encode(iv + cipher.encrypt(raw.encode())) # Encodes the output in base64 and returns the encrypted output

    def decrypt(enc):
        """
        Decrypts the provided bytes using AES CBC mode and returns the decrypted output.
        """
        enc = base64.b64decode(enc) # Decodes the input string from base64
        iv = enc[:AES.block_size]  # Extracts the IV
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv) # Decrypts the string using the same key and AES CBC mode
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8') # Performs padding removal and returns the decrypted string

    def _pad(s):
        """
        Adds padding to the input bytes so that their length is a multiple of the AES block size.
        """
        return s + (AESCipher.bs - len(s) % AESCipher.bs) * chr(AESCipher.bs - len(s) % AESCipher.bs) # Adds padding to the input string

    @staticmethod
    def _unpad(s):
        """
        Removes padding from the output bytes.
        """
        return s[:-ord(s[len(s)-1:])] # Removes padding from the output string
    
if __name__ == '__main__':
    AESCipher.init("12345") 

    cifrado = AESCipher.encrypt("hola")
    print("Cifrado: ", cifrado)

    descifrado = AESCipher.decrypt(cifrado)
    print("Descifrado: ", descifrado)
