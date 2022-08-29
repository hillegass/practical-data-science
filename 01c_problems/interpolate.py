import pandas as pd
import numpy as np
import datetime
import math
import random
import matplotlib.pyplot as plt

now = datetime.datetime.now()
current_time = now
timestamps = []
temperatures = []

for i in range(300):
    timestamps.append(current_time)
    hour_hop = random.randint(1, 6)
    current_time = current_time + datetime.timedelta(hours=hour_hop)
    if random.random() < 0.2:
        temperatures.append(np.nan)
    else:
        seconds_passed = (current_time - now).total_seconds()
        temperatures.append(10.0 + 15.0 * math.sin(seconds_passed/ 80000.00))

df = pd.DataFrame({'temps':temperatures}, index=timestamps)
print(df)
df2 = df.interpolate(method='time')
print(df2)

# plt.plot(df.index, df['temps'], 'b')
plt.plot(df2.index, df2['temps'], 'b')

plt.show()
