from Cryptodome.Cipher import Blowfish
from Cryptodome.Util.Padding import pad, unpad
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Replace 'your_secret_key' with your own secret key
# additional test
secret_key = b'bitroid'
bf = Blowfish.new(secret_key, Blowfish.MODE_ECB)

def encrypt_password(password: str):
    plaintext = password.encode('utf-8')
    padded_plaintext = pad(plaintext, Blowfish.block_size)
    cipher_text = bf.encrypt(padded_plaintext).hex()
    return {"encrypted_password": cipher_text}
def decrypt_password(encrypted_password: str):
    cipher_text = bytes.fromhex(encrypted_password)
    decrypted_text = bf.decrypt(cipher_text)
    unpadded_text = unpad(decrypted_text, Blowfish.block_size).decode('utf-8')
    return {"decrypted_password": unpadded_text}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a password using Blowfish.')
    subparsers = parser.add_subparsers(dest='command', required=True)
    enc_parser = subparsers.add_parser('encrypt', help='Encrypt a password')
    enc_parser.add_argument('password', type=str, help='The password to encrypt')
    dec_parser = subparsers.add_parser('decrypt', help='Decrypt a password')
    dec_parser.add_argument('encrypted_password', type=str, help='The encrypted password to decrypt')
    args = parser.parse_args()
    if args.command == 'encrypt':
        result = encrypt_password(args.password)
        logger.info(f"Encrypted password: {result['encrypted_password']}")
    if args.command == 'decrypt':
        result = decrypt_password(args.encrypted_password)
        logger.info(f"Decrypted password: {result['decrypted_password']}")