import requests
import binascii
import json
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decipher_data(message, iv):
    salt = b'\x15?\xab\x9a\xbf\rm\x13k\x10\xbd*|\x0c\x10P\xca\xae@o\x90o\xac\xe4\xbc\x8e\x18Z\xf0<\x04\xf1'
    password = "?)k,,Hy;M^B]5Svh"
    key = PBKDF2(password, salt, dkLen=32)
    
    message = binascii.unhexlify(message)
    iv = binascii.unhexlify(iv)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(message), AES.block_size)

    return original

if __name__ == "__main__":
    endpoint = 'http://localhost:8000/api/products/user/2/'
    get_response = requests.get(endpoint)
    data = get_response.json()
    name = json.loads(data['ciphered_name'])
    password = json.loads(data['ciphered_password'])

    decipher_data(name['ciphered_data'], name['iv'])
    decipher_data(password['ciphered_data'], password['iv'])