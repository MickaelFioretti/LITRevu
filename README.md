# LITRevu

P9 - Développez une application Web en utilisant Django

## Installation

### Prérequis

-   Docker
-   Docker-compose

### Installation avec Docker

1. Cloner le projet

```bash
git clone https://github.com/MickaelFioretti/LITRevu.git
```

2. Build les images docker

```bash
docker-compose build
```

3. Lancer les containers

```bash
docker-compose up -d
```

4. Accéder au container

```bash
docker compose exec -it litrevu bash
```

5. Lancer le projet

```bash
python3 manage.py runserver
```

6. Pour la première utilisation
```bash
python3 manage.py tailwind install
```

7. Commandes pour exécuter Tailwind CSS
```bash
python3 manage.py tailwind start
```

## Installation

### Installation sans Docker

1. Cloner le projet

```bash
git clone
```

2. Créer un environnement virtuel

```bash
python -m venv env
```

3. Activer l'environnement virtuel

```bash
source env/bin/activate
```

4. Installer les dépendances

```bash
pip install -r requirements.txt
```

5. Lancer le projet

```bash
python manage.py runserver
```

## Utilisation
