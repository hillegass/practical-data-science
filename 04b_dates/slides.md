[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python
# 4. Dates! 

[comment]: # (!!!)

## date and timedelta

```python
import datetime

dob = datetime.date(2001, 8, 24)
today = datetime.today()
age = today - today
label = dob.isoformat()
# label = '2001-08-24'

one_day_forward = datetime.timedelta(days=1)
tomorrow = today + one_day_forward
```
[comment]: # (!!!)

## Business Days

```python
import datetime
import numpy as np

july4 = datetime.date(2022,7,4)
hw = datetime.date(2022,10,31)
cal = np.busdaycalendar(holidays=[july4, hw])

start = datetime.date(2022, 3, 15)
end = datetime.date(2023, 4, 16)
bizdays = np.busday_count(start, end,bizdaycal=cal)

```
[comment]: # (!!!)

## datetime

```python
import datetime
right_now = datetime.datetime.now()
right_now.isoformat()
# '2022-08-24T11:10:48.328059'
datetime.datetime.now().isoformat(timespec="minutes")
# '2022-08-24T11:10:48'
moon_landing = datetime.datetime(1969,7,20,20,17)
time_since = right_now - moon_landing
# (days=19392, seconds=54103, microseconds=762013)
```
[comment]: # (!!!)

## strftime and strptime
```
label = right_now.strftime('%A, %B %d')
# label = 'Wednesday, August 24'

ts = datetime.datetime.strptime
  ('Aug 24, 2022 at 11:14 PM', '%b %d, %Y at %I:%M %p')
# datetime.datetime(2022, 8, 24, 23, 14)
```
[comment]: # (!!!)

## Dates and dataframes
```python
import pandas as pd
df = pd.DataFrame({'days':['Aug 24, 2002', 'May 2, 2005'])
#           days
# 0  Aug 24, 2002
# 1   May 2, 2005

df['dates'] = pd.to_datetime(df['days'], format='%b %d, %Y')

df['since'] = datetime.datetime.now() - df['dates']

           days      dates                     since
# 0  Aug 24, 2002 2002-08-24 7305 days 11:41:48.202178
# 1   May 2, 2005 2005-05-02 6323 days 11:41:48.202178

```
[comment]: # (!!!)

## Timezones

DO EVERYTHING IN UTC

```
import pytz
local_tz = pytz.timezone('Europe/Moscow')
now = datetime.datetime.utcnow()
local_dt = now.replace(tzinfo=pytz.utc).astimezone(local_tz)
label = local_dt.isoformat(timespec='minutes')
# '2022-08-24T18:53+03:00'
```

[comment]: # (!!!)

# Questions?