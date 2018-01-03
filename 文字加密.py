

from Crypto.Cipher import AES
import base64
import os
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32
# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length. This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = bytes('{',encoding="utf-8")
# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
# generate a random password(secret) key
# password = os.urandom(BLOCK_SIZE)

password = "abc///."
key32 = "{: <32}".format(password).encode("utf-8")
cipher = AES.new(key32, AES.MODE_ECB)

print ('key32: %s'%key32)
# create a cipher object using the random secret
# cipher = AES.new(key32)

# encode a string
raw_string='成功！'
print("文本：%s"%raw_string)
byte_str = raw_string.encode("utf-8")
encoded = EncodeAES(cipher, byte_str)
print ('Encrypted string: %s' %encoded)

# 加密文本
# encoded =b'GAykDtxAmu683bLPIxcrCi/uXSM+ld+jHnjLr312pGWDZU1cAWuyyk6QiWLkGr7gQxZNQsMnWsoLkMZPw3W81nlOJTUiN/7MsmxPZXabN9x5TiU1Ijf+zLJsT2V2mzfc'
# decode the encoded string
decoded = DecodeAES(cipher, encoded)
try:
    text_decoded=decoded.decode("utf-8")
    print ('Decrypted string: %s' %text_decoded)
except:
    print("密码错误！")

