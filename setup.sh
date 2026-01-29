#!/usr/bin/env bash
echo "Arrete toutes les API en cours"
docker stop $(docker ps -q --filter "ancestor=datascientest/fastapi:1.0.0") 2>/dev/null || true

set -e

echo "Nettoyage ancien environnement..."
docker compose down --remove-orphans || true

echo "Construction des images de tests..."
docker compose build

echo "Lancement des tests..."
docker compose up --abort-on-container-exit | tee log.txt

echo "Nettoyage final..."
docker compose down --remove-orphans >> log.txt

echo "Tests terminés."
echo "Voir log.txt pour les logs généraux."
echo "Voir artifacts/api_test.log pour les résultats détaillés."

