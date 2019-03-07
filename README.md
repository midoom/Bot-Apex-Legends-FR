# Si vous voulez juste utiliser mon bot sur votre serveur
* Créez un canal appelé "vos-level" (sans guillemets). Mon bot n'acceptent que les commandes envoyées dans ce canal, les commandes des autres canaux seront supprimées automatiquement.
* Il est préférable de créer des rôles pour 10 niveaux, comme ça la commande ?lvl fonctionnera aussi sur votre serveur. (Exemple de noms de rôles : "0-10", "10-20", "20-30",..., "90-100")
* ?ajuda pour tout savoir sur le bot (dans "vos-level")
* Ajouter un bot au serveur (https://discordapp.com/oauth2/authorize?client_id=551427536115073026&scope=bot&permissions=8)

# Pour modifier le bot :

## Pré-requis :
* Télécharger Python 3 sur votre ordinateur (https://www.python.org/downloads/)
* Ouvrer une invite de commande en tant qu'administrateur (cmd) et copier/coller "python3 -m pip install -U discord.py" après l'installation copier/coller "python3 -m pip install -U discord.py[voice]"
## Etape par étape :
* Aller sur [Apex API](https://apex.tracker.gg/site-api) et suiver la peocédure pour récupérer votre API
* Creér une app Discord [Discord Developers](https://discordapp.com/login?redirect_to=%2Fdevelopers%2Fapplications%2F), créer un bot à votre app et récupérer le token.
* Une fois les deux clés récupéré, allez les mettre dans main.py à leur emplacement.
* Configurer le bot à l'aide du fichier main.py (des aides/commentaires sont fournis dans le fihcier pour vous aidez)
* C'est tout.

## Hébergez le bot sur Heroku
Si vous souhaitez héberger votre bot 24/7 sur Heroku, j'ai fourni les fichiers nécessaires (main.py, requirements.txt, Procfile), tout ce que vous avez à faire est :
* Importer votre "repository" dans GitHub 
* Allez sur Heroku, créer une app, connectez-vous avec Github, et en projet mettez [Nom d'utilisateur]/[Nom du repository], valider.
* Aller dans les paramètres et ajouter un buildpack (heroku/python)
* Aller dans "Overview", cliquer sur "Configure Dynos", cliquer sur le crayon et activer le dynos.
* Retourner sur "Deploy" et déployer la branche manuellement
* C'est tout.

## Commandes :
* ?lvl PLATFORM PSEUDO: Cherche le pseudo Origin, vérifiez son niveau sur Apex, et ajoute le rôle à l'auteur du message avec le rôle correspondant.
* ?clvl PSEUDO NICKNAME: Cherche le pseudo Origin, vérifier son niveau sur Apex indique le niveau mais ne fait pas d'autorole.
* ?kills PSEUDO NICKNAME: Cherche le pseudo Origin, vérifie son nombre de morts et l'indique.
* ?ajuda: Fonction d'aide, malheureusement je n'ai pas réussi à remplacer la fonction d'aide, alors j'en ai créé une autre avec un nom différent.

API Tracker by https://apex.tracker.gg/site-api
Code source by https://github.com/AdautoP
