import requests
from bs4 import BeautifulSoup
import csv
import time

def scrap():
    pages = ["https://www.lescreasdeseve.com/tous-les-produits/", 
             "https://www.lescreasdeseve.com/bois-de-vigne/", 
             "https://www.lescreasdeseve.com/luminaire-a-piles/", 
             "https://www.lescreasdeseve.com/table-basse/", 
             "https://www.lescreasdeseve.com/platre2/"]
    
    for page in pages:
        response = requests.get(page)
        
        if response.status_code != 200:
            print(f"Erreur du chargement de la page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        produits = soup.find_all("article", class_="item") 
        page2 = soup.find("h1", class_="wnd-align-center")

        results = []
        
        for article in produits:
            title = article.find("span", class_="prd-title-c")
            price = article.find("div", class_="item-price").find("span", class_="prd-price-c wnd-product-price")
            image = article.find("div", class_="item-media").find("img")
            stock = article.find("div", class_="item-labels label-small").find("span", class_="prd-label-c prd-out-of-stock-c").text.strip()

            if stock == "":
                stock = "En Stock"

            product_data = {
                "Page": page2.text.strip() if page2 else "",
                "Titre": title.text.strip() if title else "",
                "Prix": price.text.strip() if price else "",
                "Stock": stock,
                "Image": image['src'].strip() if image else ""
            }

            results.append(product_data)

        if page == pages[0]:
            for i in range(1, 3):
                time.sleep(2)
                reponse = requests.get(f"https://www.lescreasdeseve.com/tous-les-produits/p-nja4otgw/{i}")

                if reponse.status_code == 200:
                    soup = BeautifulSoup(reponse.text, "html.parser")
                    produits_2 = soup.find_all("article", class_="item")

                    for article in produits_2:
                        title = article.find("span", class_="prd-title-c")
                        price = article.find("div", class_="item-price").find("span", class_="prd-price-c wnd-product-price")
                        image = article.find("div", class_="item-media").find("img")
                        stock = article.find("div", class_="item-labels label-small").find("span", class_="prd-label-c prd-out-of-stock-c").text.strip()

                        if stock == "":
                            stock = "En Stock"

                        product_data = {
                            "Page": page2.text.strip() if page2 else "",
                            "Titre": title.text.strip() if title else "",
                            "Prix": price.text.strip() if price else "",
                            "Stock": stock,
                            "Image": image['src'].strip() if image else ""
                        }

                        results.append(product_data)
                else:
                    print(f"Problème de chargement de la page {i} pour {page}")

        save_to_csv(results, page2.text.strip() if page2 else "produits")
        print(f"{len(results)} articles récupérés.")

def save_to_csv(data, page):
    if not data:
        print("Aucune donnée à enregistrer.")
        return

    page = clean_texte(page)
    with open(f"../data/raw_{page}.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def clean_texte(text):
    text = text.lower()

    accents = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 'ä': 'a', 'ç': 'c', 
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u', 'ÿ': 'y', 'œ': 'oe', 'æ': 'ae'
    }

    for accent, normal in accents.items():
        text = text.replace(accent, normal)

    text = text.replace(" ", "-")
    return text
