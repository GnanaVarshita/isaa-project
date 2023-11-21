"""import os
from cryptography.fernet import Fernet

def decrypt_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.enc'):
            with open(os.path.join(folder, filename), 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            key = Fernet.generate_key()
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)

            decrypted_filename = os.path.splitext(filename)[0] + '.dec'
            with open(os.path.join(folder, decrypted_filename), 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)

if __name__ == '__main__':
    folder = os.path.dirname('input_part1.enc')

    decrypt_files(folder)
"""

import os

def combine_files(folder, output_filename):
    with open(os.path.join(folder, output_filename), 'wb') as output_file:
        for filename in os.listdir(folder):
            if filename.endswith('.enc'):
                with open(os.path.join(folder, filename), 'rb') as input_file:
                    output_file.write(input_file.read())
if __name__ == '__main__':
    folder = os.path.dirname('input_part1.enc')
    output_filename = 'combined_file.enc'

    combine_files(folder, output_filename)


