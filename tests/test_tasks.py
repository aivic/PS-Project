# Importing libraries
import pytest
from utils import get_calls, get_assignments
import sys

sys.path.insert(1, '../')

from tasks import solution

# -------------------------------------------------
# Pytest for Task 1
# Importing the `pandas` library with an alias `pd`

@pytest.mark.test_task1
def test_task1():
    assert 'pd' in dir(solution), 'Have you imported the`pandas` library with an alias as `pd`?'
    
# -------------------------------------------------
# Pytest for Task 2
# Loading the CSV file in a variable `df` using the `pd.read_csv()` method.

@pytest.mark.test_task2
def test_task2():
    assert get_calls(solution)[0] == 'pd:read_csv:../data/student_db.csv', 'Have you loaded the CSV file using the `pd.read_csv()` method with proper arguments?'
    assert get_assignments(solution)[0][:2] == 'df', 'Has the `df` DataFrame been created?'    

# -------------------------------------------------
# Pytest for Task 3
# Finding the median of the `GRADE` column and storing the result in the `grade_median` variable.

@pytest.mark.test_task3
def test_task3():    
    assert get_assignments(solution)[1][:12] == 'grade_median', 'Has the `grade_median` variable been created?'    
    assert solution.grade_median == 7.25, 'You can use the `df.GRADE.median()` call to calculate the correct median.'