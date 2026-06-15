# argos-local

Local translation server for Unity games using Argos Translate, FastAPI, and Uvicorn.

---

# Español

## Descripción

**argos-local** instala y ejecuta un servidor local de traducción basado en Argos Translate para ser utilizado con XUnity.AutoTranslator y otros sistemas compatibles.

Todo el procesamiento se realiza localmente, sin depender de servicios externos de traducción.

---

## Requisitos

* Windows 10 o superior
* Conexión a Internet durante la instalación inicial

---

## Instalación

### 1. Descargar Python Embeddable

Ir a:

https://www.python.org/downloads/windows/

En la sección **Stable Releases**, descargar:

**Windows embeddable package (64-bit)**

### 2. Descargar este repositorio

Descargar este repositorio como archivo ZIP.

### 3. Descomprimir archivos

Descomprimir:

* Python Embeddable
* argos-local

### 4. Copiar archivos

Copiar todo el contenido de este repositorio dentro de la carpeta extraída de Python Embeddable.

Ejemplo:

```text
python-embed-amd64/
├── python.exe
├── start.bat
├── requirements.txt
├── app.py
└── ...
```

### 5. Ejecutar

Ejecutar:

```bat
start.bat
```

Durante la primera ejecución se realizará automáticamente:

* Instalación de pip
* Instalación de Argos Translate
* Instalación de FastAPI
* Instalación de Uvicorn
* Descarga del modelo Inglés → Español

Dependiendo de la velocidad de Internet, este proceso puede tardar varios minutos.

---

## Uso

Una vez finalizada la instalación, el servidor quedará disponible en:

```text
http://127.0.0.1:8000/translate
```

### Importante

No cerrar la ventana de consola mientras se esté utilizando el traductor.

---

## Configuración de XUnity.AutoTranslator

Editar el archivo `Config.ini`:

```ini
[Service]
Endpoint=CustomTranslate
FallbackEndpoint=

[Custom]
Url=http://127.0.0.1:8000/translate
EnableShortDelay=False
DisableSpamChecks=True
```

Guardar los cambios y ejecutar el juego normalmente.

---

## Finalizar el servidor

Para detener el servidor:

* Cerrar la ventana de consola.
* O presionar:

```text
Ctrl + C
```

---

## Desinstalación

Para eliminar completamente la instalación:

1. Borrar la carpeta donde se extrajo Python Embeddable.
2. Eliminar la caché descargada por Argos Translate:

```text
C:\Users\{USUARIO}\.local\cache
```

Reemplazar `{USUARIO}` por el nombre de usuario correspondiente de Windows.

---

# English

## Description

**argos-local** installs and runs a local translation server powered by Argos Translate for use with XUnity.AutoTranslator and other compatible applications.

All translations are processed locally without relying on external translation services.

---

## Requirements

* Windows 10 or later
* Internet connection for the initial installation

---

## Installation

### 1. Download Python Embeddable

Go to:

https://www.python.org/downloads/windows/

Under **Stable Releases**, download:

**Windows embeddable package (64-bit)**

### 2. Download this repository

Download this repository as a ZIP file.

### 3. Extract files

Extract:

* Python Embeddable
* argos-local

### 4. Copy files

Copy all files from this repository into the extracted Python Embeddable folder.

Example:

```text
python-embed-amd64/
├── python.exe
├── start.bat
├── requirements.txt
├── app.py
└── ...
```

### 5. Run

Execute:

```bat
start.bat
```

During the first execution, the installer will automatically:

* Install pip
* Install Argos Translate
* Install FastAPI
* Install Uvicorn
* Download the English → Spanish translation model

Depending on your Internet connection, this process may take several minutes.

---

## Usage

After installation is complete, the translation server will be available at:

```text
http://127.0.0.1:8000/translate
```

### Important

Do not close the console window while the translator is being used.

---

## XUnity.AutoTranslator Configuration

Edit the `Config.ini` file:

```ini
[Service]
Endpoint=CustomTranslate
FallbackEndpoint=

[Custom]
Url=http://127.0.0.1:8000/translate
EnableShortDelay=False
DisableSpamChecks=True
```

Save the file and launch the game normally.

---

## Stopping the server

To stop the server:

* Close the console window.
* Or press:

```text
Ctrl + C
```

---

## Uninstallation

To completely remove the installation:

1. Delete the extracted Python Embeddable folder.
2. Delete the Argos Translate cache:

```text
C:\Users\{USERNAME}\.local\cache
```

Replace `{USERNAME}` with your Windows username.
