import pandas as pd
import os

# URL of dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
save_path = "raw_data/iris.csv"

# Create raw_data folder if not exists
os.makedirs("raw_data", exist_ok=True)

# Download and save
df = pd.read_csv(url)
df.to_csv(save_path, index=False)

print(f"Data saved to: {save_path}")
