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

def simulate_dictionary_attack():
    """Simulate a simple dictionary attack on weak vs secure hashes."""
    print('\n' + '=' * 68)
    print('SIMULACION DE ATAQUE DE DICCIONARIO')
    print('=' * 60)

    dictionary = [
        '123456', 'password', '123456789', '12345', 'qwerty', 'abc123', 'password123', 'admin', 'letmein'
    ]

    # Caso 1: Hash debil(SHA-256 sin salt - como muchos sitios viejos)
    weak_password = 'password123'
    weak_hash = hashlib.sha256(weak_password.encode('utf-8')).hexdigest()
    print(f"\n1. Hash débil (SHA-256 sin salt) de '{weak_password}':")
    print(f"{weak_hash}")

    print('\nAtacante prueba diccionario')
    cracked = False
    for attempt in dictionary:
        if hashlib.sha256(attempt.encode('utf-8')).hexdigest() == weak_hash:
            print(f'CRAKEADO! Contraseña encontrada: {attempt}')
            cracked = True
            break
    if not cracked:
        print('No crakeado con este diccionario pequeño')
    # Caso 2: Nuestro hash SEGURO con salt
    secure_result = hash_password('password123')
    print(f"\n2. Nuestro hash seguro (PBKDF2 + salt) de 'password123':")
    print(f"   Salt: {secure_result['salt']}")
    print(f"   Hashed: {secure_result['hashed']}")

    print(f"\nAtacante prueba el mismo diccionario")
    cracked_secure = False
    for attempt in dictionary:
        test_hash = hash_password(attempt, secure_result['salt'], secure_result['iterations'])
        if test_hash == secure_result['hashed']:
            print(f"CRACKEADO! (improbable con salt unico)")
            cracked_secure = True
            break
        if not cracked_secure:
            print("NO CRACKEADO! el salt hace que cada hash sea unico")
    print("\nConclusión: el salt obliga al atacante a crackear CADA usuario por separado.")
    print("Con 600.000 iterations → millones de veces más lento.")

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