import pandas as pd
import seaborn as sns

# Încărcarea dataset-ului tips
tips = sns.load_dataset("tips")

# 1. Dimensiunea, tipurile de date și statisticile descriptive
print("Dimensiunea dataset-ului:")
print(tips.shape)

print("\nTipurile de date:")
print(tips.dtypes)

print("\nStatistici descriptive:")
print(tips.describe())

# 2. Bacșișul mediu per zi și per sex
print("\nBacșiș mediu per zi și sex:")
avg_tip = tips.groupby(["day", "sex"]).mean(numeric_only=True)
print(avg_tip["tip"])

# 3. Crearea unei coloane noi procent_bacsis (pe copie)
tips_copy = tips.copy()

tips_copy["procent_bacsis"] = (tips_copy["tip"] / tips_copy["total_bill"]) * 100

print("\nPrimele rânduri cu noua coloană:")
print(tips_copy.head())

# 4. Cele mai generoase 5 mese
top5 = tips_copy.sort_values(by="procent_bacsis", ascending=False).head(5)

print("\nTop 5 mese cu cel mai mare procent de bacșiș:")
print(top5[["total_bill", "tip", "procent_bacsis"]])

# 5. Numărul de mese per zi și categorie de fumători
meals = tips.groupby(["day", "smoker"]).size()

print("\nNumăr de mese per zi și categorie de fumători:")
print(meals)