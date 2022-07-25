#! /usr/bin/env python3

import argparse
import os.path
import getpass
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description = 'Encrypt password')
parser.add_argument('-f', '--force', action='store_true',
                    help='Force overwrite files')
parser.add_argument('output_dir', nargs='?', default='./keys',
                    help='Output directory (default: ./keys)')
args = parser.parse_args()

# Check if files already exist and quit if so
key_filename = os.path.join(args.output_dir, 'key')
pw_filename = os.path.join(args.output_dir, 'pw')
if not args.force:
    if os.path.isfile(key_filename) or os.path.isfile(pw_filename):
        print('ERROR: keys already exists. Use -f to force overwrite.')
        exit(1)

# Check output directory exists
if not os.path.isdir(args.output_dir) and not os.path.isfile(args.output_dir):
    os.makedirs(args.output_dir)
try:
    assert(os.path.isdir(args.output_dir))
except:
    print('ERROR: Cannot create output directory')
    exit(1)

# Input password
try:
    password = getpass.getpass()
    password_b = str.encode(password)
except Exception as error:
    print('ERROR', error)

# print('Password entered:', password)

# Encrypt password
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(password_b)

# print('Key: ', key)
# print('Encrypted password: ', encrypted)

# Output files
with open(key_filename, 'wb') as f:
    f.write(key)
with open(pw_filename, 'wb') as f:
    f.write(encrypted)

# Change file permissions to user read/write only
os.chmod(key_filename, 0o600)
os.chmod(pw_filename, 0o600)
