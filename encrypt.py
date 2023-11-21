import os
import shutil
from cryptography.fernet import Fernet

def split_file(input_file, num_parts):
    file_size = os.path.getsize(input_file)
    part_size = file_size // num_parts

    with open(input_file, 'rb') as f:
        for i in range(num_parts):
            start = i * part_size
            end = min((i + 1) * part_size, file_size)
            f.seek(start)
            part_data = f.read(end - start)

            part_filename = os.path.splitext(input_file)[0] + f'_part{i + 1}.enc'
            with open(part_filename, 'wb') as part_file:
                part_file.write(part_data)

def encrypt_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.enc'):
            key = Fernet.generate_key()
            f = Fernet(key)

            with open(os.path.join(folder, filename), 'rb') as input_file:
                data = input_file.read()
                encrypted_data = f.encrypt(data)

            with open(os.path.join(folder, filename), 'wb') as output_file:
                output_file.write(encrypted_data)

if __name__ == '__main__':
    input_file = 'input.txt'
    num_parts = 4
    folder = os.path.dirname(input_file)

    split_file(input_file, num_parts)
    encrypt_files(folder)
