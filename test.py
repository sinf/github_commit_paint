#!/usr/bin/python3
from datetime import datetime, timedelta
import os

from paint import paint

def render(title, t0, n_cols):
    offset_today = 0
    while t0.weekday() != 6: # seek to sunday
        t0 = t0 - timedelta(days=1)
        offset_today += 1
    t0 = t0.replace(hour=12, minute=0)
    print(title)
    for j in range(7):
        row=""
        for i in range(n_cols):
            t = t0 + timedelta(days=j, weeks=i)
            t = t.replace(hour=12, minute=0)
            full, empty = '#', ' '
            if  (i*7 + j) - offset_today == 0:
                full, empty = '/', '.'
            row += full if paint(t) else empty
        row += ';'
        print(row)
    print()

os.environ['TZ'] = 'UTC'
render("now", datetime.now(), 80)
render("end of year", datetime(2024, 12, 20), 80)
render("end of next year", datetime(2025, 12, 20), 80)

