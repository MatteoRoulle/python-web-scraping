# Python Web Scraping

Ce projet est un outil Python de **web scraping**, de **nettoyage de données** et d’**analyse automatisée** à partir de fichiers CSV.
Il met en pratique la récupération de données web, traitement de données structurées, automatisation et génération de rapports.

---

## Objectifs du projet

- Extraire des données depuis des pages web
- Sauvegarder les données sous forme de fichiers CSV
- Nettoyer les données collectées
- Analyser les données (prix, stock, catégories)
- Générer des rapports automatiques lisibles

---

## Fonctionnalités

### Web scraping
- Récupération automatique de données depuis plusieurs pages
- Gestion de la pagination

### Nettoyage des données
- Suppression des lignes incomplètes
- Nettoyage des espaces et caractères invalides
- Création de fichiers CSV propres

### Analyse des données
- Nombre total de produits
- Analyse des prix
- Répartition par catégorie

### Rapports automatiques
- Génération d’un fichier texte récapitulatif
- Résumés des nettoyages

---

## Exécution

Dans un terminal : `python src/main.py`

## Explications

Le script :
  - Scrape les pages ciblées
  - Génère des fichiers CSV
  - Nettoie les données
  - Produit un rapport dans le dossier `logs/`

