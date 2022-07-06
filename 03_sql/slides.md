[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)
### Practical Data Science with Python
# 3. SQL and Built-in File Handling with Python

[comment]: # (!!!)

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



[comment]: # (!!!)

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

## SQL
- "Structured Query Language" for relational data
- On PostgreSQL, MySQL, Oracle, MS SQLServer, etc.

| `property_id` | `zoned`      | `sale_price` |
|---------------|-------------|---------------
|9329           |"residential"| 343433.34    |
|3294           |"commercial" | NULL         |
|9299           |"commercial" | 239920000.00 |


[comment]: # (!!!)

## Types

Common: numbers, strings, dates/times, booleans

`NULL` means no-value

Constraints: Not-NULL, unique, always in some set

Primary keys: Not-null and unique

| `property_id` | `zoned`      | `sale_price` |
|---------------|-------------|---------------
|9329           |"residential"| 343433.34    |
|3294           |"commercial" | NULL         |
|9299           |"commercial" | 29920000.00 |

[comment]: # (!!!)

## SQLite
- Not networked! A library and a file format
- Free, very fast, very reliable, ubiquitous
- `sqlite3` is the command-line shell

```
$ sqlite3  mydata.db
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

## SELECT

```sql
sqlite> SELECT property_id, zoned WHERE sale_price > 500000;

9299|commercial

sqlite> SELECT * WHERE sale_price IS NULL;

3294|commercial|NULL

sqlite> SELECT UNIQUE zoned ORDER BY zoned;

commercial
residential
```
[comment]: # (!!!)


## SELECT (aggregates)

```sql
sqlite> SELECT count(*);
3

sqlite> SELECT avg(sale_price), max(sale_price), min(sale_price)
    FROM property;
12031716.67|343433.34|29920000.00

sqlite> SELECT sum(amount) 
	WHERE account = 2313 AND type = 'debit';
39898.12
```
[comment]: # (!!!)

## GROUP BY

```
sqlite> .schema Album
CREATE TABLE [Album]
(
    [AlbumId] INTEGER  NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
	...
);

sqlite> SELECT ArtistID, count(*) as album_count 
	FROM Album 
	GROUP BY ArtistId 
	ORDER BY album_count DESC LIMIT 5;
90|21
22|14
58|11
50|10
150|10
```
[comment]: # (!!!)

## JOIN

```
sqlite> .schema ARTIST
CREATE TABLE [Artist]
(
    [ArtistId] INTEGER  NOT NULL,
    [Name] NVARCHAR(120),
    CONSTRAINT [PK_Artist] PRIMARY KEY  ([ArtistId])
);
sqlite> SELECT Title, Name
	FROM Album INNER JOIN Artist 
		ON Album.ArtistId = Artist.ArtistID
	ORDER BY Title
	LIMIT 3;
...And Justice For All|Metallica
20th Century Masters Collection: Best of Scorpions|Scorpions
A Copland Celebration, Vol. I|London Symphony Orchestra
```

LEFT JOIN: "If the Album has a null ArtistID, include it"
[comment]: # (!!!)

## Indexes
The Big Deal is that columns can be indexed

```
sqlite> CREATE INDEX idx_price ON property (sale_price);
sqlite> SELECT * FROM property 
	WHERE sale_price < 1000000 AND sale_price > 900000;
```

Only needed rows are read from disk!

[comment]: # (!!!)

## INSERT, UPDATE, DELETE

```
sqlite> INSERT INTO property (property_id,zoned,sale_price)
	       VALUES (5894, "residential", 480000.00);

sqlite> UPDATE property
        SET sale_price = 520000.00
        WHERE property_id = 5894;

sqlite> DELETE FROM property WHERE property_id = 5894;
```
[comment]: # (!!!)


## SQL from Python

```
import sqlite3
conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM property')
properties = cursor.fetchall()
```

[comment]: # (!!!)


# Questions?

