import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_theme(style='whitegrid')

tips = sns.load_dataset('tips')
print(f"Dataset încărcat cu succes! {tips.shape[0]} înregistrări")

colors = {'Male': '#3498db', 'Female': '#e74c3c'}
order_days = ['Thur', 'Fri', 'Sat', 'Sun']


fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Dashboard Analiză Dataset Tips\n(Visualizări multiple)', 
             fontsize=18, fontweight='bold', y=0.98)

ax1 = axes[0, 0]

if len(tips) > 0:
    for sex, color in colors.items():
        subset = tips[tips['sex'] == sex]
        
        if len(subset) > 0:
            scatter = ax1.scatter(subset['total_bill'], 
                                 subset['tip'], 
                                 c=color, 
                                 label=sex,
                                 alpha=0.7, 
                                 s=80,  # mărimea punctelor
                                 edgecolors='white', 
                                 linewidth=1)
            if len(subset) >= 2:
                try:
                    z = np.polyfit(subset['total_bill'], subset['tip'], 1)
                    p = np.poly1d(z)
                    # Sortăm x pentru o linie frumoasă
                    x_sorted = np.sort(subset['total_bill'])
                    ax1.plot(x_sorted, 
                            p(x_sorted), 
                            color=color, 
                            linestyle='--', 
                            alpha=0.5,
                            linewidth=1.5)
                except Exception as e:
                    print(f"Nu s-a putut adăuga linia de trend pentru {sex}: {e}")

# subplot 1
ax1.set_title('Relația dintre total factură și bacșiș\n(împărțit pe sexe)', fontsize=13, fontweight='bold')
ax1.set_xlabel('Total factură ($)', fontsize=11)
ax1.set_ylabel('Bacșiș ($)', fontsize=11)
ax1.legend(title='Sex', fontsize=10, title_fontsize=11)
ax1.grid(True, alpha=0.3, linestyle='--')

# Adăugăm statistici în colț
correlatie = tips['total_bill'].corr(tips['tip'])
ax1.text(0.05, 0.95, f'Corelație: {correlatie:.2f}\nTotal puncte: {len(tips)}', 
         transform=ax1.transAxes, fontsize=10,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax2 = axes[0, 1]

sns.boxplot(data=tips, 
            x='day', 
            y='total_bill', 
            order=order_days,
            palette='Set2',  # Paletă de culori plăcută
            ax=ax2)

# subplot 2
ax2.set_title('Distribuția totalului facturii pe zile', fontsize=13, fontweight='bold')
ax2.set_xlabel('Ziua săptămânii', fontsize=11)
ax2.set_ylabel('Total factură ($)', fontsize=11)
ax2.grid(True, alpha=0.3, axis='y', linestyle='--')

# Adăugăm mediana pe fiecare boxplot
medians = tips.groupby('day')['total_bill'].median()
for i, day in enumerate(order_days):
    if day in medians.index:  # Verificăm că ziua există
        ax2.text(i, medians[day], f'Mediană: {medians[day]:.1f}$', 
                 ha='center', va='bottom', fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

ax3 = axes[1, 0]

sns.histplot(data=tips, 
             x='tip', 
             hue='time', 
             kde=True, 
             bins=20,
             palette=['#f39c12', '#9b59b6'],  # Portocaliu pentru Lunch, mov pentru Dinner
             alpha=0.6,
             ax=ax3)

# subplot 3
ax3.set_title('Distribuția bacșișului - Lunch vs Dinner', fontsize=13, fontweight='bold')
ax3.set_xlabel('Bacșiș ($)', fontsize=11)
ax3.set_ylabel('Frecvență', fontsize=11)
ax3.legend(title='Momentul zilei', fontsize=10, title_fontsize=11)
ax3.grid(True, alpha=0.3, linestyle='--', axis='y')

# Adăugăm linii pentru medii
media_lunch = tips[tips['time'] == 'Lunch']['tip'].mean()
media_dinner = tips[tips['time'] == 'Dinner']['tip'].mean()
ax3.axvline(media_lunch, color='#f39c12', linestyle='--', linewidth=2, alpha=0.8, label=f'Media Lunch: {media_lunch:.2f}$')
ax3.axvline(media_dinner, color='#9b59b6', linestyle='--', linewidth=2, alpha=0.8, label=f'Media Dinner: {media_dinner:.2f}$')


ax4 = axes[1, 1]

sns.barplot(data=tips, 
            x='day', 
            y='tip', 
            order=order_days,
            palette='Blues_d',
            errorbar='ci',  # interval de încredere 95%
            capsize=0.2,    # mărimea capacelor la barele de eroare
            errwidth=1.5,   # grosimea barelor de eroare
            ax=ax4)

#  subplot 4
ax4.set_title('Bacșișul mediu pe zile\n(cu interval de încredere 95%)', fontsize=13, fontweight='bold')
ax4.set_xlabel('Ziua săptămânii', fontsize=11)
ax4.set_ylabel('Bacșiș mediu ($)', fontsize=11)
ax4.grid(True, alpha=0.3, axis='y', linestyle='--')

# Adăugăm valorile medii deasupra barelor
means = tips.groupby('day')['tip'].mean()
for i, day in enumerate(order_days):
    if day in means.index:
        ax4.text(i, means[day] + 0.1, f'{means[day]:.2f}$', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')


# Ajustăm layout-ul pentru a evita suprapunerile
plt.tight_layout()
# Ajustăm pentru a face loc titlului principal
plt.subplots_adjust(top=0.93)

# Salvăm figura
output_filename = 'dashboard_tips.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight', facecolor='white')
plt.show()