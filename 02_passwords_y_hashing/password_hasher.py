import hashlib
import os
import binascii


def generate_salt() -> str:
    """Generate a random salt as hex string."""
    return binascii.hexlify(os.urandom(16)).decode('utf-8')


def hash_password(password: str, salt: str = None) -> dict:
    """
    Hash a password with SHA-256 and a random salt (if not provided).
    Returns a dictionary with salt and hashed password.
    """
    if salt is None:
        salt = generate_salt()

    # TO DO: implement hashing

    return {
        "salt": salt,
        "hashed": "TO DO"
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