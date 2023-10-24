# LITRevu

P9 - Développez une application Web en utilisant Django

## Installation

### Installation avec Docker

### Prérequis

-   Docker
-   Docker-compose

1. Cloner le projet

```bash
git clone https://github.com/MickaelFioretti/LITRevu.git
```

2. Build l'images docker

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

4.1. Accéder au dossier du projet

```bash
cd website
```

5. Faire les migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Lancer le projet

```bash
python3 manage.py runserver
```

7. Pour la première utilisation
```bash
python3 manage.py tailwind install
```

8. Commandes pour exécuter Tailwind CSS
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

4.1. Accéder au dossier du projet

```bash
cd website
```

5. Faire les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Lancer le projet

```bash
python manage.py runserver
```

6. Pour la première utilisation

```bash
python manage.py tailwind install
```

7. Commandes pour exécuter Tailwind CSS

```bash
python manage.py tailwind start
```

## Utilisation

### Superuser

'''text
username: admin
password: inforoot
'''

### Utilisateur

'''text
username: Mickael
password: 8eEhMeRxbJ8jRyd5
'''

'''text
username: Jean
password: xPoY4MBET3s5Kc8C
'''

'''text
username: Paul
password: Gto93qf7RBsy3kB8
'''