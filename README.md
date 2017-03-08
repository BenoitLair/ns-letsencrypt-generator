# ns-letsencrypt-generator
-==============================================================================-
Cette application sert à générer et a gérer des certificats ssl let's encrypt pour du netscaler
L'application s'installe sur un serveur ubuntu 16.04

pour que ns-letsencrypt fonctionnes il faut : 

apt-get install python git python-pip curl
pip install requests

Ensuite il faut installer : 

pip install python-crontab


Usage : 

python test1.py letsencrypt-src/ns-letsencrypt/ ns-letsencrypt-nom-nouveau-certificat


- letsencrypt-src/ns-letsencrypt/ est la source de ns-letsencrypt
- ns-letsencrypt-nom-nouveau-certificat est le nouveau dossier à créer qui contiendra le nouveau certificat