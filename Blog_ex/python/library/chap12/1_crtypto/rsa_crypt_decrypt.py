from Crypto.PublicKey import RSA
from Crypto import Random

public_key_file = open('public.pem', 'r')
private_key_file = open('private.pem', 'r')

public_key = RSA.importKey(public_key_file.read())
private_key = RSA.importKey(private_key_file.read(), passphrase='password')

plain_text = 'ham'
print('원래 문자열:', plain_text)

random_func = Random.new().read
encrypted = public_key.encrypt(plain_text.encode('utf-8'), random_func)
print('암호화된 문자열:', encrypted)

decrypted = private_key.decrypt(encrypted)
print('복호화된 문자열:', decrypted.decode('utf-8'))

public_key_file.close()
private_key_file.close()
