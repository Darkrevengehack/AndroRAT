# Reglas ProGuard específicas del proyecto
# Puedes controlar el conjunto de archivos de configuración aplicados usando
# la configuración proguardFiles en build.gradle

# Para más detalles, ver:
#   http://developer.android.com/guide/developing/tools/proguard.html

# Si tu proyecto usa WebView con JS, descomenta lo siguiente
# y especifica el nombre de clase completo de la interfaz JavaScript:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Descomenta esto para preservar la información de número de línea para
# depuración de stack traces
-keepattributes SourceFile,LineNumberTable

# Si mantienes la información de número de línea, descomenta esto para
# ocultar el nombre del archivo fuente original
-renamesourcefileattribute SourceFile

# Mantener clases de la aplicación
-keep class com.example.reverseshell2.** { *; }

# Mantener clases de AndroidX
-keep class androidx.** { *; }
-keep interface androidx.** { *; }

# Mantener clases nativas
-keepclasseswithmembernames class * {
    native <methods>;
}

# Mantener enums
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}

# Mantener constructores de Parcelable
-keep class * implements android.os.Parcelable {
    public static final android.os.Parcelable$Creator *;
}

# Optimizaciones para Termux
-optimizationpasses 5
-dontusemixedcaseclassnames
-verbose

# Remover logs en release
-assumenosideeffects class android.util.Log {
    public static *** d(...);
    public static *** v(...);
}

# Mantener clases de terceros importantes
-keep class eu.bolt.screenshotty.** { *; }
-keep class org.apache.commons.io.** { *; }
