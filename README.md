# Customer Salary Filter - Python CLI Tool
This Python script filters customers with salaries greater than $10,000 from a CSV file.

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


## Additional Filters That Can Be Added
- Filter by job category
- Filter by city or state
- Filter by salary range (min & max)
- Sort customers by salary

## Unit Tests
Unit tests are added using Python assertions to validate:
- Salary cleaning logic
- Salary filtering correctness


## How to Run the Program

```bash
python filter_customers.py data/customer_100.csv