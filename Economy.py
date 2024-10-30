import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('csv/data_economy.csv')

# Display the first few rows of the dataframe
print(data.head())

# Convert the 'Jobless Rate' column to numeric, coercing errors
data['Jobless Rate'] = pd.to_numeric(data['Jobless Rate'], errors='coerce')

# Drop rows with NaN values in the 'Jobless Rate' column
data.dropna(subset=['Jobless Rate'], inplace=True)

# Filter for European countries
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

# Filter the dataframe to include only European countries
europe_data = data[data['Country'].isin(european_countries)]

# Get top 10 best and worst countries based on Jobless Rate
top_10_best = europe_data.nsmallest(10, 'Jobless Rate')  # Lower jobless rate is better
top_10_worst = europe_data.nlargest(10, 'Jobless Rate')  # Higher jobless rate is worse

# Set up the visualizations
plt.figure(figsize=(14, 6))

# Plot for the top 10 best countries
plt.subplot(1, 2, 1)
sns.barplot(data=top_10_best, x='Jobless Rate', y='Country', palette='viridis')
plt.title('Top 10 Best European Countries by Employment Rate')
plt.xlabel('Jobless Rate (%)')
plt.ylabel('Country')

# Plot for the top 10 worst countries
plt.subplot(1, 2, 2)
sns.barplot(data=top_10_worst, x='Jobless Rate', y='Country', palette='magma')
plt.title('Top 10 Worst European Countries by Employment Rate')
plt.xlabel('Jobless Rate (%)')
plt.ylabel('Country')

plt.tight_layout()
plt.show()

# Prepare lists for printing to a file
best_jobless_rate_countries = top_10_best['Country'].tolist()
worst_jobless_rate_countries = top_10_worst['Country'].tolist()

# Print the lists to a file
with open('best_worst_jobless_rate.txt', 'w') as f:
    f.write("Top 10 Countries with Lowest Jobless Rate:\n")
    f.write(", ".join(best_jobless_rate_countries) + "\n\n")
    f.write("Top 10 Countries with Highest Jobless Rate:\n")
    f.write(", ".join(worst_jobless_rate_countries) + "\n")

print("Lists printed to 'best_worst_jobless_rate.txt'")
