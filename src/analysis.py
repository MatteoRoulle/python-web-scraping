import csv
import os

fichiers = os.listdir("../data")
FICHIER_RAPPORT = "rapport.txt"


def lire_donnees():
    categories = []
    liste_lignes = []
    price = []
    nombre_stock = 0

    for fichier in fichiers:
        with open(f"../data/{fichier}", newline="", encoding="utf-8") as f:
            lecteur = csv.DictReader(f)

            cat = []
            for ligne in lecteur:
                prix_converti = ""
                for lettre in ligne["Prix"]:
                    if lettre != ",":
                        prix_converti += lettre
                    else:
                        break

                desc = {
                    "Page": ligne["Page"],
                    "Titre": ligne["Titre"],
                    "Prix": int(prix_converti),
                    "Stock": ligne["Stock"] == "En Stock"
                }
                cat.append(desc)

            categories.append(cat)
            liste_lignes.append({fichier: len(cat)})

            total_prix = sum(item["Prix"] for item in cat)
            page = cat[0]["Page"]

            price.append({
                "Page": page,
                "Total": total_prix,
                "Produits": len(cat)
            })

    moyenne_prix = {p["Page"]: round(p["Total"] / p["Produits"]) for p in price}
    
    produits_uniques = {}

    for cat in categories:
        for produit in cat:
            titre = produit["Titre"]
            prix = produit["Prix"]
            stock = produit["Stock"]

            if titre not in produits_uniques:
                produits_uniques[titre] = prix
                if stock:
                    nombre_stock += 1

    total_unique = sum(produits_uniques.values())
    nb_produits_uniques = len(produits_uniques)

    moyenne_totale = total_unique / nb_produits_uniques if nb_produits_uniques > 0 else 0

    with open("../logs/analyses.txt", "w", encoding="utf-8") as f:
        f.write(
            "ANALYSE DES DONNEES TERMINEE\n"
            "----------------------------\n\n"
            f"Nombre de pages : {len(categories)}\n"
            f"Noms des pages : {fichiers}\n\n"
            f"Lignes par fichier : {liste_lignes}\n"
            f"Lignes totales : {sum(d[list(d.keys())[0]] for d in liste_lignes)}\n\n"
            f"Nombre de produits uniques en stock : {nb_produits_uniques}\n"
            f"Produits en stock : {nombre_stock}\n"
            f"Moyenne de prix par page : {moyenne_prix}\n"
            f"Moyenne totale (sans doublons, en stock) : {round(moyenne_totale)} €\n"
        )
