# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

def secondInYear():
    days = 365 # A Year
    hours = 24 # A day
    mins = 60  # A Minute
    secs = 60  # A Second
    print("\n ### SECOND IN YEAR ### \n")
    print(f"There are {days*hours*mins*secs} seconds in a year!")

secondInYear()
