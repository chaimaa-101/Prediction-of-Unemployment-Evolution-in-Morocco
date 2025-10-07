import pandas as pd

# Remplacez "URL_DU_FICHIER_EXCEL" par le lien direct vers votre fichier Excel
url_excel = "Dataset.xlsx"

# Lire le fichier Excel depuis le lien
df = pd.read_excel(url_excel, index_col='trimestres')


# Afficher le DataFrame avant la suppression des colonnes
print("DataFrame Before Column Removal:")
print(df)

# Afficher des informations sur le DataFrame
print("\nDataFrame Information:")
df.info()

df1 = df[df.duplicated(keep=False)]

# If you want to keep at least one occurrence of each duplicate, you can use df.duplicated() without keep=False

# Print or display the duplicated rows
print("Duplicated Rows (All Columns):")
print(df1)


missing_values_count = df1.isnull().sum()

# Print or display the result
print("Missing Values Count in Each Column:")
print(missing_values_count)