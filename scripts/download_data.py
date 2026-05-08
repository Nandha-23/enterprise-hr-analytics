import os

print("Downloading dataset...")

os.system(
    "kaggle datasets download -d raghavgour/multi-company-hr-analytics-20192025"
)

print("Dataset downloaded successfully")