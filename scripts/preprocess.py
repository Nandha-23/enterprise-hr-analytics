
def clean_data(df):
    """
    Clean employee dataset
    """

    print("\nCleaning Dataset...")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing numeric values with median
    numeric_columns = df.select_dtypes(include=['number']).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values with mode
    categorical_columns = df.select_dtypes(include=['object']).columns

    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("Missing values handled")

    print("\nDataset Info:")
    print(df.info())

    return df