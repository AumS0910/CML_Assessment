import pandas as pd
import unittest


class TestSalaryFilter(unittest.TestCase):

    def test_salary_filter(self):
        data = {
            "customer_name": ["A", "B", "C"],
            "customer_salary": ["$9000", "$15000", "$20000"]
        }

        df = pd.DataFrame(data)

        df["customer_salary"] = (
            df["customer_salary"]
            .replace(r"[\$,]", "", regex=True)
            .astype(float)
        )

        filtered = df[df["customer_salary"] > 10000]

        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered.iloc[0]["customer_name"], "B")


if __name__ == "__main__":
    unittest.main()
