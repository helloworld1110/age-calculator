# python 3.7.1

# importing 

import datetime

# inputting data

Year_birth = int(input("write a year of birth \n"))
Month_birth = int(input("write a month of birth \n"))
Day_birth = int(input("write a day of birth \n"))

# definiting current time 

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

# definiting time

time = str(input ("do u wanna use ur time or current time? y/n \n"))
y = str(input)

if (time == "y") : 
  custom_year = int(input ("ur own year \n"))
  custom_month = int(input ("ur own month \n"))
  custom_day = int(input ("ur own day \n"))

# change the values

if (time == "y"):
 current_year = custom_year
 current_month = custom_month
 current_day = custom_day

# calculating

# real age

A1 = current_year - Year_birth
A2 = A1 * 12
A3 = A2 - Month_birth
real_age = A3 // 12 
if current_month > Month_birth:
  real_age += 1

# counting leap years

L1 = Year_birth // 4 
L2 = current_year // 4
leap_year_correction = L2 - L1

if Year_birth % 4 == 0:
  if Month_birth > 2:
    leap_year_correction -= 1
  

# correct month

A5 = abs(current_month - Month_birth)
real_month = 12 - A5 
if Month_birth < current_month:
  real_month += 3 
if current_month > Month_birth:
  real_month -= 1
  real_age -= 1
if current_month < Month_birth:
  leap_year_correction -= 1 
if real_month >= 12:
  real_age += 1
  real_month -= 12
  
# correct day

real_day = abs(current_day - Day_birth) + leap_year_correction

# months days 'array'

Jan = 31
Feb = 28 # cuz variable leap_year_correction corrects the value            
Mar = 31
Apr = 30
May = 31
Jun = 30
Jul = 30
Aug = 31
Sep = 30
Oct = 31
Nov = 30
Dec = 31

# days total

days_total = 0

if Month_birth == 1 :
  days_total = Jan
if Month_birth == 2 :
  days_total = Jan + Feb
if Month_birth == 3 :
  days_total = Jan + Feb + Mar
if Month_birth == 4 :
  days_total = Jan + Feb + Mar + Apr
if Month_birth == 5 :
  days_total = Jan + Feb + Mar + Apr + May
if Month_birth == 6 :
  days_total = Jan + Feb + Mar + Apr + May + Jun
if Month_birth == 7 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul                                      
if Month_birth == 8 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug                                     
if Month_birth == 9 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep     
if Month_birth == 10 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct     
if Month_birth == 11 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov
if Month_birth == 12 :
  days_total = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec

# calculating unimportant necessary values

days_total = 365 * real_age + days_total + leap_year_correction
hours = days_total * 24
minutes = hours * 60
seconds = minutes * 60

# printing

print ("Age: " , real_age ," years", real_month , " months" ,  real_day ,"days")                        
print ("Or: " , days_total , " days")
print ("Or: ", hours," hours")
print ("Or: ",minutes, " minutes")
print ("Or: ",seconds, " seconds")




#rrrr
# tttt