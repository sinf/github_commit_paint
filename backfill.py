#!/usr/bin/python3
from datetime import datetime, timedelta
import subprocess
import os

from paint import paint

def commit(t):
    if paint(t):
        for _ in range(5):
            d = t.isoformat(timespec='seconds')
            t = t + timedelta(seconds=1)
            opts=['/usr/bin/git', 'commit', '--date', d, '--allow-empty', '-m', 'commit']
            print(opts)
            subprocess.run(opts, stdout=subprocess.DEVNULL)
    else:
        print(t.isoformat(timespec='seconds'), '-')

def date_range(t0, count):
    for i in range(count):
        t = (t0 - timedelta(days=i)).replace(hour=12, minute=0)
        commit(t)

os.environ['TZ'] = 'UTC'
date_range(datetime.now(), 40*7)


