__author__ = 'chifeng'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import *
from dateutil.parser import *
import matplotlib.dates as mdates

import sys

print 'pandas.__version__ is ', pd.__version__
# print 'matplotlib.__version__ is ', matplotlib.__version__

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


fig, ax = plt.subplots(1, 1, figsize=(15, 3))
fig2, ax1 = plt.subplots(1, 1, figsize=(10, 10))

path = "./postEvent.csv.out.csv"
csv = pd.read_csv(path)


# fromtimestamp() accepts timestamp in seconds and add tz to it.
# utcfromtimestamp() doesn't add tz.
utc = csv.eventUTCTime.apply(
    lambda x: datetime.utcfromtimestamp(x / 1000))  # Series
csv['DatetimeUTC'] = utc

cat = csv.loc[:, ['DatetimeUTC', 'category']]  # DataFrame


'''
#cc = cat.category.values
cat4 = cat[cat.category == 4]

s = pd.Series(data=cat4.category.values, index=cat4.DatetimeUTC)
d = pd.DataFrame(s)
ax.scatter(d.index, d[0], marker='v', c='r')
#plot_date(cat.DatetimeUTC.astype(datetime), cat.category )
#cat.plot(kind='scatter', x='DatetimeUTC', y='category', ax=ax)
#cat.plot(x='DatetimeUTC', y='category', ax=ax, style='v--')

catE = cat[cat.category != 4]
sE = pd.Series(data=catE.category.values, index=catE.DatetimeUTC)
dE = pd.DataFrame(sE)
ax.scatter(dE.index, dE[0], c='b')
'''
def draw(df, i, ax):
    cat = None
    if i < 0:
        cat = df
    else:
        cat = df[df.category == i]
    s = pd.Series(data=cat.category.values, index=cat.DatetimeUTC)
    d = pd.DataFrame(s)
    ax.scatter(d.index, d[0], marker='v', c='b')

draw(cat, -1, ax)

ax.yaxis.grid()
ax.yaxis.set_ticklabels(category.values()[1:])

csz = range(len(category))
for i in csz:
    csz[i] = len(cat.category[cat.category == i])

catz = pd.Series(csz, index=category.values())
catz.plot(kind='pie', ax=ax1)










# date2num() returns a float since 0001-01-01 00:00:00 UTC *plus* *one*.
#t = csv.eventUTCTime.apply(
#    lambda x: mdates.date2num(datetime.utcfromtimestamp(x / 1000)))  # Series
# dat = pd.DataFrame({'category': cat.category, 'utc': t})
# plt.plot_date(dat.utc, dat.category, fmt="bo", tz=None, xdate=True)




