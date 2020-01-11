### Vous trouverez également le rendu sur github à l'adresse : https://github.com/florinePrat/renduAsaiot
# renduAsaiot
Bonjour ce projet à pour but de contrôler l'ouverture et la fermeture des volets électriques en fonction de la température et de la luminosité. 
Il permet donc d'être plus économique et plus écologique.

Attention : c'est une simulation grâce à une raspberry et un montage avec un petit moteur, Pas un cas réel.
Language utilisé pour ce projet :
  - Python avec le framework flask
  - html
  - css
  - js
  
Tous les fichiers dans le dossier static, à savoir :
  - css
  - images
  - font
  - vendor
  
Servent uniquement pour le style de la page web et ne sont donc pas necessaire au bon fonctionnemment. 

### Installation

Il ne fonctionne que depuis une raspberry directement.
Installer les dépendances et démmarer le serveur.

```sh
$ cd renduAsaiot
$ apt-get install
$ python3 view.py flask run
```

Le serveur se lance donc et demande de se rendre à l'adresse : 

```sh
http://127.0.0.1:5000/
```

Vous arrivez donc sur l'interface web (index.html). Vous pouvez donc entrer votre température souhaité, ainsi que l'état actuel des volets. Puis cliquer sur submit.
Notons ici que seul le mode automatique fonctionne, le mode manuel n'est pas implémenté.

### Le programme se lance donc automatiquement sur la raspberry et les logs sont sur le terminal.

Ce projet est un projet scolaire d'initiation à l'iot et à la dommotique
