import smtplib
from email.message import EmailMessage

# Seuils prédéfinis pour les métriques du serveur
SEUIL_CPU = 90  # Seuil d'utilisation CPU en pourcentage
SEUIL_RAM = 80  # Seuil d'utilisation de la RAM en pourcentage

# Fonction pour envoyer des alertes par e-mail
def envoyer_alerte_par_email(destinataire, sujet, corps_message):
    # Créer un objet EmailMessage
    message = EmailMessage()
    message.set_content(corps_message)
    message['Subject'] = sujet
    message['From'] = 'arijachour87@gmail.com'
    message['To'] = destinataire

    # Établir une connexion au serveur SMTP de votre fournisseur de messagerie
    serveur_smtp = smtplib.SMTP('', 587)
    serveur_smtp.starttls()  # Activer le chiffrement TLS
    serveur_smtp.login('', '')

    # Envoyer l'e-mail
    serveur_smtp.send_message(message)

    # Fermer la connexion au serveur SMTP
    serveur_smtp.quit()

# Fonction pour vérifier les seuils et envoyer une alerte si nécessaire
def verifier_seuils_et_envoyer_alertes(usage_cpu, usage_ram):
    # Code pour récupérer les métriques du serveur (CPU, RAM, etc.)
    # Utilisez des bibliothèques appropriées pour obtenir les métriques actuelles

    # Exemple de vérification du seuil CPU
    if usage_cpu > SEUIL_CPU:
        sujet = 'Alerte : Utilisation CPU élevée'
        corps_message = f'L\'utilisation CPU est actuellement à {usage_cpu}%. Veuillez vérifier le serveur.'
        envoyer_alerte_par_email('destinataire@example.com', sujet, corps_message)

    # Exemple de vérification du seuil RAM
    if usage_ram > SEUIL_RAM:
        sujet = 'Alerte : Utilisation de la RAM élevée'
        corps_message = f'L\'utilisation de la RAM est actuellement à {usage_ram}%. Veuillez vérifier le serveur.'
        envoyer_alerte_par_email('destinataire@example.com', sujet, corps_message)