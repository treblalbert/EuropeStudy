import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the lists
happiest_countries = ["Switzerland", "Iceland", "Denmark", "Norway", "Finland", 
                      "Netherlands", "Sweden", "Austria", "Luxembourg", "Ireland"]

life_expectancy_countries = ["San Marino", "Norway", "Switzerland", "Iceland", "Malta", 
                             "Sweden", "Italy", "Spain", "Ireland", "France"]

air_quality_countries = ["Latvia", "Liechtenstein", "Moldova", "Andorra", "Denmark", 
                        "Albania", "Finland", "Lithuania", "Estonia", "Iceland"]

jobless_rate_countries = ["Switzerland", "Moldova", "Denmark", "Malta", "Norway", 
                          "Hungary", "United Kingdom", "Czech Republic", "Russia", "Netherlands"]

# Create a DataFrame
data = {
    'Happiness': happiest_countries,
    'Life Expectancy': life_expectancy_countries,
    'Air Quality': air_quality_countries,
    'Jobless Rate': jobless_rate_countries
}

df = pd.DataFrame(data)

# Convert country names to numerical rankings (1 to 10)
ranking_df = df.apply(lambda x: pd.factorize(x)[0] + 1).T  # Add 1 for ranking from 1 to 10

# Display the rankings as a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(ranking_df, annot=df.T.values, fmt='', cmap='YlGnBu', cbar=False)
plt.title('Country Rankings by Aspect (1 to 10)')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.xlabel('Countries')
plt.ylabel('Aspects')
plt.show()

# Count appearances of each country across the lists
country_counts = pd.Series(happiest_countries + life_expectancy_countries + 
                           air_quality_countries + jobless_rate_countries)

# Group by country and count occurrences
country_appearance_count = country_counts.value_counts()

# Create a bar plot for country appearances with a color palette
plt.figure(figsize=(12, 6))
colors = sns.color_palette("viridis", len(country_appearance_count))  # Using a color palette
country_appearance_count.plot(kind='bar', color=colors)
plt.title('Number of Appearances of Each Country Across Lists')
plt.xlabel('Countries')
plt.ylabel('Number of Appearances')
plt.xticks(rotation=45)
plt.show()
