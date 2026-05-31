import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

plaintext = b"UTS Kriptografi"

# Fernet (Simetris)
key = Fernet.generate_key()
fernet = Fernet(key)

start = time.time()
ciphertext_fernet = fernet.encrypt(plaintext)
fernet_time = time.time() - start

# RSA (Asimetris)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

start = time.time()
ciphertext_rsa = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
rsa_time = time.time() - start

print("=== FERNET ===")
print("Ukuran Ciphertext:", len(ciphertext_fernet))
print("Waktu:", fernet_time)

print("\n=== RSA ===")
print("Ukuran Ciphertext:", len(ciphertext_rsa))
print("Waktu:", rsa_time)
