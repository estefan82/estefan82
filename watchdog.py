#requirement pip install watchdog

import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. Definir el callback (función que se ejecuta al cambiar el CSV)
def al_cambiar_csv(path):
    print(f"\n[EVENTO] El archivo {path} ha cambiado.")
    try:
        # Leer el archivo actualizado
        df = pd.read_csv(path)
        print("Datos actualizados (primeras 5 filas):")
        print(df.head())
        # Aquí puedes agregar lógica adicional: enviar alertas, procesar, etc.
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

# 2. Definir el manejador de eventos
class HandlerCSV(FileSystemEventHandler):
    def __init__(self, filename, callback):
        self.filename = filename
        self.callback = callback

    def on_modified(self, event):
        # Verificar si el archivo modificado es el nuestro
        if not event.is_directory and event.src_path.endswith(self.filename):
            self.callback(event.src_path)

# 3. Configurar el observador
if __name__ == "__main__":
    path_a_monitorear = "." # Carpeta actual
    archivo_csv = "datos.csv" # Archivo a vigilar
    
    event_handler = HandlerCSV(archivo_csv, al_cambiar_csv)
    observer = Observer()
    observer.schedule(event_handler, path_a_monitorear, recursive=False)
    
    print(f"Monitoreando cambios en: {archivo_csv}...")
    observer.start()
    
    try:
        while True:
            time.sleep(1) # Mantiene el script vivo
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
