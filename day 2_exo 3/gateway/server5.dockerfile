# Utiliser une image Python officielle comme base
FROM python:3.13.0a1-bookworm

RUN mkdir -p home/app

# Définir le répertoire de travail dans le conteneur
WORKDIR /home/app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copier le code source du serveur dans le conteneur
COPY s5.py .

# Define environment variable
#ENV FLASK_APP=server_3_central.py

# Exposer le port sur lequel le serveur s'exécute
EXPOSE 8574

# Commande pour lancer l'application
CMD ["python", "s5.py"]

