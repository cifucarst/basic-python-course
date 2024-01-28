#!/usr/bin/env python3

import datetime

# Current date and time
now = datetime.datetime.now()

# Specific time
specific_time = datetime.time(14, 15, 15)
print(specific_time)

# Specific date
specific_date = datetime.date(2023, 6, 14)
print(specific_date)

# Specific date and time
date_time = datetime.datetime(2023, 6, 12, 14, 15, 15)

#################################################

# Current date and time components
current_date = datetime.datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day
hours = current_date.hour
minutes = current_date.minute
seconds = current_date.second

# Displaying date and time components
print(f'Year: {year}, Month: {month}, Day: {day}, Time: {hours}:{minutes}:{seconds}')