import hashlib
import os
import binascii


def generate_salt(length: int = 16) -> str:
    """Generate a random salt as hex string."""
    return binascii.hexlify(os.urandom(length)).decode('utf-8')


def hash_password(password: str, salt: str = None, iterations: int = 600000) -> dict:
    """
    Securely hash a password using PBKDF2-HMAC-SHA256.
    Returns dict with salt, hashed password (hex) and iterations.
    """
    if salt is None:
        salt = generate_salt()
    #Convert password to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    #PBKDF2 with HMAC-SHA256 - 32 bytes output (256 bits)
    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt_bytes,
        iterations,
        dklen=32)
    #Convert to hex for storage
    hashed_hex = binascii.hexlify(derived_key).decode('utf-8')
    return {
        "salt": salt,
        "hashed": hashed_hex,
        "iterations": iterations
    }


def verify_password(password: str, salt: str, hashed: str) -> bool:
    """Verify if password matches the stored hash."""
    # TO DO: re-hash and compare
    return False


def main():
    password = input("Enter password to hash: ").strip()

    result = hash_password(password)
    print(f"\nSalt: {result['salt']}")
    print(f"Hashed: {result['hashed']}")

    # Verification test
    check = input("\nEnter the same password to verify: ").strip()
    if verify_password(check, result['salt'], result['hashed']):
        print("Verification: SUCCESS – password matches")
    else:
        print("Verification: FAILED – password does not match")


if __name__ == "__main__":
    main()