from PIL import Image
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import sys

# SM4 key must be 16 bytes long
SM4_KEY = b'1234567890123456'

# Convert bytes to a binary string
def bytes_to_bits(bytes_data):
    return ''.join(format(i, '08b') for i in bytes_data)

# Convert a binary string to bytes
def bits_to_bytes(bits):
    return bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

# Encrypt text using SM4
def encrypt_text(text):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(SM4_KEY, SM4_ENCRYPT)
    return crypt_sm4.crypt_ecb(text.encode())

# Decrypt bytes using SM4
def decrypt_bytes(bytes_data):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(SM4_KEY, SM4_DECRYPT)
    return crypt_sm4.crypt_ecb(bytes_data).decode()

# Hide text in a given image
def hide_text(image_path, text, output_path):
    img = Image.open(image_path)
    img_data = img.load()

    encrypted_bytes = encrypt_text(text)
    text_len_bits = format(len(encrypted_bytes), '032b')
    text_bits = text_len_bits + bytes_to_bits(encrypted_bytes)
    text_len = len(text_bits)

    if img.width * img.height * 3 < text_len:
        print("The image is too small to hide this text.")
        return

    idx = 0
    for x in range(img.width):
        for y in range(img.height):
            pixel = list(img_data[x, y])

            for i in range(3):
                if idx < text_len:
                    pixel[i] = (pixel[i] & ~1) | int(text_bits[idx])
                    idx += 1
                else:
                    break

            img_data[x, y] = tuple(pixel)

    img.save(output_path)
    print("The text has been hidden in the image.")

# Recover text from a given image
def recover_text(image_path):
    img = Image.open(image_path)
    img_data = img.load()

    bits = ''
    for x in range(img.width):
        for y in range(img.height):
            pixel = img_data[x, y]

            for i in range(3):
                bits += str(pixel[i] & 1)

    text_len = int(bits[:32], 2)
    bytes_data = bits_to_bytes(bits[32:32 + text_len * 8])
    decrypted_text = decrypt_bytes(bytes_data)
    print("Recovered text:", decrypted_text)

# Main program
def main():
    action = input("Choose an action:\n1 - Hide text in an image\n2 - Recover text from an image\nYour choice: ")
    if action == '1':
        image_path = input("Enter the path of the original image: ")
        text = input("Enter the text to hide: ")
        output_path = input("Enter the path to save the image with hidden text: ")
        hide_text(image_path, text, output_path)
    elif action == '2':
        image_path = input("Enter the path of the image with hidden text: ")
        recover_text(image_path)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == '__main__':
    main()

