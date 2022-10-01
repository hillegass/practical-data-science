[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 10. Feature Engineering

[comment]: # (!!!)

## Review Standardization

```python
# Get the mean and std for each column
means = X.mean(axis=0)
std = X.std(axis=0)
Xp = (X - means) / std
```

[comment]: # (!!!)

## Reshaping arrays into a column

```python
x = np.array([[1,2],[3,4]])
# array([[1, 2],
#        [3, 4]])

x2 = x.reshape(-1,1)
# array([[1],
#        [2],
#        [3],
#        [4]])
```

[comment]: # (!!!)


## Yeo-Johnson and Box-Cox

### Makes things more like normal distribution

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer()

w = df['waist'].values.reshape(-1,1)

df['t_waist'] = pt.fit_transform(w)
```

Box-cox only works on positive values

```python
df['t_waist'] = pt.fit_transform(w, method='box-cox')
```
[comment]: # (!!!)

## Combining columns

```python
df['lifetime'] = (df['death'] - df['dob']).dt.days
```

[comment]: # (!!!)

## Encoding year

```python
angles = 2 * np.pi * df['date'].dt.dayofyear / 365.0

df['season0'] = np.sin(angles)
df['season1'] = np.cos(angles)
```

(Same trick for encoding time)

[comment]: # (!!!)

## Categories with order

| shirt_id | size    |
|--------|----------|
| 1      | 'S'    |
| 2      | 'L'  | 
| 3      | 'M'    | 
| 4      | 'XL' |
| 5      | 'XS' |

[comment]: # (!!!)

## LabelEncoder

```python
from sklearn.preprocessing import LabelEncoder

le = preprocessing.LabelEncoder()
le.fit(['XS','S','M','L','XL'])

shirts['size_index'] = le.transform(shirts['size'])

| shirt_id | size | size_index |
|--------|--------|------------|
| 1      | 'S'    | 2
| 2      | 'L'  | 4
| 3      | 'M'    | 3
| 4      | 'XL' | 5
| 5      | 'XS' | 1

sizes = le.inverst_transform([1,2,3])
# ['XS','S','M']
```
[comment]: # (!!!)


## Categories with no order

| car_id | color    |
|--------|----------|
| 1      | 'red'    |
| 2      | 'green'  | 
| 3      | 'red'    | 
| 4      | 'orange' |

[comment]: # (!!!)

## One-hot encoding

```python
car_colors = pd.get_dummies(cars['color'])
cars = pd.concat([cars, car_colors], axis=1)
```

| car_id | green | orange | red |
|--------|-------|--------|-----|
| 1      | 0     | 0   | 1      |
| 2      | 1     | 0   | 0      |
| 3      | 0     | 0   | 1      |
| 4      | 0     | 1     | 0    |


[comment]: # (!!!)

## Clipping outliers

### Always questionable!

```python
df['height'].clip(upper=3.0, inplace=True)
```
[comment]: # (!!!)

# Questions?

