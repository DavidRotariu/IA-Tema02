import matplotlib.pyplot as plt
import seaborn as sns

# Încărcare dataset
tips = sns.load_dataset("tips")

# Ordinea zilelor
day_order = ["Thur", "Fri", "Sat", "Sun"]

# Creare figura cu 2x2 subploturi
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Scatter plot (Matplotlib)
ax = axes[0, 0]

colors = {"Male": "blue", "Female": "red"}

for sex in tips["sex"].unique():
    subset = tips[tips["sex"] == sex]
    ax.scatter(subset["total_bill"], subset["tip"],
               label=sex, color=colors[sex], alpha=0.7)

ax.set_title("Total Bill vs Tip (by Sex)")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")
ax.legend()


# 2. Boxplot (Seaborn)
ax = axes[0, 1]

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    order=day_order,
    ax=ax
)

ax.set_title("Distribuția Total Bill per Day")
ax.set_xlabel("Day")
ax.set_ylabel("Total Bill")


# 3. Histogramă (Seaborn histplot)
ax = axes[1, 0]

sns.histplot(
    data=tips,
    x="tip",
    hue="time",
    kde=True,
    ax=ax
)

ax.set_title("Distribuția Tip (Lunch vs Dinner)")
ax.set_xlabel("Tip")
ax.set_ylabel("Count")


# 4. Barplot (Seaborn)
ax = axes[1, 1]

sns.barplot(
    data=tips,
    x="day",
    y="tip",
    order=day_order,
    errorbar="ci",
    ax=ax
)

ax.set_title("Bacșiș mediu per Day")
ax.set_xlabel("Day")
ax.set_ylabel("Average Tip")


# Ajustare layout
plt.tight_layout()

# Salvare figură
plt.savefig("tips_analysis.png")

# Afișare
plt.show()