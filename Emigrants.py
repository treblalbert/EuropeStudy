import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for the emigrants table
data = {
    'Country': ['Germany', 'Spain', 'France', 'Poland', 'Romania', 'Italy', 'Switzerland', 'Netherlands', 'Belgium', 'Greece'],
    'Emigrants (2022)': [533485, 531889, 249355, 228006, 202311, 150189, 122123, 109616, 84627, 80307]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the total number of emigrants
total_emigrants = df['Emigrants (2022)'].sum()

# Set up the plot
plt.figure(figsize=(8, 6))
sns.set_theme(style="whitegrid")

# Using a color palette with the 'YlGnBu' colormap
table = sns.heatmap(
    df[['Emigrants (2022)']],  # Plotting the 'Emigrants (2022)' column
    annot=True,                # Annotate cells with the emigrant numbers
    fmt=',',                   # Format numbers with commas
    cmap="YlGnBu",             # Color palette
    cbar=False,                # Remove color bar
    linewidths=0.5
)

# Customize the table appearance
table.set_yticklabels(df['Country'], rotation=0)  # Display countries as row labels
table.set_xticklabels(["Emigrants (2022)"], rotation=0)  # Display 'Emigrants (2022)' as column header
plt.title("2022 Emigrants by Country")
plt.show()
