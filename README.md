# Dev-AI — Django + base de données + application mobile PWA

Cette version transforme le projet Flask fourni en application Django avec :
- authentification par email/mot de passe ;
- connexion Google via django-allauth ;
- inscription placée en **attente d'approbation** ;
- panneau Django Admin pour approuver/refuser les utilisateurs ;
- base de données SQLite en local et PostgreSQL en production ;
- historique des analyses lié à chaque utilisateur ;
- même thème visuel bleu sombre / cyan ;
- interface responsive mobile ;
- PWA installable sur Android/Chrome avec bouton « Installer l'app » ;
- modèle Machine Learning Decision Tree conservé.

## Installation locale

1. Créer un environnement virtuel :
   `python -m venv .venv`

2. Activer sous Windows :
   `.venv\Scripts\activate`

3. Installer :
   `pip install -r requirements.txt`

4. Préparer la base :
   `python manage.py migrate`

5. Créer ton compte administrateur :
   `python manage.py createsuperuser`

6. Lancer :
   `python manage.py runserver`

7. Ouvrir :
   `http://127.0.0.1:8000`

## Approbation des utilisateurs

Va sur :
`http://127.0.0.1:8000/admin/`

Connecte-toi avec ton superutilisateur, puis ouvre **Profiles**.
Sélectionne les utilisateurs et utilise :
- « Approuver les utilisateurs sélectionnés »
- ou « Refuser les utilisateurs sélectionnés ».

Un utilisateur non approuvé reste sur l'écran d'attente.

## Google

Dans Google Cloud Console :
1. Crée un projet.
2. Configure l'écran de consentement OAuth.
3. Crée un identifiant client OAuth de type application Web.
4. Ajoute l'URL de redirection allauth :
   `https://TON-DOMAINE/accounts/google/login/callback/`
5. En local :
   `http://127.0.0.1:8000/accounts/google/login/callback/`
6. Dans Django Admin > Social applications, crée une application Google avec le Client ID et Client Secret, puis associe le site.

Tu peux aussi utiliser les variables d'environnement `GOOGLE_CLIENT_ID` et `GOOGLE_CLIENT_SECRET` si tu adaptes la configuration.

## Déploiement

Le fichier `render.yaml` prépare un déploiement Django + PostgreSQL sur Render.
Le dépôt GitHub peut ensuite être connecté à Render pour obtenir une URL publique.

## Installation mobile

Une fois le site HTTPS en ligne, ouvre `/installation/` depuis Chrome Android.
Le bouton d'installation peut apparaître automatiquement. Sinon :
Menu ⋮ du navigateur > « Installer l'application » / « Ajouter à l'écran d'accueil ».

Important : cette version est une **PWA installable**, pas un APK natif. Elle permet d'avoir une icône d'app sur Android tout en gardant Django comme backend.
