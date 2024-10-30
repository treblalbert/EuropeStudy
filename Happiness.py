import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of European countries
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
    'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
    'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
    'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
    'United Kingdom', 'Vatican City'
]

# Load happiness data from CSV
happiness_data = pd.read_csv('csv/data_happy.csv')

# Filter data for only European countries
happiness_data = happiness_data[happiness_data['Country'].isin(european_countries)]

# Sort data to identify happiest and least happy countries
happiest_countries = happiness_data.sort_values(by='Happiness Score', ascending=False).head(10)
least_happy_countries = happiness_data.sort_values(by='Happiness Score').head(10)

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot the happiest countries table
sns.heatmap(happiest_countries[['Country', 'Happiness Score']].set_index('Country').T, annot=True, fmt=".2f", cmap="Blues", cbar=False, ax=axes[0])
axes[0].set_title("Top 10 Happiest European Countries")
axes[0].set_xlabel("Country")
axes[0].set_ylabel("Happiness Score")

# Plot the least happy countries table
sns.heatmap(least_happy_countries[['Country', 'Happiness Score']].set_index('Country').T, annot=True, fmt=".2f", cmap="Purples", cbar=False, ax=axes[1])
axes[1].set_title("Top 10 Least Happy European Countries")
axes[1].set_xlabel("Country")
axes[1].set_ylabel("Happiness Score")

# Adjust layout
plt.tight_layout()
plt.show()

# Prepare lists for printing to a file
happiest_list = happiest_countries['Country'].tolist()
least_happy_list = least_happy_countries['Country'].tolist()

# Print the lists to a file
with open('happiest_least_happy_countries.txt', 'w') as f:
    f.write("Top 10 Happiest European Countries:\n")
    f.write(", ".join(happiest_list) + "\n\n")
    f.write("Top 10 Least Happy European Countries:\n")
    f.write(", ".join(least_happy_list) + "\n")

print("Lists printed to 'happiest_least_happy_countries.txt'")
