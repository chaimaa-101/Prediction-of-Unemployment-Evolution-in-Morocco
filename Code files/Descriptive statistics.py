import pandas as pd

url_excel = "Dataset.xlsx"

# Lire le fichier Excel depuis le chemin local
df = pd.read_excel(url_excel, index_col='trimestres')

# Afficher des statistiques descriptives pour toutes les colonnes
descriptive_stats = df.describe(include="all")

# Ajouter une colonne avec des étiquettes appropriées au début de chaque statistique
descriptive_stats.insert(0, 'Statistique', descriptive_stats.index)

# Sauvegarder les statistiques descriptives dans un fichier Excel
descriptive_stats.to_excel("Path.xlsx", index=False)
