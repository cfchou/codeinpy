__author__ = 'chifeng'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import *
from dateutil.parser import *
import matplotlib.dates as mdates

import sys

print 'pandas.__version__ is ', pd.__version__
#print 'matplotlib.__version__ is ', matplotlib.__version__

category = {
    0: '\"UNKNOWN\"',
    1: '\"LOG_FILE\"',
    2: '\"SYSTEM\"',
    3: '\"DEVICE\"',
    4: '\"MEDIA\"',
    5: '\"ACCESSIBILITY\"',
    6: '\"ICS_CTRL\"',
    7: '\"VEHICLE_STATE\"',
    8: '\"ONSTAR\"',
    9: '\"HVAC\"'
}

def datetimeToMillies(d):
    epoch = datetime.utcfromtimestamp(0)
    # timedelta.total_seconds() return a float
    return (d - epoch).total_seconds() * 1000.0

fig, ax = plt.subplots(1, 1, figsize=(15, 5))

path = "./postEvent.csv.out.csv"
csv = pd.read_csv(path)


# fromtimestamp() accepts timestamp in seconds and add tz to it.
# utcfromtimestamp() doesn't add tz.
utc = csv.eventUTCTime.apply(
    lambda x: datetime.utcfromtimestamp(x / 1000))  # Series
csv['DatetimeUTC'] = utc

cat = csv.loc[:, ['DatetimeUTC', 'category']]  # DataFrame
cat.plot(kind='scatter', x='DatetimeUTC', y='category', ax=ax)
#cat.plot(x='DatetimeUTC', y='category', ax=ax, style='v--')
ax.yaxis.grid()
ax.yaxis.set_ticklabels(category.values())

rng1 = pd.date_range('1/1/2011', periods=10, freq='H')
rng2 = pd.date_range('2/1/2011', periods=10, freq='H')



# date2num() returns a float since 0001-01-01 00:00:00 UTC *plus* *one*.
#t = csv.eventUTCTime.apply(
#    lambda x: mdates.date2num(datetime.utcfromtimestamp(x / 1000)))  # Series
# dat = pd.DataFrame({'category': cat.category, 'utc': t})
# plt.plot_date(dat.utc, dat.category, fmt="bo", tz=None, xdate=True)




