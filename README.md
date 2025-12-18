# Customer Salary Filter – Production-Ready Python CLI Tool

A Python command-line application that reads customer records from a CSV file, cleans and validates the data, and filters customers whose salary exceeds a configurable threshold.

This project is designed with **production-readiness** in mind, following clean code principles, proper error handling, modular design, logging, and unit testing.

---

## 📌 Problem Statement

Given a CSV file containing customer records, the program:
- Accepts the CSV file path as a command-line argument
- Reads and parses the CSV
- Filters customers where `customer_salary > 10000`
- Outputs the filtered result
- Handles edge cases gracefully

---

## 1.How do you plan to read the CSV file? Explain your choice

I used the `pandas.read_csv()` function to read the CSV file.

**Reason:**
- Pandas provides fast and reliable CSV parsing
- It handles large files efficiently
- Built-in support for data cleaning and filtering
- Vectorized operations simplify salary comparisons

Since the dataset size is moderate (~100 rows), loading the file fully into memory is safe and efficient.


## 2.Which data structure do you use to store the parsed rows?

The parsed data is stored in a **Pandas DataFrame**.

**Why DataFrame:**
- Tabular structure maps naturally to CSV data
- Easy column-based filtering
- Efficient numeric operations
- Cleaner and more readable code compared to manual parsing


## 3.Which alternative data structures could be useful, and why? Discuss trade-offs 
- **List of dictionaries:** Simple, but slower for filtering
- **Tuple:** Immutable, but not flexible for column operations
- **Set:** Useful for deduplication, not filtering
- **Dictionary:** O(1) lookups if indexed by customer ID
- **Heap/Priority Queue:** Useful for top-N salary queries
- **Tree-based structures:** Useful for sorted traversal
- **DataFrame:** Best choice for tabular filtering and analytics


## 4.How do you handle edge/error cases?
The program handles:
- Invalid file paths
- Missing required columns
- Non-numeric salary values
- Empty CSV files
- Unexpected runtime errors

Meaningful error messages are displayed to guide the user.


## Project Structure

.
├── src/
│   ├── constants.py
│   ├── exceptions.py
│   ├── filter_customers.py
│   └── utils.py
├── tests/
│   └── test_filter.py
├── data/
│   └── customer_100.csv
└── README.md



## Additional Filters That Can Be Added
- Filter by job category
- Filter by city or state
- Filter by salary range (min & max)
- Sort customers by salary


This ensures no hardcoded values are scattered across the codebase.

---

## 🧪 Unit Testing

Unit tests are written using Python’s `unittest` framework to verify:
- Salary cleaning logic
- Salary filtering behavior
- Correct handling of edge cases

### Run tests:
```bash
python -m unittest discover tests


## How to Run the Program

```bash
pip install -r requirements.txt
python run.py data/customer_100.csv