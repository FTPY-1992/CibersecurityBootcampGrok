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

**Definición clara**
La superficie de ataque (attack surface) es el conjunto total de puntos donde un atacante puede intentar entrar o extraer datos de un sistema.
No es solo código o servidores: incluye hardware, software, red, personas, procesos y hasta proveedores externos.Cuanto más grande la superficie, más oportunidades tiene un atacante.
El objetivo principal de cualquier hardening es reducir la superficie de ataque al mínimo necesario.

**Tipos de superficie de ataque**
* **Digital**: puertos abiertos, servicios expuestos, APIs, sitios web, aplicaciones móviles.
* **Física**: dispositivos sin supervisión (laptops en oficinas, USBs perdidos, servidores en data centers con acceso físico débil).
* **Humana**: empleados, contratistas, proveedores (el famoso “el eslabón más débil”).

**Vectores de ataque comunes (los más explotados en la realidad)**
1. **Phishing / Ingeniería social**
El vector #1 mundial (más del 90% de brechas empiezan acá). Engaña al humano para que entregue credenciales o ejecute malware.
2. **Credenciales débiles o robadas**
Passwords simples, reutilizadas o filtradas en breaches anteriores (HaveIBeenPwned es oro para esto).
3. **Software sin parchear / Vulnerabilidades conocidas**
Ejemplo: Log4Shell (2021) afectó millones de sistemas porque muchos no aplicaron el patch rápido.
4. **Configuraciones incorrectas**
S3 buckets públicos en AWS, bases de datos expuestas en internet (Shodan es el buscador favorito de atacantes para esto), puertos innecesarios abiertos.
5. **Ataques a la cadena de suministro**
Como SolarWinds (2020): comprometen un proveedor confiable y llegan a miles de clientes.
6. **Malware**
Ransomware, troyanos, keyloggers entregados vía email, drive-by download o USB.
7. **Inyecciones y ataques web**
SQL injection, XSS, CSRF – clásicos que veremos en detalle en el módulo 07.

**Cómo reducir la superficie de ataque (principios prácticos)**
* **Principio de menor privilegio (least privilege)**: dar solo los permisos necesarios.
* **Segmentación de red**: firewalls, VLANs, zero trust.
* **Eliminar lo innecesario**: cerrar puertos, deshabilitar servicios no usados, remover software legacy.
* **Patch management riguroso**.
* **Monitoreo y inventory**: saber exactamente qué tenés expuesto (herramientas como Nessus o incluso nmap interno).
* **Educación del usuario final**: porque el humano siempre forma parte de la superficie.

**Ejemplo real y simple**:
Imaginá un servidor web típico.
**Superficie grande**: puerto 80/443 abierto, WordPress con plugins viejos, admin con password “admin123”, backup expuesto en /backup/.
**Superficie reducida**: solo puerto 443 con TLS fuerte, aplicación mínima (sin CMS innecesario), autenticación MFA, backups en almacenamiento offline, monitoreo de logs.

## 4. Modelo de defensa en profundidad (Defense in Depth)

### ¿Qué es?

Es una estrategia de seguridad que parte de una premisa realista: ningún control o capa de protección es perfecta ni infalible.
Por eso, en vez de confiar en una sola barrera “mágica” (como un firewall caro o un antivirus top), se implementan múltiples capas independientes que se complementan y superponen.Si un atacante atraviesa una capa, se encuentra inmediatamente con la siguiente.
El objetivo no es impedir el 100% de los ataques (eso es imposible), sino aumentar tanto el costo y el esfuerzo del atacante que el ataque deje de ser rentable o sea detectado a tiempo.
Metáfora clásica: un castillo medieval  
* Foso → muralla → puertas reforzadas → patio con arqueros → torre del homenaje con bóveda → cofre con cerradura y guardia personal.
Aunque alguien cruce el foso, todavía tiene 5 obstáculos más.

### ¿Por qué una sola capa nunca alcanza?

Razones reales del mundo:
* Todo software tiene bugs y vulnerabilidades (incluso los “mejores” antivirus han tenido zero-days).
* Los humanos cometen errores (click en phishing, password débil, USB perdido).
* Los atacantes son creativos y pacientes (buscan el camino más débil).
* Las amenazas evolucionan más rápido que cualquier producto único (nuevo malware, nuevas técnicas de ingeniería social).

Ejemplo histórico: si Equifax en 2017 hubiera confiado solo en su firewall perimetral, la brecha de 147 millones de personas habría sido igual… pero con Defense in Depth (segmentación, monitoreo, cifrado de datos sensibles) el daño habría sido mucho menor.

### Capas típicas de defensa

(No hay un orden fijo, pero un esquema común es este):
1. **Perímetro**:
Firewall, WAF, protección DDoS, VPN para acceso remoto.
2. **Red interna**:
Segmentación (VLANs, microsegmentación), Zero Trust Network Access, NAC.
3. **Endpoints**:
Antivirus/EDR/XDR, hardening del SO, application control, patch management.
4. **Aplicaciones**:
Secure coding practices, input validation, WAF a nivel app, autenticación fuerte (MFA).
5. **Datos**:
Cifrado en reposo y en tránsito, clasificación de datos, DLP (prevención de fuga).
6. **Factor humano**:
Capacitación continua, simulaciones de phishing, políticas claras, cultura de seguridad.
7. **Seguridad física**:
Control de acceso al data center, cámaras, destrucción segura de discos.
8. **Detección y respuesta**:
SIEM, logging centralizado, threat hunting, equipo de incident response.

### Ejemplo práctico

Imaginá un ataque de ransomware a una empresa mediana:
* El atacante envía un email de phishing a un empleado.
* Capa 1 (humana): el empleado está capacitado y no hace click → ataque detenido.
* Si falla y hace click → Capa 2 (email gateway): filtro anti-phishing lo bloquea.
* Si pasa → Capa 3 (endpoint): EDR detecta el payload y lo pone en cuarentena.
* Si evade → Capa 4 (red): segmentación impide que llegue a servidores críticos.
* Si llega → Capa 5 (acceso): necesita credenciales con MFA que no tiene.
* Si las roba → Capa 6 (datos): los archivos sensibles están cifrados.
* Si cifra algo → Capa 7 (backups): backups offline e inmutables permiten recuperación rápida.
* Todo el tiempo → Capa 8 (monitoreo): SIEM alerta al equipo que responde en minutos.

**Resultado**: aunque varias capas fallen, el ataque no logra su objetivo final. 
Conclusión clave
`“La seguridad no es un producto, sino un proceso continuo”.` 
Defense in Depth no elimina el riesgo, pero lo gestiona de forma realista y escalable.

## 5. Principios básicos de seguridad

- Least privilege
- Fail securely
- Etc.