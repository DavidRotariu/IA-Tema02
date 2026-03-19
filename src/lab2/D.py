import seaborn as sns
import matplotlib.pyplot as plt

# Încărcare dataset Iris
iris = sns.load_dataset("iris")

# ==============================
# 1. Pairplot complet
# ==============================

pairplot = sns.pairplot(
    iris,
    hue="species",
    diag_kind="kde"
)

# Titlu general
pairplot.fig.suptitle("Pairplot Iris Dataset", y=1.02)

# Salvare figură
pairplot.savefig("iris_pairplot.png")


# ==============================
# 2. Figură cu 4 violinplot-uri
# ==============================

numeric_cols = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

fig, axes = plt.subplots(1, 4, figsize=(18, 5))

for i, col in enumerate(numeric_cols):
    sns.violinplot(
        data=iris,
        x="species",
        y=col,
        hue="species",
        split=False,
        ax=axes[i],
        legend=False
    )

    axes[i].set_title(col)

# Titlu general
fig.suptitle("Distribuția variabilelor Iris pe specii", fontsize=14)

# Ajustare layout
plt.tight_layout()

# Salvare figură
plt.savefig("iris_violinplots.png")

# Afișare
plt.show()
