# Setup

## Create Virtual Environment

In a terminal run the following commands from the root folder of the forked project.

```
python -m venv venv
```

Once that completes, also run this command from the same folder.

Windows

```
venv\Scripts\activate.bat
```

macOS & Linux

```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We’ll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

# Working on tasks
## Task 1: Importing Pandas Library
**`@pytest.mark.test_task1`** In order to start working with the project, load the `pandas` library with an alias `pd` at the top of the `tasks/solution.py` file.

## Task 2: Importing the CSV dataset
**`@pytest.mark.test_task2`** Next, in the same file load the dataset `student_db.py` from the `data` directory using the `pd.read_csv()` method and store the Pandas DataFrame in the `df` variable.

## Task 3: Finding the Median of the GRADE column
**`@pytest.mark.test_task3`** To fill the missing values in the GRADE column, find the median of the complete column using the `median()` function and store the result to a variable `grade_median`. 

