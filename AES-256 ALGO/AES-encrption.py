from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import json

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=oi9lfOXrQWH8R8wTWxKDHzGbm2oGhEFJEmGoP0aT'
r = requests.get(url)
data = r.json()

# 1. Prepare the Data
plaintext = json.dumps(data).encode('utf-8')

# 2. Generate a random 16-byte IV
iv = get_random_bytes(16)

# 3. Create a CBC Cipher object
key = bytes.fromhex('A1B2C3D4E5F67890A1B2C3D4E5F67890A1B2C3D4E5F67890A1B2C3D4E5F67890') # Your 32-byte key
cipher = AES.new(key, AES.MODE_CBC, iv)

# 4. Encrypt the datas (padding is handled automatically)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# 5. The output to send or store is IV + ciphertext
encrypted_data = iv + ciphertext
print("Encrypted data (hex):", encrypted_data.hex())