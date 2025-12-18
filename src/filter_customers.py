import pandas as pd
import logging
from src.constants import SALARY_THRESHOLD, REQUIRED_COLUMNS, LOG_FORMAT
from src.exceptions import InvalidCSVError


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file from the provided file path and returns
    its contents as a Pandas DataFrame.

    This function assumes the file is a valid CSV file
    readable by pandas.

    Args:
        file_path (str): Absolute or relative path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.

    Raises:
        FileNotFoundError: If the file path does not exist.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV is malformed.
    """
    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame) -> None:
    """
    Validates that the required columns are present in the DataFrame.

    This ensures downstream processing does not fail due to
    missing or incorrect column names.

    Args:
        df (pd.DataFrame): DataFrame to validate.

    Raises:
        InvalidCSVError: If required columns are missing.
    """
    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise InvalidCSVError(
            f"CSV must contain the following columns: {REQUIRED_COLUMNS}"
        )


def clean_salary_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and converts the salary column to a numeric float value.

    This function removes currency symbols and formatting characters
    before converting the column to float.

    Args:
        df (pd.DataFrame): Input DataFrame containing salary data.

    Returns:
        pd.DataFrame: DataFrame with cleaned numeric salary values.

    Raises:
        ValueError: If salary values cannot be converted to float.
    """
    df["customer_salary"] = (
        df["customer_salary"]
        .replace(r"[\$,]", "", regex=True)
        .astype(float)
    )
    return df


def filter_high_salary_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters and returns customers whose salary exceeds
    the configured salary threshold.

    Args:
        df (pd.DataFrame): DataFrame containing customer data.

    Returns:
        pd.DataFrame: Filtered DataFrame with high-salary customers only.
    """
    return df[df["customer_salary"] > SALARY_THRESHOLD]
