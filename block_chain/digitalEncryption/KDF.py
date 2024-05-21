import hashlib
import os

key = b'13032637048'

"""
加入盐值使用指定的随机函数多次迭代获得密钥
"""
def pdldf2(pwd:str,salt:str=os.urandom(16)):
    return hashlib.pbkdf2_hmac("sha256",pwd.encode(),salt,100000)
import crypto
import sys
sys.modules['Crypto'] = crypto
from crypto.Cipher import Blowfish
from crypto import Random


"""
使用key对称加密生成随机向量，使用8位CBC
"""
def crypt(key, data):
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(data.encode())
    return ciphertext

from ecdsa import SigningKey, SECP256k1, VerifyingKey
from hashlib import sha256
def ecdsa() -> (tuple):
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    message = b"Hello, ECDSA!"
    message_hash = sha256(message).digest()
    signature = private_key.sign(message_hash)
    print("private_key:",private_key.to_string(),"\n")
    print("public_key:",public_key,"\n")
    print("message_hash",message_hash.hex(),"\n")
    print("signature",signature.hex(),"\n")
    assert public_key.verify(signature, message_hash)
    print("签名验证成功!")
    

    
"""
使用key和数据前8位的向量解密
"""
def decrypt(key,data):
    iv = data[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = cipher.decrypt(data[Blowfish.block_size:]).decode()
    return plaintext
if __name__ == '__main__':
    ecdsa()
    
    