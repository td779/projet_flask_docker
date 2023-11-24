#!/bin/bash

# Définir le port de départ
port_base=8080

# Préfixe pour le nom du container
nom_container_base="worker"

# Créer 10 containers généraliste
for i in {1..10}
do
   # Calculer le port pour ce container
   port=$((port_base + i))

   # Générer un nom unique pour le container
   nom_container="${nom_container_base}${i}"

   # Lancer le container avec la variable d'environnement PORT définie et un nom unique
   docker run -d --network spider -p $port:$port --env PORT=$port --name $nom_container worker
done


# Créer 10 containers spécialisés multiplication
for i in {11..20}
do
   # Calculer le port pour ce container
   port=$((port_base + i))

   # Générer un nom unique pour le container
   nom_container="${nom_container_base}${i}"

   # Lancer le container avec la variable d'environnement PORT définie et un nom unique
   docker run -d --network spider -p $port:$port --env PORT=$port --env ADD=false --env MULT=true --name $nom_container worker
done



# Créer 10 containers spécialisés en additions
for i in {21..30}
do
   # Calculer le port pour ce container
   port=$((port_base + i))

   # Générer un nom unique pour le container
   nom_container="${nom_container_base}${i}"

   # Lancer le container avec la variable d'environnement PORT définie et un nom unique
   docker run -d --network spider -p $port:$port --env PORT=$port --env ADD=true --env MULT=false --name $nom_container worker
done