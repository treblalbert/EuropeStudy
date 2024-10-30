import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'csv/life_expectancy_by_country.csv'
data = pd.read_csv(file_path)

# Extract the relevant columns
data = data[['country_name', 'year', 'value']]

# List of European countries
european_countries = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus",
    "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia",
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia",
    "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro",
    "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
    "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"
]

# Filter the data to include only European countries
european_data = data[data['country_name'].isin(european_countries)]

# Get the latest year of data for each country
latest_data = european_data.loc[european_data.groupby('country_name')['year'].idxmax()]

# Rank the top 10 best life expectancy
top_10_best = latest_data.nlargest(10, 'value')

# Rank the top 10 worst life expectancy
top_10_worst = latest_data.nsmallest(10, 'value')

# Create Seaborn tables for visualization
plt.figure(figsize=(12, 6))

# Top 10 best life expectancy
plt.subplot(1, 2, 1)
ax1 = sns.barplot(x='value', y='country_name', data=top_10_best, palette='Blues_d')
plt.title('Top 10 Countries with Best Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('Country')

# Add life expectancy values on top of the bars
for index, value in enumerate(top_10_best['value']):
    ax1.text(value, index, f'{value:.1f}', va='center')

# Top 10 worst life expectancy
plt.subplot(1, 2, 2)
ax2 = sns.barplot(x='value', y='country_name', data=top_10_worst, palette='Reds_d')
plt.title('Top 10 Countries with Worst Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('Country')

# Add life expectancy values on top of the bars
for index, value in enumerate(top_10_worst['value']):
    ax2.text(value, index, f'{value:.1f}', va='center')

plt.tight_layout()
plt.show()

# Prepare lists for printing to a file
best_life_expectancy_countries = top_10_best['country_name'].tolist()
worst_life_expectancy_countries = top_10_worst['country_name'].tolist()

# Print the lists to a file
with open('best_worst_life_expectancy.txt', 'w') as f:
    f.write("Top 10 Countries with Best Life Expectancy:\n")
    f.write(", ".join(best_life_expectancy_countries) + "\n\n")
    f.write("Top 10 Countries with Worst Life Expectancy:\n")
    f.write(", ".join(worst_life_expectancy_countries) + "\n")

print("Lists printed to 'best_worst_life_expectancy.txt'")
