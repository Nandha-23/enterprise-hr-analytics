import zipfile

zip_path = "multi-company-hr-analytics-20192025.zip"

extract_path = "data/raw"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset extracted successfully")