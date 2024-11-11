from datetime import datetime, timedelta
import os

data=(
    "                                      ",
    "# #    # #       #   #        #   #   ",
    "# # ## # #       #   #        #   #   ",
    "# # #  # #       #   #        #   #   ",
    "### ## # # ###   # # # ### ## # ###   ",
    "# # #  # # # #   # # # # # #  # # #   ",
    "# # ## # # ###   ## ## ### #  # ###   ",
)
assert all( len(row) == len(data[0]) for row in data )
assert len(data) == 7

def get_week_nr(t):
    t=t.replace(hour=12, minute=0)
    d0=datetime(2024, 9, 29)
    return (t-d0).days//7
    #from dateutil import rrule as r
    #return r.rrule(r.WEEKLY, dtstart=d0, until=t).count()
    sun=d0
    d=d0
    n=0
    while d < t:
        d += timedelta(days=1)
        if d.weekday() == 6:
            sun=d
            n+=1
    return n

def read_value(row, col):
    return 1 if data[row][col] == '#' else 0

def paint(t):
    t = t.replace(hour=12, minute=0)
    row = ( t.weekday() + 1 ) % 7 # on github, sunday=0
    col = get_week_nr(t) % len(data[0])
    x = read_value(row, col)
    return x

def main():
    t = datetime.now()
    x = paint(t)
    # inverted return value;
    # if python dies to exception, dont commit
    exit(0 if x else 1)

if __name__=="__main__":
    main()

