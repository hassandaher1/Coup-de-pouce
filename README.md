# Coup de pouce

Site web Django pour une ressourcerie : page publique et espace de gestion des produits.

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Voir le site sur ton téléphone (même réseau Wi‑Fi) :** lance le serveur avec `python manage.py runserver 0.0.0.0:8000`, puis ouvre sur le téléphone `http://<TON_IP>:8000` (ex. `http://192.168.1.10:8000`). Ton IP locale : `ipconfig` (Windows) ou `ifconfig` (Mac/Linux).

Python 3.10+ requis. En production, définir les variables d'environnement (voir `.env.example`).
