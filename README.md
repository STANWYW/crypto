# Python Image Steganography with SM4 Encryption

This is a simple steganography tool written in Python that uses the SM4 symmetric key algorithm for encryption and decryption. The program hides text information within an image and can also recover the hidden text from the image.

## Features

- **Hide Text**: Encrypts the input text using SM4 encryption and hides the encrypted text within the least significant bits of an image.
- **Recover Text**: Recovers the encrypted text from the least significant bits of an image and then decrypts it using SM4 decryption.

## Dependencies

- Python 3.6+
- Pillow
- gmssl.sm4 (For SM4 encryption and decryption)

## Usage

1. Run `python main.py` in your terminal.
2. Choose the action you want to perform:
   - If you choose to hide text, you will be prompted to provide the path of the original image, the text to hide, and the path to save the image containing the hidden text.
   - If you choose to recover text, you will be prompted to provide the path of the image containing the hidden text.

Please note that if the image is too small to hide all the text, the program will display an error message.

## Disclaimer

This program uses a simple method of steganography, i.e., the least significant bit method. It makes barely noticeable changes to the image, but it can also be easily detected by a conscious attacker. Therefore, it is not recommended to use this tool to hide sensitive or important information.