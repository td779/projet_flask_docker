# Utiliser une image Python officielle comme base
FROM python:3.13.0a1-bookworm

RUN mkdir -p home/app

# Définir le répertoire de travail dans le conteneur
WORKDIR /home/app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copier le code source du serveur dans le conteneur
COPY s2.py .


# Define environment variable
#ENV FLASK_APP=server_2_ping.py


# Exposer le port sur lequel le serveur s'exécute
EXPOSE 5372

# Commande pour lancer l'application Flask
CMD ["python", "s2.py"]

