from __future__ import print_function
from __future__ import division
from builtins import input

from gopigo import *
import sys
import atexit
import requests

atexit.register(stop)


#### fwd() stop() bwd() les fonctions pour faire bouger les moteurs



from grovepi import *
import grovepi,math,time

#!/usr/bin/env python
# coding : utf-8

import sys
print(sys.argv)


sensor=4 #Temperature sensor plugged at D4
light_sensor=0 #Light sensor plugged at A0
ultrasonic=3 #Range sensor plugged at D3
blue=0 

fonctionnalite_activee = True
objet_detectee=False
seuil = 700
seuil_distance=20

#[interieur,humidite_interieure] = grovepi.dht(sensor,blue)



#print("À l'interieur il fait : ",interieur," degrés.")

api_result = requests.get('http://api.weatherstack.com/current?access_key=6eae411c313bdb85639094063a7d62c8&query=Montpellier')
api_response = api_result.json()
print(u'La temperature acctuelle a %s est de : %d℃' % (api_response['location']['name'], api_response['current']['temperature']))


ext= int(api_response['current']['temperature'])     

i=0

souhaitee = int( sys.argv[1] )
reponse = ( sys.argv[2] )
if reponse =="ouvert":
	ouvert = True
elif reponse=="ferme":
	ouvert = False

def monter_volet(seconde):
	fwd()
	time.sleep(seconde)
	stop()
		

def descendre_volet(seconde):
	bwd()
	time.sleep(seconde)
	stop()

seconde=2.1

while True:

	#On obtient la luminosité mesurée par le detecteur
	lumiere=grovepi.analogRead(light_sensor)
	#On récupère la température interieure
	[interieur,humidite_interieure] = grovepi.dht(sensor,blue)
	
	while i<7:
	#Récupère la mesure du detecteur de distance
		distance=ultrasonicRead(ultrasonic)
		i=i+1
	i=0
	
	if distance<seuil_distance:
		objet_detectee=True


	print("Il fait ",interieur," degrés chez vous")

	if fonctionnalite_activee:
		if not objet_detectee:
			if souhaitee>interieur: #Température souhaitée inferieur  la température exterieure
				if ext>interieur: # Il fait plus chaud à l'exterieur
					if not ouvert: #La volet est fermé
						print("Monter, on veut faire entrer de la chaleur")
						monter_volet(seconde)
						ouvert=True
					else : print("Déjà ouvert")# souhaitée>exterieur>interieur et ouvert
				else:
					if lumiere>seuil: #interieur<exterieur 
						if not ouvert:
							print("Monter, on veut faire entrer les rayons du soleil")
							monter_volet(seconde)
							ouvert=True
						else: 
							print("Le volet est déjà levé")
					else:
						if ouvert:
							print("Fermer, on ne veut pas perdre de la chaleur")
							descendre_volet(seconde)
							ouvert=False
						else: print("Déjà fermé")
			else: #Ici il fait plus chaud que souhaité
				if ext<interieur:
					if not ouvert:
						print("Monter, on veut perdre de la chaleur")
						monter_volet(seconde)
						ouvert=True
					else:
						print("Déjà ouvert")
				else:
					if ouvert:
						print("Fermer, on ne veut pas faire entrer plus de chaleur")
						descendre_volet(seconde)
						ouvert=False
					else: print("Déjà fermé")
		else:
			print("Envoi du message, objet detecté ! desactivation de la fonctionnalité")
			fonctionnalite_activee=False

	time.sleep(5) 



