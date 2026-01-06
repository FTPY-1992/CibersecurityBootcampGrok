# 02 - Passwords y hashing

## 1. Por qué nunca almacenar contraseñas en texto plano

* Si la DB se filtra → atacante tiene todas las contraseñas al instante.
* Reutilización: la gente usa la misma contraseña en 5-10 sitios → una brecha = acceso masivo.
* Ejemplos reales: LinkedIn 2012 (6.5M hashes SHA-1 sin salt → crackeados rápido), Yahoo 2013-2014 (3 mil millones en MD5/ bcrypt mixto).

## 2. Qué es una función de hash y propiedades críticas

Una función hash es un algoritmo que toma un dato de entrada (puede ser cualquier tipo de información, como un archivo, mensaje o contraseña) y lo convierte en un valor de longitud fija, generalmente representado como una cadena de caracteres alfanuméricos. 
Este valor se llama "valor hash" o simplemente "hash".
Lo más importante de una función hash es que cualquier cambio, por pequeño que sea, en los datos de entrada genera un hash completamente diferente. 
Este proceso se hace de forma unidireccional, lo que significa que no puedes reconstruir los datos originales a partir del hash.
**Ejemplo de uso**:
Imagina que tienes la palabra "Hola". Si aplicas una función hash, por ejemplo, SHA-256 (uno de los algoritmos más populares), te generará un valor hash de longitud fija que podría verse algo así:

`2cf24dba5fb0a30e26e83b2ac5b9e29e1b169e4f6c98c3a6d67b273b2760d9c4`

Este valor es único para "Hola". Si cambias la palabra, aunque sea en un solo carácter, el hash cambiará completamente. 
Por ejemplo, si escribes "Holaa", el hash será completamente diferente.

* **Unidireccional**: fácil calcular hash → imposible (prácticamente) revertir a contraseña original.
* **Determinística**: misma entrada → mismo hash.
* **Avalancha**: pequeño cambio en entrada → cambio drástico en hash.
* **Resistencia a colisiones**: difícil encontrar dos entradas con mismo hash.
* **Para contraseñas necesitamos adicionalmente**: ser lenta y costosa (para resistir bruteforce).

## 3. Ataques comunes contra hashes de contraseñas

* **Tablas rainbow**: precomputadas para funciones rápidas sin salt.
* **Ataque de diccionario**: probar palabras comunes, variaciones ("password123").
* **Bruteforce**: probar todas las combinaciones posibles.
* **Ataque offline**: si la DB se filtra, atacante prueba millones de hashes por segundo en GPUs.

## 4. Salt: por qué es obligatorio y cómo funciona

* Valor aleatorio único por usuario.
* Concatenado antes de hashear → mismo contraseña → hashes diferentes.
* Destruye tablas rainbow precomputadas.
* Fuerza al atacante a crackear cada hash individualmente.

## 5. Funciones de hash débiles vs modernas

* MD5, SHA-1: rotas, rápidas → millones de hashes/segundo en GPU.
* SHA-256 puro: seguro criptográficamente, pero demasiado rápido para contraseñas.
* PBKDF2: estándar viejo pero sólido (usado por WPA2, iOS, etc.). Configurable iterations.
* bcrypt: diseñado para contraseñas, cost factor, popular.
* scrypt: memoria-hard (dificulta GPUs).
* Argon2 (2015, ganador Password Hashing Competition): memory-hard + time-hard, recomendado actual (2026) por OWASP, NIST.

## 6. PBKDF2, bcrypt, scrypt, Argon2 – diferencias y recomendaciones actuales (2026)

* Argon2id es el ganador actual.
* Si no disponible → PBKDF2 con ≥600.000 iterations o bcrypt.
* Python: argon2-cffi library (la instalamos después).

## 7. Buenas prácticas reales para almacenamiento de contraseñas

* Salt aleatorio 128+ bits.
* Iterations/cost alto pero tolerable (<500ms en servidor).
* Almacenar: $algorithm$iterations$salt$hash
* Nunca limitar longitud de contraseña.
* Forzar cambio si se filtra.

