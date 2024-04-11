import pandas as pd

# Charger le fichier CSV
champignonsDF = pd.read_csv('data/champignons_processed.csv')
champignonsDF = champignonsDF.astype(int)

largeurs_max = [max(len(str(colonne)), champignonsDF[colonne].astype(str).map(len).max()) for colonne in champignonsDF.columns]


entetes_markdown = "| " + " | ".join(f"{colonne:<{largeur_max}}" for colonne, largeur_max in zip(champignonsDF.columns, largeurs_max)) + " |\n"


separateur = "|" + "|".join(["-" * (largeur_max+2) for largeur_max in largeurs_max]) + "|\n"


donnees_markdown = ""
for index, row in champignonsDF.iterrows():
    ligne = "| " + " | ".join([f"{str(valeur):<{largeur_max}}" for valeur, largeur_max in zip(row, largeurs_max)]) + " |\n"
    donnees_markdown += ligne


tableau_markdown = entetes_markdown + separateur + donnees_markdown


with open('data/tableau_markdown.csv', 'w') as fichier:
    fichier.write(tableau_markdown)

print("Le tableau Markdown a été écrit dans le fichier 'tableau_markdown.csv'.")
