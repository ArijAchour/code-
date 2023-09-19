
import psutil
import logging
import datetime

# Configuration de la journalisation
logging.basicConfig(filename='journal.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def collecter_metriques():
    try:
        # Collecter les métriques CPU, mémoire et espace disque
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Retourner les métriques sous forme de dictionnaire
        return {
            'Utilisation du CPU (%)': cpu_usage,
            'Mémoire totale (Go)': round(memory.total / (1024 ** 3), 2),
            'Mémoire utilisée (Go)': round(memory.used / (1024 ** 3), 2),
            'Espace disque total (Go)': round(disk.total / (1024 ** 3), 2),
            'Espace disque utilisé (Go)': round(disk.used / (1024 ** 3), 2) 
                }
    except Exception as e:
        # En cas d'erreur, journaliser l'erreur
        journaliser_erreur(str(e))
        return None
    def journaliser_erreur(message):
    # Journaliser l'erreur dans un fichier journal avec horodatage
     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('journal.log', 'a') as journal:
        journal.write(f"{timestamp} - Erreur : {message}\n")

if __name__ == "__main__":
    # Collecter les métriques
    metriques = collecter_metriques()
    if metriques:
        for cle, valeur in metriques.items():
            print(f"{cle}: {valeur}")
