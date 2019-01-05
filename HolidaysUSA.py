# Python script to print holidays in year 2019(USA)
# pip install holidays


from datetime import date
import holidays
import sys


# Select country
uk_holidays = holidays.UnitedStates()

for ptr in holidays.UnitedStates(year=2019).items():
    print(ptr)

