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

# Load data from CSV
data = pd.read_csv('csv/data_date.csv')

# Ensure Date column is in datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for only European countries
data = data[data['Country'].isin(european_countries)]

# Sort data by Date, then by AQI Value, keeping the latest record for each country
latest_data = data.sort_values(by=['Country', 'Date']).drop_duplicates(subset='Country', keep='last')

# Sort data to identify top and bottom countries by air quality
best_quality = latest_data.sort_values(by='AQI Value').head(10)
worst_quality = latest_data.sort_values(by='AQI Value', ascending=False).head(10)

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Plot the best air quality table
sns.heatmap(best_quality[['Country', 'AQI Value']].set_index('Country').T, annot=True, fmt=".0f", cmap="Greens", cbar=False, ax=axes[0])
axes[0].set_title("Top 10 European Countries with Best Air Quality")
axes[0].set_xlabel("Country")
axes[0].set_ylabel("AQI Value")

# Plot the worst air quality table
sns.heatmap(worst_quality[['Country', 'AQI Value']].set_index('Country').T, annot=True, fmt=".0f", cmap="Reds", cbar=False, ax=axes[1])
axes[1].set_title("Top 10 European Countries with Worst Air Quality")
axes[1].set_xlabel("Country")
axes[1].set_ylabel("AQI Value")

# Adjust layout
plt.tight_layout()
plt.show()

# Prepare lists for printing to a file
best_quality_list = best_quality['Country'].tolist()
worst_quality_list = worst_quality['Country'].tolist()

# Print the lists to a file
with open('top_bottom_countries.txt', 'w') as f:
    f.write("Top 10 European Countries with Best Air Quality:\n")
    f.write(", ".join(best_quality_list) + "\n\n")
    f.write("Top 10 European Countries with Worst Air Quality:\n")
    f.write(", ".join(worst_quality_list) + "\n")

print("Lists printed to 'best_worst_air_quality_countries.txt'")
