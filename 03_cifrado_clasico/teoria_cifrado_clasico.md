# 03 - Cifrado clásico

## 1. ¿Qué es el cifrado clásico y por qué lo estudiamos?

* Cifrado simétrico manual o mecánico (sin computadoras).
* Usado desde la antigüedad hasta la Segunda Guerra Mundial (Enigma, máquina de cifrado japonesa).
* Lo estudiamos porque: 
  Te enseña los principios básicos: sustitución, transposición, claves.
* Muestra cómo romperlos con técnicas simples → entendés por qué la criptografía moderna es resistente a esos ataques.
* Muchos errores actuales (ej: passwords débiles) repiten patrones clásicos.

## 2. Cifrado César (Shift cipher)

* El más simple: desplaza cada letra del alfabeto por un número fijo (clave = 3, por ejemplo).
  Ejemplo: A → D, B → E, ... Z → C (clave 3).
* Clave: 1 a 25 (26 posibles).
* Fácil de romper: fuerza bruta (prueba las 25 claves) o análisis de frecuencia (la E más común en español/inglés).

## 3. Cifrado de Vigenère (polybius square)

* Polialfabético: usa una clave de varias letras (ej: "LEON").
* Cada letra de la clave desplaza el alfabeto correspondiente (tabla Vigenère).
* Ejemplo: texto "ATAQUE" + clave "LEON" → cifrado "LXLQJ".
* Más fuerte que César porque cambia el desplazamiento.
* Rompible con:
  * Análisis de frecuencia por posición (Kasiski o Friedman).
  * Longitud de clave descubierta → fuerza bruta por subalfabetos.

## 4. Cifrado por sustitución monoalfabética

* Cada letra del alfabeto plano se reemplaza por otra (clave = permutación del alfabeto).
* 26! posibles claves (~4 × 10^26) → imposible fuerza bruta.
* Rompible con análisis de frecuencia (E ~12%, T ~9%, etc.) + patrones (palabras comunes, bigramas).
* Ejemplo real: Edgar Allan Poe usaba estos para cuentos.

## 5. Cifrado por transposición (rail fence, columnar)

* No cambia letras, solo reordena (ej: Rail Fence, Columnar).
* Rail Fence: escribe en "rieles" y lee por filas.
* Columnar: escribe en columnas, lee por orden de clave.
* Rompible con análisis de patrones de longitud y frecuencia.

## 6. Ataques comunes a cifrados clásicos

* Fuerza bruta: probar todas las claves posibles.
* Análisis de frecuencia: letras comunes (E, A, O en español) se mantienen comunes.
* Ataque conocido: texto plano conocido → deducir clave.
* Kasiski/Friedman: encontrar repeticiones para longitud de clave.

## 7. Por qué ya no sirven en la era moderna (lecciones para la criptografía actual)

* Computadoras: fuerza bruta y análisis en segundos.
* Frecuencia y patrones: siguen siendo vulnerables.
* Lección clave: la criptografía moderna debe resistir:
  * Ataques estadisticos
  * Ataques conocidos
  * Fuerza bruta masiva
  * Side-channel (timing,power)

