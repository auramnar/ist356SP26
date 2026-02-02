'''
use the `datetime` module to:

parse a string like this "Month/Day/Year" 1/15/2025 into a datetime
then print it like this: YYYY-MM-DD

For example in the current date is January 15, 2025 the output should be 2025-01-15

You will need to read through the module with `dir()` and `help()` or read the python docs to determine which functions to use.
'''




from datetime import datetime, timedelta

today = datetime.now()
print(today)
print(today.day)

birthday = "1/15/2025"
test = datetime.strptime(birthday, "%m/%d/%Y")
test = test + timedelta(days =1)
print(test)

"Monday January 15, 2025"

test_str = test.strftime("%A, %B %d %Y")
print(test_str)