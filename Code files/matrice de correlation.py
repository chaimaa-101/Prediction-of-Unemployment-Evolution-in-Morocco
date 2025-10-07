import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lire le fichier Excel depuis le chemin local
df = pd.read_excel("Dataset.xlsx", index_col='trimestres')

# Calculer la matrice de corrélation
correlation_matrix = df.corr()

# Tracer la matrice de corrélation en utilisant un heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matrice de Corrélation')
plt.show()
