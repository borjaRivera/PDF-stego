import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher():

    def init(key):
        AESCipher.bs = AES.block_size
        AESCipher.key = hashlib.sha256(key.encode()).digest()

    def encrypt(raw):
        raw = AESCipher._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(AESCipher.key, AES.MODE_CBC, iv)
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(s):
        return s + (AESCipher.bs - len(s) % AESCipher.bs) * chr(AESCipher.bs - len(s) % AESCipher.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
    

if __name__ == '__main__':
    key = input("Introduce key: ")
    AESCipher.init(key)

    cifrado = AESCipher.encrypt("hola")
    print("Cifrado: ", cifrado)

    key = input("Introduce key to decode: ")
    AESCipher.init(key)
    descifrado = AESCipher.decrypt(cifrado)
    print("Descifrado: ", descifrado)
