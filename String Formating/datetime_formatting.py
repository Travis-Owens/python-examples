# Author:   @Travis-Owens
# Date:     2019-2-1
# Purpose:  Demonstrate how to format datetime.now() using strftime()

from datetime import datetime #import the datetime class from the datetime library

# Retrieve the current time from the datetime.now() function
now = datetime.now()  #Example output: 2019-02-01 09:50:40.806669

# Using strftime() - String Format Time, a built-in python module
# Used formatting codes in this example:
#           %Y = year
#           %m = month
#           %d = day
#           %H = Hour
#           %M = minute
#           %S = second
#           %a = abbreviated day name. Ex. Mon
#           %A = Day name. Ex. Monday
#           For a full list of codes check out: https://www.programiz.com/python-programming/datetime/strftime#format-code

# Now format current_date_time and remove millisecond value.
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Date and Time: ", date_time)      # Example output: "Date and Time: 2019-02-01 10:02:53"

# Extract just the year
year = now.strftime("%Y")
print("year: ", year)            # Example output: "Year: 2019"

# Extract just the month
month = now.strftime("%m")
print("Month: ", month)          # Example output: "Month: 02"

# Extract just the day
day = now.strftime("%d")        # Example output: "Day: 15"
print("Day: ", day)

# Extract the hour, minute, and second. Then format into H:M:S
time = now.strftime("%H:%M:%S")
print("Time: ", time)           # Example output: "Time: 12:45:23"

day_of_the_week = now.strftime("%A")
print("Day of the week: ", day_of_the_week)         # Example output: "Day of the week: Friday"
