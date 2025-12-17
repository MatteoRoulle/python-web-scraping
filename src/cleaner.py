import csv
import os
from datetime import datetime

def clean():
    noms = os.listdir("../data")

    for nom in noms:
        donnees_propres = []
        lignes_totales = 0
        lignes_conservees = 0
        lignes_ignorees = 0

        with open(f"../data/{nom}", "r", encoding="utf-8") as fichier:
            lignes = csv.DictReader(fichier)
            colonnes = lignes.fieldnames

            for ligne in lignes:
                lignes_totales += 1
                ligne_propre = {cle: valeur.strip() for cle, valeur in ligne.items()}

                if all(ligne_propre.values()):
                    donnees_propres.append(ligne_propre)
                    lignes_conservees += 1
                else:
                    lignes_ignorees += 1

        with open(f"../data/{nom[4:]}", "w", newline="", encoding="utf-8") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=colonnes)
            writer.writeheader()
            writer.writerows(donnees_propres)

        os.remove(f"../data/{nom}")

        with open("../logs/rapport.txt", "a", encoding="utf-8") as fichier:
            fichier.write(
                f"RÉSULTAT DU NETTOYAGE DE {nom} LE {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                "----------------------------------\n\n"
                f"Lignes totales initiales : {lignes_totales}\n"
                f"Lignes conservées        : {lignes_conservees}\n"
                f"Lignes ignorées          : {lignes_ignorees}\n\n"
                "Nettoyage terminé avec succès.\n\n"
            )