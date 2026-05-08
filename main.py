from scripts.download_data import load_dataset
from scripts.preprocess import clean_data
from scripts.visualize import create_visualizations

print("Enterprise HR Analytics Project Started")

# Load Dataset
raw_df = load_dataset("data/raw/employees.csv")

# Clean Dataset
cleaned_df = clean_data(raw_df)

# Save cleaned data
cleaned_df.to_csv("data/cleaned/cleaned_employees.csv", index=False)

print("Cleaned data saved successfully")

# Create charts
create_visualizations(cleaned_df)

print("Charts generated successfully")