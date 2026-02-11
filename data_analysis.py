import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def process_data():
    df = pd.read_csv("All_Diets.csv")
    df.fillna(pd.DataFrame( # reads data values instead of string headers and data values causing type mismatch
        [df['Protein(g)'].mean(), df['Carbs(g)'].mean(), df['Fat(g)'].mean()]
    ).mean(), inplace=True)

    avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
    top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)

    df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)']
    df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)']


    ## visualize data for macronutrients
    # bar graph to show average protein for each diet type
    sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'])
    plt.title('Average Protein by Diet Type')
    plt.ylabel('Average Protein (g)')
    plt.show()

    # bar graph to show average carbs for each diet type
    sns.barplot(x=avg_macros.index, y=avg_macros['Carbs(g)'])
    plt.title('Average Protein by Diet Type')
    plt.ylabel('Average Carbs (g)')
    plt.show()

    sns.barplot(x=avg_macros.index, y=avg_macros['Fat(g)'])
    plt.title('Average Fat by Diet Type')
    plt.ylabel('Average Fat (g)')
    plt.show()


    sns.heatmap(data=avg_macros['Protein(g)'], cmap='YlGnBu')

if __name__ == '__main__':
    process_data()