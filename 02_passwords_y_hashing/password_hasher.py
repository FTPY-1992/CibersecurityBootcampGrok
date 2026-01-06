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


def verify_password(password: str, stored:dict) -> bool:
    """Verify if password matches the stored hash."""
    new_hash = hash_password(
        password = password,
        salt = stored["salt"],
        iterations=stored["iterations"]
    )
    return new_hash["hashed"] == stored["hashed"]

def main():
    print("=== Secure Password Hasher - Module 02 ===\n")
    password = input("Enter password to hash: ").strip()

    if not password:
        print("Error: Empty password")
        return

    print("\nHashing with 600000 iterations... (this should take ~0.3-0.5 seconds)")
    result = hash_password(password)
    print(f"\nSalt (hex): {result['salt']}")
    print(f"Hashed password: {result['hashed']}")
    print(f"Iterations: {result['iterations']}")

    print("\n" + "-" * 60)
    # Verification test
    check = input("\nEnter the same password to verify: ").strip()
    if verify_password(check, result):
        print("Verification: SUCCESS – password matches")
    else:
        print("Verification: FAILED – password does not match")


if __name__ == "__main__":
    main()