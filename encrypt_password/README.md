# Encrypt Password

You'll need to authenticate with your unimelb credentials to use these Mediaflux scripts. You can email ResPlat to get a token if you're concerned about security, or use your unimelb username and password. If you use the latter, I recommend not storing your password as plain-text inside the scripts themselves, in case you accidently share your password. At minimum, store your password in a separate file and keep it safe. If you don't want to store your password as plain-text on your computer, you can also encrypt it using `encrypt_password.py`.


### Instructions

1. Examine script to check it doesn't do anything nefarious. Don't use it if you don't trust it with your unimelb password.

```
% less encrypt_password.py
```

2. Run the script.

```bash
# Here, I'm choosing to store my keys with my ssh keys
% python3 encrypt_password.py ~/.ssh/mf_keys/
Password:
# Then input your password when given the prompt
```

3. Change variables in the Mediaflux scripts to reflect the location of your keys.


### Usage

```
% python3 encrypt_password.py -h
usage: encrypt_password.py [-h] [-f] [output_dir]

Encrypt password

positional arguments:
  output_dir   Output directory (default: ./keys)

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  Force overwrite files
```