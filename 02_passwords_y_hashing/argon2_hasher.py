from argon2 import PasswordHasher, exceptions


def hash_with_argon2(password: str) -> dict:
    """
    Hash password using Argon2id (recommended 2026 standard).
    Returns dict with params and hash.
    """
    # Configuración recomendada OWASP/NIST 2026
    ph = PasswordHasher(
        time_cost=2,  # iterations (tiempo)
        memory_cost=102400,  # 100 MiB RAM
        parallelism=8,  # threads paralelos
        hash_len=32,  # longitud del hash
        salt_len=16,
        encoding='utf-8'
    )

    hashed = ph.hash(password)

    return {
        "algorithm": "argon2id",
        "params": ph.parameters,  # para debug
        "hashed": hashed
    }


def verify_with_argon2(password: str, hashed: str) -> bool:
    """Verify password against Argon2 hash."""
    ph = PasswordHasher()
    try:
        ph.verify(hashed, password)
        return True
    except exceptions.VerifyMismatchError:
        return False
    except exceptions.InvalidHashError:
        return False


def main_argon2():
    print("=== Argon2id Hasher - 2026 Standard ===\n")

    password = input("Enter password to hash with Argon2id: ").strip()

    result = hash_with_argon2(password)

    print(f"\nAlgorithm: {result['algorithm']}")
    print(f"Hashed (full string): {result['hashed']}")

    print("\n" + "-" * 60)
    check = input("\nEnter password to verify: ").strip()

    if verify_with_argon2(check, result["hashed"]):
        print("\nVerification: SUCCESS – password matches!")
    else:
        print("\nVerification: FAILED – password does not match.")


if __name__ == "__main__":
    main_argon2()