# Étape 1 : base image avec Python
FROM python:3.9-slim

# Étape 2 : créer le dossier de travail
WORKDIR /app

# Étape 3 : copier les fichiers nécessaires
COPY . /app

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : exposer le port de l’API
EXPOSE 8000

# Étape 6 : lancer l’API avec Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
