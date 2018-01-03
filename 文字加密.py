

from Crypto.Cipher import AES
import base64
import os
import sys

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

password = "65fu8ju98jmoin@"
key32 = "{: <32}".format(password).encode("utf-8")
try:
    cipher = AES.new(key32, AES.MODE_ECB)
except:
    print("密码超过32个字符！")
    sys.exit(-1)

print ('密码key32: %s'%key32)
# create a cipher object using the random secret
# cipher = AES.new(key32)

# 把文本加密密文
raw_string='此软件的目的在于将文章内容加密，防止被不良人员阅读！请不要把此工具用于不良企图！仅供研究学习之用！'
print("文本：%s"%raw_string)
byte_str = raw_string.encode("utf-8")
encoded = EncodeAES(cipher, byte_str)
print ('密文: %s' %encoded)

# 密文
# encoded =b'kCCyO9/0zExoOkzA6Ee61JzNDu3V5ehQSrWidqNx4vM4R0dD/iFhEUn6tFlvN0Pxqa/QNAIiESvNFpoPuT00xtI1ffT9Cgd81eK7BaKjJxG1+X6BxhcZ9jMnzyavw3tTq30OWq73y8LHbz0SrxEgK8g2Nwa6dYIlCyh3hFW8kO4LBJuJ8mGfA8WP2JQyUsQw/PvSt4BvCiLNoBkG9Gi1YTyQERlog9oNJY5xi7rFIjS+SBh1PiIqlNcF8KIaEQTcFxw4AHeoUVzKVRpF7HRoQ5/tWSUSc9hR5fRbA7RKmXqlkFaRkUBUo8gCbKmRyQwb1xnNb8+kXZk4UfCt7Rhw+LgUejJLO6xRxA0KxrK7Jb/cI/qARBgx4AuHz5Uon40CaGFPMw/tFW04uBbKqxajyRmTHCiHYTGXuVAZJahCSTcf66bMAoAIU7s95yaz8/pTg+9pCVojuENIE1DYEWR0MfWdf7NJyBQUVXsAsWCMdxi/3NQBBmRxKjmNHUpOpstPmvgrR0qGhuFG2Tb8/s+qw7UGzNpT8NE/A1x9ELX7KyHoiFtM7fh1KHAJi1CF+TL97qZUECW3Ehu2d2rdiQ13bGNKMdNdKgyLF/pXeSXjwax4tPSyKU4XA4eYAmc+3BJo9z8dVG5JVpNm4tuiwz/2nKm/IM+Ib19yVOt1bAW+ajDQhCxT9ZcpwwcRwU5Gxwh/9AhaK+hKKVk1k0ekuKG3tg=='
# 解码密文encoded
decoded = DecodeAES(cipher, encoded)
try:
    text_decoded=decoded.decode("utf-8")
    print ('Decrypted string: %s' %text_decoded)
except:
    print("密码错误！")
    sys.exit(-1)
