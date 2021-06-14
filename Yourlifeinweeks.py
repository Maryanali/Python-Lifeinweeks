#!/usr/bin/env python3

#Your life in weeks,days weeks and months if you lived until you are 90!!
age = input("What is your current age? ")

age_int= int(age)

years_remaining= 90- age_int

days_remaining=years_remaining*365

weeks_remaining=years_remaining*52

months_remaining=years_remaining*12

print(f"You have {days_remaining} days remaining, {weeks_remaining} weeks remaining, {months_remaining} months remaining, {years_remaining} years remaining 🙂" )