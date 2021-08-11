from math import exp
from os import system
import random, time

 print(""" _______           __ __ __       __    
|       \         |  \  \  \     |  \   
| ▓▓▓▓▓▓▓\ ______  \▓▓\▓▓ ▓▓   __ \▓▓   
| ▓▓__/ ▓▓|      \|  \  \ ▓▓  /  \  \   
| ▓▓    ▓▓ \▓▓▓▓▓▓\ ▓▓ ▓▓ ▓▓_/  ▓▓ ▓▓   
| ▓▓▓▓▓▓▓\/      ▓▓ ▓▓ ▓▓ ▓▓   ▓▓| ▓▓   
| ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓ ▓▓ ▓▓▓▓▓▓\| ▓▓__ 
| ▓▓    ▓▓\▓▓    ▓▓ ▓▓ ▓▓ ▓▓  \▓▓\ ▓▓  \\
 \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓\▓▓\▓▓   \▓▓\▓▓\▓▓""")


print("This generator only generates Visa credit cards.")
nb_nitros = int(input("Veuillez saisir le nombre de cartes à générer: "))
nb = 1
print("Génération de la carte de crédits..")
while nb <= nb_nitros:
    exp_date2 = str(random.randint(1, 12))
    if exp_date2 == str(1):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(2):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(3):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(4):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(5):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(6):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(7):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(8):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(9):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(10):
        pass
    elif exp_date2 == str(11):
        pass
    elif exp_date2 == str(12):
        pass
    card = "4540 03" + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999)) + " | " + exp_date2 + "/"  + str(random.randint(21, 26)) + " | " + str(random.randint(100, 999))
    f = open('Codes.txt', "a+")
    f.write(f'{card}\n')
    f.close()

    print(f"[GENERATED] - {card}")
    time.sleep(0.025)
    nb += 1
