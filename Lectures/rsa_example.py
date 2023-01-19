import rsa
import base64

if __name__ == '__main__':
    # Generate a new public and private key-pair
    pubkey, privkey = rsa.newkeys(1024)
    # print(pubkey.save_pkcs1().decode('utf-8'))
    # print(privkey.save_pkcs1().decode('utf-8'))
    # pubkey.pem
    # privkey.pem

    # The original message
    message = 'secret message!'

    # Encrypt the text
    crypto_text = rsa.encrypt(bytes(message, 'utf-8'), pubkey)
    # Store encrypted text using base64 encoding to make the text more compact and easier on the eyes
    b64_crypto_text = base64.b64encode(crypto_text).decode('utf-8')

    # Decrypt the text
    # Either decrypt the regular crypto text
    decrypted_message = rsa.decrypt(crypto_text, privkey).decode('utf-8')
    # Or decrypt the base64-coded crypto text
    plain_crypto_text = base64.b64decode(bytes(b64_crypto_text, 'utf-8'))
    decrypted_b64_msg = rsa.decrypt(plain_crypto_text, privkey).decode('utf-8')

    # Print
    print('Encrypted: ', b64_crypto_text)
    print('Decrypted: ', decrypted_b64_msg)
