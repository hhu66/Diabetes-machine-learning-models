import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.


## YOUR CODE HERE ##
morg_df = pd.read_csv(r"C:\Users\momom\Desktop\TT7_data\data\morg_d07_strings.csv")
morg_df = morg_df.set_index('h_id')

#Set the maximum numbers of rows and columns you see in your IPython session
pd.options.display.max_columns = 15
pd.options.display.max_rows = 20

# TASKS 2-6
# For each of the tasks, print the value requested in the task.

## YOUR CODE HERE ##
print(morg_df['age'])
print(morg_df[morg_df.index =='1_2_2'])
print(morg_df.iloc[0:4])

any(morg_df.loc[:, "hours_worked_per_week"].isna()) #True
any(morg_df.loc[:, "age"].isna()) #False

columns = morg_df.columns
columns_missing_value =[]

for i in columns:
    if morg_df[i].isna().any():
        columns_missing_value.append(i)

print(columns_missing_value)

morg_df[columns_missing_value].fillna(value=0)


### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

## YOUR CODE HERE ##
morg_df[TO_CATEGORICALS] = morg_df[TO_CATEGORICALS].astype('category')

# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##
hours_boundaries = range(0,99+1,10)
morg_df.loc[:,'hwpw_bin'] = pd.cut(morg_df.loc[:,"hours_worked_per_week"],
                             bins=boundaries,
                             labels=range(len(boundaries)-1),
                             include_lowest=True, right=False)
print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13
print(morg_df[morg_df['hours_worked_per_week'] >= 35])
print(morg_df[morg_df['employment_status'] != 'Working'])
print(morg_df[(morg_df['hours_worked_per_week'] >= 35) | (morg_df['earnings_per_week'] > 1000)])

race_counts = morg_df['race'].value_counts().sort_values(ascending=False)
print(race_counts.head())

race_groups = morg_df.groupby('race').size()
print(race_groups)

### Task 14

students = pd.read_csv(r"C:\Users\momom\Desktop\TT7_data\data\students.csv")
extended_grades = pd.read_csv(r"C:\Users\momom\Desktop\TT7_data\data\extended_grades.csv")

grades_major_count = pd.merge(students, extended_grades, on='UCID', how='inner')
print(grades_major_count.groupby(['Grade','Major']).size().reset_index())
