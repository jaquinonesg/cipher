from django.db import models

import binascii
import json
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class User(models.Model):
    sip_authorization_name = models.CharField(max_length=120)
    sip_authorization_password = models.CharField(max_length=120)

    def cipher(self, message):
        salt = b'\x15?\xab\x9a\xbf\rm\x13k\x10\xbd*|\x0c\x10P\xca\xae@o\x90o\xac\xe4\xbc\x8e\x18Z\xf0<\x04\xf1'
        password = "?)k,,Hy;M^B]5Svh"
        key = PBKDF2(password, salt, dkLen=32)

        cipher = AES.new(key, AES.MODE_CBC)
        binary_message = message.encode('utf-8')
        ciphered_message = cipher.encrypt(pad(binary_message, AES.block_size))
        return  cipher.iv, ciphered_message


    def ciphered_name(self):
        iv, ciphered_data = self.cipher(self.sip_authorization_name)
        return json.dumps({
            'iv': binascii.hexlify(iv).decode('utf-8'),
            'ciphered_data': binascii.hexlify(ciphered_data).decode('utf-8')
        })
    
    def ciphered_password(self):
        iv, ciphered_data = self.cipher(self.sip_authorization_password)
        return json.dumps({
            'iv': binascii.hexlify(iv).decode('utf-8'),
            'ciphered_data': binascii.hexlify(ciphered_data).decode('utf-8')
        })