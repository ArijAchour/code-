import argparse
import psutil
import time
from datetime import datetime

# Fonction pour collecter les métriques
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

# Fonction pour journaliser les erreurs
def journaliser_erreur(message):
    # Journaliser l'erreur dans un fichier journal avec horodatage
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('journal.log', 'a') as journal:
        journal.write(f"{timestamp} - Erreur : {message}\n")

# Fonction principale pour collecter et afficher les métriques
def main():
    parser = argparse.ArgumentParser(description="Outil de collecte de métriques de serveur")
    parser.add_argument("--cron", action="store_true", help="Mode d'exécution en tâche cron (silencieux)")
    args = parser.parse_args()
    while True :
        metriques = collecter_metriques()
        if metriques:
            for cle, valeur in metriques.items():
                if args.cron:
                    print(f"{cle}: {valeur}")
                else:
                    print(f"{cle}: {valeur}")
                    print("Métriques collectées avec succès.")

        time.sleep(30)

if __name__ == "__main__":
    main()