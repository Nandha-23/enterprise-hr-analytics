import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations(df):
    """
    Create HR analytics charts
    """

    os.makedirs("outputs/charts", exist_ok=True)

    # Style
    sns.set(style="whitegrid")

    # -----------------------------
    # Department Count Chart
    # -----------------------------

    if 'department' in df.columns:

        plt.figure(figsize=(8, 5))

        sns.countplot(data=df, x='department')

        plt.title('Employees by Department')
        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig("outputs/charts/department_chart.png")

        plt.close()

    # -----------------------------
    # Salary Distribution
    # -----------------------------

    if 'salary' in df.columns:

        plt.figure(figsize=(8, 5))

        sns.histplot(df['salary'], bins=20)

        plt.title('Salary Distribution')

        plt.tight_layout()

        plt.savefig("outputs/charts/salary_distribution.png")

        plt.close()

    # -----------------------------
    # Age Distribution
    # -----------------------------

    if 'age' in df.columns:

        plt.figure(figsize=(8, 5))

        sns.histplot(df['age'], bins=20)

        plt.title('Employee Age Distribution')

        plt.tight_layout()

        plt.savefig("outputs/charts/age_distribution.png")

        plt.close()

    print("Charts saved in outputs/charts/")