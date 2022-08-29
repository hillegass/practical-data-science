[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 1C. Table Problems and Workarounds

[comment]: # (!!!)

## Missing values

There is no value for a particular cell.

Workarounds:

1. Drop the row
2. Impute or interpolate the value
3. Go back to the source to get value


[comment]: # (!!!)

## Dropping
```
df2 = df.dropna(subset=['height', 'width'])
```

[comment]: # (!!!)

## Filling

```python
df['height'].fillna(1.5, inplace=True)
```

[comment]: # (!!!)

## Linear interpolation
```
                                temps
2022-08-20 17:08:36.382917  11.348178
2022-08-20 19:08:36.382917        NaN
2022-08-21 01:08:36.382917  18.282991
...                               ...
2022-10-02 15:08:36.382917  18.944569
2022-10-02 18:08:36.382917        NaN
2022-10-02 22:08:36.382917        NaN
2022-10-03 01:08:36.382917  14.129328

df2 = df.interpolate(method='time')

2022-08-20 17:08:36.382917  11.348178
2022-08-20 19:08:36.382917  13.081881
2022-08-21 01:08:36.382917  18.282991
...                               ...
2022-10-02 15:08:36.382917  18.944569
2022-10-02 18:08:36.382917  17.499997
2022-10-02 22:08:36.382917  15.573900
2022-10-03 01:08:36.382917  14.129328
```

[comment]: # (!!!)

## Imputing

```
df['price'].fillna(df['price'].mean(), inplace = True)
```

[comment]: # (!!!)


## Bad format

Supposed to be a date, cell says "78".

Workarounds:

1. Figure out how to parse it
2. Drop the row
2. Impute the value
3. Go back to the source to get value

[comment]: # (!!!)


## Incorrect Category

Value can be "S" or "L", cell contains "M"

Workarounds:

1. Drop the row
2. Add new category
3. Change to reasonable category
4. Go back to the source to get value


[comment]: # (!!!)

## Out-of-range

Height should be in range 1 - 3, cell contains 0.4

Workarounds:

1. Drop the row
2. Project into range
3. Extend the range
4. Go back to the source to get value


[comment]: # (!!!)

## Not unique

Two car records have the same VIN.

Workarounds:

1. Merge them
2. Discard both

[comment]: # (!!!)

## Inconsistent

A vehicles max_cargo is 12.  

Its current_cargo is 17.

Workarounds:

1. Discard row
2. Ignore inconsistency 
3. Make consistent

[comment]: # (!!!)


## Referential Problem

Employee has department 23.  

There is no Department 23.

(Usual cause: Dept 23 was deleted.)

Delete rules for departments:

1. Cascade - Delete everyone in the department
2. Nullify - Everyone gets null department ID
3. Deny - You can only delete empty departments


[comment]: # (!!!)

# Questions?


