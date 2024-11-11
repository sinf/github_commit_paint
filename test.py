from datetime import datetime, timedelta
import subprocess
import os

from paint import paint

def run_script(ts):
    return not paint(datetime.fromtimestamp(ts))

def render(title, t0, n_cols):
    while t0.weekday() != 6:
        t0 = t0 - timedelta(days=1)
    t0 = t0.replace(hour=12, minute=0)
    print(title)
    for j in range(7):
        row=""
        for i in range(n_cols):
            t = t0 + timedelta(days=j, weeks=i)
            t = t.replace(hour=12, minute=0)
            ts = int(t.timestamp())
            row += '#' if run_script(ts) == 0 else ' '
        row += ';'
        print(row)
    print()

render("now", datetime.now(), 80)
render("end of year", datetime(2024, 12, 20), 80)
render("end of next year", datetime(2025, 12, 20), 80)

