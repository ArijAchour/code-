import smtplib
from email.message import EmailMessage
from mailjet_rest import Client
API_KEY    = "435d6f9bfbaa833bbae14134fde22c6a"
API_SECRET = "6a5b679f12fe9e2b4da5be5a99534c9d"
mailjet = Client(auth=(API_KEY, API_SECRET))

# Seuils prédéfinis pour les métriques du serveur
SEUIL_CPU = 70  # Seuil d'utilisation CPU en pourcentage
SEUIL_RAM = 80  # Seuil d'utilisation de la RAM en pourcentage

# Fonction pour envoyer des alertes par e-mail
def envoyer_alerte_par_email(sujet, corps_message):
    
    data = {
            'Messages': [
                {
                "FromEmail": "hsmztn93@gmail.com",
                "Recipients": [
                    {
                    "Email": "houssem.zitoun@outlook.com"
                    },
                    {
                    "Email": "achourarij1@outlook.fr"
                    }
                ],
                "Subject": sujet,
                "Text-part": corps_message
                }
            ]
        }
    print("# Envoie d'email")
    result = mailjet.send.create(data=data)
    if result.status_code == 200:
        print ("Email d'alerte envoyé avec succées")

# Fonction pour vérifier les seuils et envoyer une alerte si nécessaire
def verifier_seuils_et_envoyer_alertes(usage_cpu, usage_ram):
    # Code pour récupérer les métriques du serveur (CPU, RAM, etc.)
    # Utilisez des bibliothèques appropriées pour obtenir les métriques actuelles

    # Exemple de vérification du seuil CPU
    if usage_cpu > SEUIL_CPU:
        sujet = 'Alerte : Utilisation CPU élevée'
        corps_message = f'L\'utilisation CPU est actuellement à {usage_cpu}%. Veuillez vérifier le serveur.'
        envoyer_alerte_par_email('arijachour87@gmail.com', sujet, corps_message)

    # Exemple de vérification du seuil RAM
    if usage_ram > SEUIL_RAM:
        sujet = 'Alerte : Utilisation de la RAM élevée'
        corps_message = f'L\'utilisation de la RAM est actuellement à {usage_ram}%. Veuillez vérifier le serveur.'
        envoyer_alerte_par_email('arijachour87@gmail.com', sujet, corps_message)