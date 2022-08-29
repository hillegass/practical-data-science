[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python
# 4. Loading and Wrangling Data with pandas and NumPy 

[comment]: # (!!!)

## CSV (comma separated values)

```
employee_id,gender,height,waist,salary,dob,death
4782566,m,1.82,1.11,74917.00,1961-11-18,1986-10-21
1427930,m,1.73,1.11,63012.00,1946-03-18,1972-09-13
8880433,f,1.68,0.93,86437.00,1978-08-14,2012-08-09
```
### Read in data frame
```
import pandas as pd
df = pd.read_csv('employees.csv', index_col='employee_id')
```
### Show the shape of the dataframe
```
(row_count, col_count) = df.shape
print(f"Rows: {row_count}") # Shows 6!
print(f"Columns: {col_count}")
```
[comment]: # (!!!)

## pandas supported file types
- CSV
- Excel
- JSON
- XML
- HTML
- HDF5
- SQL databases
[comment]: # (!!!)

## Series

### Get column as a Series
```
salary_series = df['salary']
salary_series.mean()
```

### Get row as series:
```
an_employee = df.loc[4782566]
first_employee = df.iloc[0]
```
[comment]: # (!!!)
 
 
## When data is too big (1)

### Work with just the columns you need
```
df = pd.read_csv('e.csv', index_col='employee_id', 
                  usecols=['waist', 'height'])
```

### No pandas – process one row at a time:
```
import csv

with open('e.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) 
    
    next(csvreader)
    for row in csv_reader:
		…
```

[comment]: # (!!!)


## When data is too big (2)


### Use indexed files (SQL, HDF5). 
```
# Read just the rows you need:
df = pd.read_hdf('my.h5', 'results_table', where='age < 18')
```
[comment]: # (!!!)

## NumPy?

- n-dimensional arrays of numbers
- Common linear algebra and statistics functions
- Very fast (for Python)
- Data representation for scikit-learn and pandas
- Can use GPU
- Fixed size

```
import numpy as np
mymatrix = np.array([[1, 2, 3], [3, 4, 5]])
myshape = mymatrix.shape # (2,3)
mytype = mymatrix.dtype  # int64
```

[comment]: # (!!!)

## pandas dataframe has np array

```
import pandas as pd
import numpy as np


df = pandas.whatever() # Make a dataframe
a = df.values
```
[comment]: # (!!!)

## Handy numpy methods

```
p = myarray[0, 2]      # indexing
q = myarray[1:, 1:]    # grabbing slices
r = myarray[-1, -1]    # -1 means "last"
t = myarray.T          # transpose
```

[comment]: # (!!!)

## Linear algebra

$2 x_1 + 3 x_2 + 4 x_3 = 4$

$9 x_1 + -2 x_2 + 4 x_3 = 5$

$7 x_1 + 6 x_2 + 5 x_3 = -8$

Becomes

$\begin{bmatrix} 
2 & 3 & 4 \\\\
9 & -2 &4 \\\\
7 & 6 & 5 \end{bmatrix} 
\begin{bmatrix} 
x_1 \\\\
x_2 \\\\
x_3\end{bmatrix} = 
\begin{bmatrix} 
4 \\\\ 5 \\\\ -8
\end{bmatrix}$

[comment]: # (!!!)

## Linear algebra

$A x = b$

$x = A^{-1}b$

```python
A = np.array([[2,3,4],[9,-2,4],[7,6,5]])
A_inv = np.linalg.inv(A)
b = np.array([4,5,6])
x = A_inv @ b
```
$x_1 = 0.18954248$

$x_2 = 0.06535948$

$x_3 = 0.85620915$

[comment]: # (!!!)

## Tensors

Storing a data set in `X`, an np.array: 

- 800 images
- 1024 pixels tall
- 2048 pixels wide
- 3 channels (RGB): 

`X.shape` is (800, 1024, 2048, 3)

5 billion numbers!

[comment]: # (!!!)

## Broadcasting

`X.shape` is (800, 1024, 2048, 3)


```
Y = X + 1

a = np.array([1, 3, 7]) 
# a.shape = (3,)
Z = X + a

R = #some image (1024, 2048, 3)
W = X + R
```

[comment]: # (!!!)


# Questions?

