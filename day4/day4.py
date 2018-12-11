import re
from collections import defaultdict
from datetime import datetime


def parse_datetime(event_str):
    datetime_str = re.search(r'\[.*\]', event_str).group(0)
    return datetime.strptime(datetime_str, '[%Y-%m-%d %H:%M]')


with open('day4input.txt') as f:
    lines = [line.rstrip() for line in sorted(f.readlines())]


guards = defaultdict(int)
minutes = defaultdict(lambda: [0 for i in range(60)])

current_guard = None
start = None
for line in lines:
    event_dt = parse_datetime(line)
    if 'begins shift' in line:
        current_guard = re.search(r'\#\d+', line).group(0)
        start = None
    elif 'falls asleep' in line:
        start = event_dt.minute
    elif 'wakes up' in line:
        if start is not None:
            duration = event_dt.minute - start
            guards[current_guard] += duration
            for minute in range(start, event_dt.minute):
                minutes[current_guard][minute] += 1
        else:
            print('WAKING BEFORE SLEEPING')

guards = sorted(guards.items(), key=lambda x: x[1], reverse=True)
print(f'Most sleep: {guards[0][0]}')
print(minutes[guards[0][0]].index(max(minutes[guards[0][0]])))

max_id = 0
max_minute = 0
for g_id, minute_list in minutes.items():
    if max_minute < max(minute_list):
        max_id = g_id
        max_minute = max(minute_list) 
print(f'{max_id}, {minutes[max_id].index(max_minute)}')
print(minutes)
