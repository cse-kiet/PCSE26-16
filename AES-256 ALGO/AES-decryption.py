from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

# === CONFIGURATION ===
# Use a securely generated and stored key. This is just for example.
# This must be the SAME 32-byte key for both encryption and decryption.
KEY_HEX = 'A1B2C3D4E5F67890A1B2C3D4E5F67890A1B2C3D4E5F67890A1B2C3D4E5F67890'
key = bytes.fromhex(KEY_HEX)

# === SIMULATE YOUR API DATA ===
# Instead of making the API call, let's create a sample data structure identical to your output.
# This is the "plaintext" we will encrypt.
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=oi9lfOXrQWH8R8wTWxKDHzGbm2oGhEFJEmGoP0aT'
r = requests.get(url)
data = r.json()

plaintext = json.dumps(data).encode('utf-8')
print("Original Data Prepared for Encryption.\n")

# === ENCRYPTION (Sender's Side) ===
print("=== ENCRYPTING ===")
# Generate a random 16-byte IV
iv = get_random_bytes(16)
# Create a CBC Cipher object
cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
# Encrypt the data (padding is handled automatically)
ciphertext = cipher_encrypt.encrypt(pad(plaintext, AES.block_size))
# The output to send or store is IV + ciphertext
encrypted_data = iv + ciphertext
print(f"IV (hex): {iv.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Full Message (IV + Ciphertext): {encrypted_data.hex()}")
print("Encryption Successful. Ready to transmit.\n")

# === DECRYPTION (Receiver's Side) ===
print("=== DECRYPTING ===")
# This is the crucial part. The receiver gets the 'encrypted_data' variable.
# In a real scenario, this would be received over the network or read from a file.
# ******************************************************************
# YOU MUST HAVE THE 'encrypted_data' VARIABLE FROM THE ENCRYPTION STEP.
# This is the data you were trying to decrypt and the cause of your error.
# ******************************************************************
received_data = encrypted_data  # This line fixes the error!

# Now, we can split the received_data.
received_iv = received_data[:16]        # First 16 bytes are the IV
received_ciphertext = received_data[16:] # The rest is the ciphertext

print(f"Received IV (hex): {received_iv.hex()}")
print(f"Received Ciphertext (hex): {received_ciphertext.hex()}")

# Create a cipher object for decryption
cipher_decrypt = AES.new(key, AES.MODE_CBC, received_iv)
# Decrypt and unpad the data
decrypted_padded_plaintext = cipher_decrypt.decrypt(received_ciphertext)
decrypted_plaintext = unpad(decrypted_padded_plaintext, AES.block_size).decode('utf-8')

# Convert the decrypted string back to a JSON object
decrypted_data = json.loads(decrypted_plaintext)

print("\nDecryption Successful! Decrypted Data:")
print(json.dumps(decrypted_data, indent=4))