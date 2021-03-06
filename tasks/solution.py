# Task 1: Importing Pandas library
import pandas as pd


# Task 2: Reading CSV file into a Pandas DataFrame
df = pd.read_csv('data/student_db.csv')


# Task 3: Finding the median of the GRADE column
grade_median = df.GRADE.median()
