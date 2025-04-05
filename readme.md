# 🏗 Eventos del Calendario

Aplicacion simple hecha en Python con el fin de planificar mi dia
en base a las tareas mas proximas en un rango especifico de tiempo
Para quien lo use, asegurarse de tener la API de Google Calendar
funcionando y de tener las credenciales guardadas en su carpeta
_Documentos_.

* Creador: Miguel Soto Delgado (ElMaikina)
* Correo: mikesoto890@gmail.com
* Licencia: GNU General Public License GPLv3

## Requisitos

Para correr la aplicacion es necesario tener la ultima
version de Python 3, ademas de tener instaladas y 
habilitadas las API de Google y las librerias utilizadas
para hacer la creacion del _Markdown_. Para todo esto,
hay que seguir los pasos a continuacion:

### 🐍 1. Instalar librerias y dependencias

* Para instalar las dependencias basta con ejecutar el siguiente comando desde
el directorio que contenga el codigo de este proyecto:

    ```
    pip install -r requirements.txt
    ```

### 🛠️ 2. Crear un proyecto en Google Cloud Console

* Ve a https://console.cloud.google.com/
* Crea un nuevo proyecto (o selecciona uno existente).
* Ve al menú izquierdo → APIs y servicios → Biblioteca.
* Busca Google Calendar API → haz clic → activa la API.

### 🔐 3. Crear credenciales OAuth2

* En el menú de GCP, ve a APIs y servicios → Credenciales.
* Haz clic en + Crear credenciales → ID de cliente de OAuth.
* Si no tienes una pantalla de consentimiento configurada, te pedirá hacerlo:
    * Tipo de usuario: externo (si solo lo usarás tú, es seguro).
    * Rellena nombre de app, email, etc. (puedes poner datos simples).
    * Guarda y vuelve a la creación del ID.
* Tipo de aplicación: Aplicación de escritorio.
* Ponle un nombre (yo le puse _"Calendar"_).
* Dale a Crear.
* Descarga el archivo JSON (haz clic en el ícono de descarga). Renómbralo como:
    ```
    👉 credentials.json
    ```
    y colócalo en el mismo directorio de _Documentos_ de tu usuario actual.

### 💻 4. Ejecuta el script de Python

* Cuando corras por primera vez el script (por ejemplo, python script.py):
* Se abrirá una ventana del navegador para que inicies sesión en tu cuenta de Google.
* Te pedirá permiso para acceder a tu Google Calendar.
* Al aceptar, se generará automáticamente un archivo en tu carpeta de _Documentos_:
    ```
    👉 token.pickle
    ```

## Ejecucion

Basta con estar en el directorio del proyecto y ejecutar
el siguiente comando desde _Powershell_:

```
python main.py
```