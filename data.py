import matplotlib.pyplot as plt 
import pandas as pd 
import os as os
dir_path = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(dir_path, f"data")

df = pd.read_csv(f"{file}.csv")

print(df)

    
categories = ["operations", "R&D", "sales and marketing", "general and administration"]
colors = ["#d0e1f9", "#aec6cf", "#c2b280", "#cba135"]

fig, ax1 = plt.subplots(figsize=(8, 4))

# Initialize stack base
bottom = pd.Series([0] * df.shape[0])

# Plot stacked bars
for cat, color in zip(categories, colors):
    # Divide by six since the values are given per month
    values = df[cat].astype(float).values
    ax1.bar(df["Year"], values, bottom=bottom, label=cat, color=color)
    bottom += values

# Finalize
ax1.set_ylabel("Number of employees (thousands)", color="blue")
ax1.tick_params(axis='x', rotation=45)
ax1.legend()

plt.savefig(f"{file}.svg")