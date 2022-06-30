[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)
### Practical Data Science with Python
# 1. SQL and Built-in File Handling with Python

[comment]: # (!!! data-auto-animate)

## Reading text from a file

### All at once
```python
with open('textfile.txt', 'r') as f:
	text = f.read()
	
# text is one long string
print(text)
```
### One line at a time

```python
with open('textfile.txt', 'r') as f:
	for line in f:
		print(line)
```



[comment]: # (!!! data-auto-animate)

## Writing strings to a file

```python
dog_count = 3
with open('textfile.txt', 'w',  newline='\n') as f:
	print(f"There are {dog_count} dogs.", file=f)
	print(f"{dog_count * 2} is twice as many.", file=f)

```
- `newline=`
	- Unix: `\n`
	- Windows: `\r\n`
- `encoding=`
	- `utf-8`


[comment]: # (!!!)

## JSON

```json
{
'books':12, 
'articles':100, 
'subjects':['math', 'programming', 'data science']
}
```

[comment]: # (!!!)

## JSON

### Writing
```python
import json

library = {'books':100, 'sections':['fiction', 'nonfiction']}

with open('jsonfile.json', 'w') as f:
	json.dump(library, f, indent=2)
```

### Reading
```python
import json
with open('jsonfile.json', 'r') as f:
	library = json.load(f)
	
# library is dict
print(library)
```


[comment]: # (!!! data-auto-animate)

## Pickle files


### Writing
```python
import pickle as pk

library = {'books':100, 'sections':['fiction', 'nonfiction']}

with open('myfile.pkl', 'wb') as f:
	pk.dump(library, f)
```

### Reading
```python
import pickle as pk

with open('myfile.pkl', 'rb') as f:
	library = pk.load(f)
```

[comment]: # (!!!)

### SQL
- "Structured Query Language" for relational data
- On PostgreSQL, MySQL, Oracle, MS SQLServer, etc.
- Data can be **indexed**

| `property_id` | `zoned`      | `sale_price` |
|---------------|-------------|---------------
|9329           |"residential"| 343433.34    |
|3294           |"commercial" | NULL         |
|9299           |"commercial" | 239920000.00 |


[comment]: # (!!!)

#### Types

Common: numbers, strings, dates/times, booleans

`NULL` means no-value

Constraints: Not-NULL, unique, always in some set

Primary keys: Not-null and unique

| `property_id` | `zoned`      | `sale_price` |
|---------------|-------------|---------------
|9329           |"residential"| 343433.34    |
|3294           |"commercial" | NULL         |
|9299           |"commercial" | 239920000.00 |

[comment]: # (!!!)

### SQLite
- Not networked! A library and a file format
- Free, very fast, very reliable, ubiquitous
- `sqlite3` is the command-line shell

```sh
$ sqlite3 chinook.db
sqlite> .tables
employee   department   project

sqlite> CREATE TABLE property (
   property_id INT PRIMARY KEY NOT NULL,
   zoned TEXT NOT NULL,
   sale_price REAL,
);
sqlite> .quit
```

[comment]: # (!!!)

# Questions?

