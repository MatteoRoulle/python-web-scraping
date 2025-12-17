from analysis import *
from cleaner import *
from scraper import *
import os

for fichier in os.listdir("../data"):
    os.remove(f"../data/{fichier}")

os.remove("../logs/rapport.txt")

if __name__ == "__main__":
    scrap()
    clean()
    lire_donnees()