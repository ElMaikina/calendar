from datetime import date
import datetime
import time
import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Si modificas este alcance, elimina el archivo token.pickle
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30 * DAY

# Variable que indica los dias en anticipacion a las tareas
DIAS = 14

# Se conecta a los servicios de Google para establecer una conexion
def get_calendar_service():
    creds = None
    if os.path.exists('C:/Users/ElMaikina/Documents/token.pickle'):
        with open('C:/Users/ElMaikina/Documents/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no hay credenciales válidas, solicitar login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
    'C:/Users/ElMaikina/Documents/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('C:/Users/ElMaikina/Documents/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

# Genera el archivo de texto para tener las tareas ordenaditas
def export_events_to_markdown(n_days=7, output_file='eventos.md'):
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    future = (datetime.datetime.utcnow() + datetime.timedelta(days=n_days)).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          timeMax=future, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# 🏗 Eventos del Calendario\n\n")
        f.write(f"Aplicacion simple hecha en Python con el fin de planificar mi dia")
        f.write(f"en base a las tareas mas proximas en un rango especifico de tiempo.")
        f.write(f"Para quien lo use, asegurarse de tener la API de Google Calendar ")
        f.write(f"funcionando y de tener las credenciales guardadas en su carpeta")
        f.write(f" _Documentos_.\n\n")
        f.write(f"* 📆 Fecha actual: {date.today()}\n")
        f.write(f"* 🧮 Tareas en total: {len(events)}\n")
        f.write(f"* ⏳️ Dias de anticipacion: {DIAS}\n")
        f.write(f"## ✔️ Tareas por hacer\n\n")
        f.write(f"Tareas ordenadas por las mas cercanas\n\n")
        if not events:
            f.write("No hay eventos programados.\n")

        f.write(f"| Estado | Nombre | Fecha/s | Tiempo restante | Estado |\n")
        f.write(f"| ---- | ---- | ---- | ---- | ---- |\n")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            summary = event.get('summary', 'Sin título')
            f.write(f"| ❌ | {summary} | {start} | ... | ... |\n")

    print(f"Exportado archivo a: \'{output_file}\'")

# Ejecutar
export_events_to_markdown(n_days=DIAS)
