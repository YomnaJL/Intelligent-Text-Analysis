# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et les installer
# On le fait en premier pour profiter du cache de Docker si les dépendances ne changent pas
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du code de l'application dans le répertoire de travail
# C'est cette ligne qui copie la nouvelle structure (app.py, services.py, templates/, etc.)
COPY . .

# Exposer le port sur lequel l'application Flask tourne
EXPOSE 5000

# La commande pour lancer l'application quand le conteneur démarre
# Le point d'entrée reste app.py, donc c'est toujours correct
CMD ["python", "app.py"]