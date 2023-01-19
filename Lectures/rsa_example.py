import rsa

if __name__ == '__main__':
    pubkey, privkey = rsa.newkeys(1024)
    # print(pubkey.save_pkcs1().decode('utf-8'))
    # print(privkey.save_pkcs1().decode('utf-8'))
    # pubkey.pem
    # privkey.pem

    message = 'secret message!'
    crypto_text = rsa.encrypt(bytes(message, 'utf-8'), pubkey)
    print('Encrypted: ', crypto_text)
    print('Decrypted: ', rsa.decrypt(crypto_text, privkey).decode('utf-8'))
