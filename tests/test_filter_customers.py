import unittest
import pandas as pd
from src.filter_customers import clean_salary_column, filter_high_salary_customers


class TestSalaryFilter(unittest.TestCase):

    def test_salary_filter(self):
        data = {
            "customer_name": ["A", "B", "C"],
            "customer_salary": ["$9000", "$15000", "$20000"]
        }

        df = pd.DataFrame(data)
        df = clean_salary_column(df)
        result = filter_high_salary_customers(df)

        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["customer_name"], "B")


if __name__ == "__main__":
    unittest.main()
