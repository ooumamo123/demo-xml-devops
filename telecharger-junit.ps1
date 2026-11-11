# Télécharge le JAR JUnit nécessaire pour la build Ant
New-Item -ItemType Directory -Force -Path lib | Out-Null
Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.10.2/junit-platform-console-standalone-1.10.2.jar" -OutFile "lib/junit-platform-console-standalone-1.10.2.jar"
Write-Host "JUnit téléchargé dans lib/"
