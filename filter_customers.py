import sys
import pandas as pd
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python filter_customers.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    try:
        df = pd.read_csv(file_path)

        required_columns = {"customer_name", "customer_salary"}
        if not required_columns.issubset(df.columns):
            print(
                "Error: CSV must contain 'customer_name' and 'customer_salary' columns")
            return

        df["customer_salary"] = (
            df["customer_salary"]
            .replace(r"[\$,]", "", regex=True)
            .astype(float)
        )

        filtered_df = df[df["customer_salary"] > 10000]

        print("\nCustomers with salary > 10000:\n")
        print(filtered_df[["customer_name", "customer_salary"]])

    except FileNotFoundError:
        print("Error: File not found")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
