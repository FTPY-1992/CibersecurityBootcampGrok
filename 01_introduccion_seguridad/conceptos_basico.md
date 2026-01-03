# 01 - Introducción a la seguridad informática

## 1. La triada CIA: base de todo concepto de seguridad

La triada CIA es el fundamento absoluto de la seguridad informática. Todo estándar, certificación, ley o framework (ISO 27001, NIST, CIS, etc.) se basa en estos tres pilares.

### Confidencialidad (Confidentiality)

**Definición simple**:
Asegurar que la información solo sea accesible por personas, sistemas o procesos autorizados.
Por qué es importante?
Si la confidencialidad falla, datos sensibles quedan expuestos. 

**Ejemplos reales**:
* Números de tarjetas de crédito robados → fraude masivo.
* Historias clínicas filtradas → extorsión o discriminación.
* Secretos comerciales o militares en manos de competidores → pérdida millonaria o peligro nacional.

**Cómo se protege (controles típicos)**:  
* Cifrado (en reposo y en tránsito): AES, TLS, PGP.
* Controles de acceso: autenticación fuerte (MFA), RBAC (Role-Based Access Control).
* Políticas de clasificación de datos (público, interno, confidencial, restringido).

**Qué pasa si falla**
Brecha de datos → multas (RGPD/Ley de Protección de Datos), pérdida de confianza, daño reputacional irreversible.

**Ejemplo cotidiano**
Tu contraseña de banco: si alguien la ve (porque viaja en texto plano o está mal almacenada), puede vaciar tu cuenta. La confidencialidad evita eso.

### Integridad (Integrity)

**Definición simple**:
Garantizar que la información sea exacta, completa y no haya sido alterada de forma no autorizada (ni intencional ni accidental).
Por qué es importante?
Si la integridad falla, confiás en datos falsos y tomás decisiones erróneas. 

**Ejemplos reales**:

Un atacante modifica el saldo de tu cuenta bancaria de $10.000 a $100.
Se altera un historial médico → te recetan medicación equivocada.
Se modifica código de un avión o central nuclear → catástrofe.

**Cómo se protege**:
* Hashing (SHA-256, SHA-3) para detectar cambios.
* Firmas digitales (para probar autoría y no-repudio).
* Controles de cambio y versionado (Git mismo es un gran ejemplo).
* Checksums y backups verificados.

**Qué pasa si falla**
Pérdida de confianza total en el sistema. En seguridad ofensiva, los ataques de integridad (como MITM o ransomware que modifica archivos) son devastadores.

**Ejemplo cotidiano**
Cuando descargás PyCharm desde JetBrains, verifican el hash SHA-256 del archivo. Si no coincide, sabés que el instalador fue alterado → integridad comprometida.

### Disponibilidad (Availability)

**Definición simple**:
Asegurar que la información y los sistemas estén accesibles y operativos cuando los usuarios autorizados los necesiten.

**Por qué es importante**
Si el sistema no está disponible, el negocio se para. 

**Ejemplos reales**:
* Ataque DDoS a un e-commerce en Black Friday → millones perdidos.
* Ransomware que cifra servidores de un hospital → pacientes en riesgo real.
* Fallo de AWS que tumba Netflix, Spotify, etc. por horas.

**Cómo se protege**
* Redundancia (servidores en múltiples zonas, backups).
* Protección contra DoS/DDoS (WAF, rate limiting, CDN).
* Planes de continuidad y recuperación ante desastres (DRP/BCP).
* Monitoreo y capacidad de escalado.

**Qué pasa si falla**
Pérdida económica directa + daño reputacional. En entornos críticos (salud, energía, defensa) puede costar vidas.

**Ejemplo cotidiano**
Tu conexión a GitHub cae por mantenimiento no anunciado → no podés pushear tu código del bootcamp → disponibilidad comprometida.

## 2. Amenazas y actores maliciosos

### Tipos de amenazas

* **Intencionales**: El atacante quiere hacer daño o ganar algo (robo de datos, extorsión, sabotaje).Ejemplo: ransomware, phishing dirigido.
* **Accidentales**: Nadie quiso que pase, pero pasa (error humano, fallo de configuración).Ejemplo: un empleado borra una base de datos por error o deja una S3 bucket pública en AWS.
* **Internas**: Origen dentro de la organización (empleado, ex-empleado, contratista).Estadística real: ~30-40% de las brechas vienen de adentro.
* **Externas**: Vienen de fuera (hackers, competidores, estados).
* **Activas**: Modifican o destruyen datos/sistemas (ransomware, defacement, MITM).  
* **Pasivas**: Solo observan (sniffing, eavesdropping) sin tocar nada.

### Clasificación de atacantes (threat actors)

* **Script Kiddies**:
Usan herramientas ya hechas (Kali preinstalado, scripts de GitHub) sin entender cómo funcionan.
Motivación: fama, diversión, "porque puedo".
Peligrosidad: baja-media (pero pueden causar daño por suerte).

* **Hacktivistas**:
Atacan por ideología política, social o ambiental (Anonymous, grupos pro/anti algo).
Ejemplo: defacement de sitios gubernamentales, leaks de datos.

* **Cibercriminales organizados**:
Grupos profesionales (muchos en Europa del Este, Nigeria, etc.).
Motivación: dinero puro. Ransomware as a service, carding, BEC (Business Email Compromise).
Peligrosidad: alta.

* **Insider threats**:
Empleados o ex-empleados con acceso legítimo.
Puede ser intencional (venganza, venta de datos) o accidental (phishing exitoso interno).
Muy difíciles de detectar porque ya están "adentro".

* **APT / Nation-State**:
Ataques persistentes avanzados patrocinados por estados (China, Rusia, Corea del Norte, USA, Israel, etc.).
Ejemplos: Stuxnet, SolarWinds, APT29 (Cozy Bear).
Recursos ilimitados, paciencia de años, objetivo: espionaje o sabotaje estratégico.
Peligrosidad: máxima.

## 3. Superficie de ataque y vectores comunes

## 4. Modelo de defensa en profundidad (Defense in Depth)

## 5. Principios básicos de seguridad

- Least privilege
- Fail securely
- Etc.