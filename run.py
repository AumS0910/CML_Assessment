import sys
import os
import logging
from src.filter_customers import (
    read_csv,
    validate_columns,
    clean_salary_column,
    filter_high_salary_customers
)
from src.constants import LOG_FORMAT
from src.exceptions import InvalidCSVError


logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def main():
    if len(sys.argv) != 2:
        logger.error("Usage: python run.py <csv_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        logger.error("File not found: %s", file_path)
        sys.exit(1)

    try:
        df = read_csv(file_path)
        validate_columns(df)
        df = clean_salary_column(df)
        filtered_df = filter_high_salary_customers(df)

        logger.info("Filtered %d records", len(filtered_df))
        print(filtered_df[["customer_name", "customer_salary"]])

    except InvalidCSVError as e:
        logger.error("Validation error: %s", e)
    except Exception as e:
        logger.exception("Unexpected error occurred")


if __name__ == "__main__":
    main()
