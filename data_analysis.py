import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os



# 1. LOAD DATA
try:
    df = pd.read_csv('All_Diets.csv')
    print(f"✅ Successfully loaded {len(df)} recipes")
    print(f"Columns found: {df.columns.tolist()}")
except Exception as e:
    print(f"❌ Error loading CSV: {e}")
    exit(1)

# 2. HANDLE MISSING VALUES
numeric_cols = ['Protein(g)', 'Carbs(g)', 'Fat(g)']
for col in numeric_cols:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace=True)
print("✅ Missing values handled")

# 3. CALCULATE AVERAGE MACROS PER DIET TYPE
avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean().round(2)
print("\n=== AVERAGE MACROS PER DIET ===")
print(avg_macros)
avg_macros.to_csv('avg_macros_by_diet.csv')

<<<<<<< HEAD
# 4. TOP 5 PROTEIN RECIPES PER DIET
top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)
top_protein[['Diet_type', 'Recipe_name', 'Protein(g)']].to_csv('top5_protein_per_diet.csv')
print("✅ Top protein recipes saved")

# 5. DIET WITH HIGHEST PROTEIN
highest_protein_diet = df.groupby('Diet_type')['Protein(g)'].mean().idxmax()
highest_value = df.groupby('Diet_type')['Protein(g)'].mean().max()
print(f"\n=== HIGHEST PROTEIN DIET ===")
print(f"🏆 {highest_protein_diet} with average {highest_value:.2f}g protein")

# 6. MOST COMMON CUISINE PER DIET
most_common_cuisine = df.groupby('Diet_type')['Cuisine_type'].agg(lambda x: x.mode()[0] if not x.mode().empty else 'Unknown')
print("\n=== MOST COMMON CUISINE PER DIET ===")
print(most_common_cuisine)
most_common_cuisine.to_csv('common_cuisine_per_diet.csv')

# 7. CREATE NEW METRICS
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)'].replace(0, 0.01)
df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)'].replace(0, 0.01)
df[['Recipe_name', 'Protein_to_Carbs_ratio', 'Carbs_to_Fat_ratio']].to_csv('ratio_metrics.csv')
print("✅ Ratio metrics calculated")

# 8. VISUALIZATION 1: BAR CHART
plt.figure(figsize=(12, 6))
avg_macros.plot(kind='bar')
plt.title('Average Macronutrient Content by Diet Type', fontsize=16)
plt.ylabel('Grams', fontsize=12)
plt.xlabel('Diet Type', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('avg_macros_bar_chart.png', dpi=150)
plt.show()
print("✅ Bar chart saved as avg_macros_bar_chart.png")
=======
    ### visualize data for macronutrients
    ## bar graphs
    # bar graph to show average protein for each diet type
    sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'])
    plt.title('Average Protein by Diet Type')
    plt.ylabel('Average Protein (g)')
    plt.savefig('avg_macros_protein_bar.png')
    plt.show()

    # bar graph to show average carbs for each diet type
    sns.barplot(x=avg_macros.index, y=avg_macros['Carbs(g)'])
    plt.title('Average Carbs by Diet Type')
    plt.ylabel('Average Carbs (g)')
    plt.savefig('avg_macros_carbs_bar.png')
    plt.show()

    # bar graph to show average fat for each diet type
    sns.barplot(x=avg_macros.index, y=avg_macros['Fat(g)'])
    plt.title('Average Fat by Diet Type')
    plt.ylabel('Average Fat (g)')
    plt.savefig('avg_macros_fat_bar.png')
    plt.show()

    ## heatmap
    # heatmap to show average macronutrients for each diet type
    heatmap_data = avg_macros.T
    heatmap_data.index = ["Protein (g)", "Carbs (g)", "Fat (g)"]
    plt.figure(figsize=(10, 3.5))
    sns.heatmap(
        heatmap_data,
        annot=True, fmt=".1f",
        cmap="YlGnBu",
        linewidths=0.5,
        cbar_kws={"label": "Average grams"}
    )
    plt.title("Average Macronutrients by Diet Type")
    plt.xlabel("Diet type")
    plt.ylabel("Macronutrient")
    plt.tight_layout()
    plt.savefig('avg_macros_heatmap.png')
    plt.show()

    ## scatterplot
    # scatterplot to show the top 5 protein-rich recipes and their distribution across cuisines
    sns.scatterplot(data=top_protein, x='Protein(g)', y='Cuisine_type')
    plt.title('Top 5 Protein Rich Recipes')
    plt.xlabel('Protein (g)')
    plt.ylabel('Cuisine Type')
    plt.savefig('top_protein_recipes.png')
    plt.show()
>>>>>>> d7363e47f169ac059fe480e3c6ace1efb35bc309

# 9. VISUALIZATION 2: HEATMAP
plt.figure(figsize=(10, 8))
sns.heatmap(avg_macros.T, annot=True, cmap='YlOrRd', fmt='.1f')
plt.title('Macronutrient Distribution Heatmap by Diet Type', fontsize=16)
plt.tight_layout()
plt.savefig('macro_heatmap.png', dpi=150)
plt.show()
print("✅ Heatmap saved as macro_heatmap.png")

# 10. VISUALIZATION 3: SCATTER PLOT
top_50_protein = df.nlargest(50, 'Protein(g)')
plt.figure(figsize=(14, 7))
sns.scatterplot(data=top_50_protein, x='Cuisine_type', y='Protein(g)', 
                hue='Diet_type', size='Protein(g)', sizes=(50, 500))
plt.title('Top 50 Protein-Rich Recipes by Cuisine', fontsize=16)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('top_protein_scatter.png', dpi=150)
plt.show()
print("✅ Scatter plot saved as top_protein_scatter.png")

print(f"\n=== ANALYSIS COMPLETE at {datetime.now()} ===")
print("📁 Files generated:")
for file in ['avg_macros_by_diet.csv', 'top5_protein_per_diet.csv', 'common_cuisine_per_diet.csv', 
             'ratio_metrics.csv', 'avg_macros_bar_chart.png', 'macro_heatmap.png', 'top_protein_scatter.png']:
    if os.path.exists(file):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file}")
