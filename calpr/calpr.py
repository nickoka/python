"""
calpr.py: Prints the calendar for a specific month

Authors: Nick Oka

CIS 210 Assignment 3

Limitations: Treats February as always having 28 days. 
Usage: python calpr.py month year
"""

import argparse
import datetime # To determine what day of week a month
				# begins on.  
# Note: For this project, module calendar
# is not permitted.  It basically has a function
# to do the whole assignment in one line. 

MONTHLEN = [ 0, # No month zero
	31, # 1. January
	28, # 2. February (ignoring leap years)
	31, # 3. March
	30, # 4. April
	31, # 5. May
	30,	# 6. June
	31, # 7. July
	31, # 8. August
	30, # 9. September
	31, #10. October
	30, #11. November
	31, #12. December
	]

parser = argparse.ArgumentParser(description="Print calendar")
parser.add_argument("month", type=int, 
                        help="Month number (1-12)")
parser.add_argument("year", type=int, 
                        help="Year (1800-2525)")
args = parser.parse_args()  # gets arguments from command line
month = args.month
year = args.year


# What day of the week does year,month begin on? 
a_date = datetime.date(year, month, 1)
starts_weekday = a_date.weekday()
## a_date.weekday() gives 0=Monday, 1=Tuesday, etc.
## Roll to start week on Sunday
starts_weekday = (1 + starts_weekday) % 7  


month_day = 1   			## Next day to print
last_day = MONTHLEN[month]  ## Last day to print

print(" Su Mo Tu We Th Fr Sa")
###
###  The first (perhaps partial) week
###
for i in range(7):
	if i < starts_weekday :
		print("   ", end="")
	else:
		# Logic for printing one day, moving to next
		print(format(month_day, "3d"), end="")
		month_day += 1
print() # Newline

while (month_day + 6) < last_day:
        for i in range(7):
                #Logic for printing one day, moving to next
                print(format(month_day, "3d"), end="")
                month_day += 1
        print() # Newline
###
### The last (perhaps partial) week
###
for i in range ((last_day + 1) - month_day):
        print(format(month_day, "3d"), end="")
        month_day += 1
print() #Newline	
	
