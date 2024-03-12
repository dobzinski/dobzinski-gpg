# dobzinski-gpg
Project in Python with Shell Script for crypto and decrypt all files in directories

# GPG Working
```
# gpg2 --generate-key
# gpg2 --list-keys
# gpg2 -a --export PUB-ID > key_pub.asc
```

# How to use

1. Edit the config.ini:
 - Use your Key in "passphrase";
 - Inform those "paths" to cryptograph all files
 - Use the "True" value in "recursive" to cryptograph all subfolders

2. Run to cryptograph all files
```
# python3 crypto.py
```

3. Run to descryptograph all GPG files
```
# python3 decrypt.py
```
