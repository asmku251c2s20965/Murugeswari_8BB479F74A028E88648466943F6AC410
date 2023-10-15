#1.2 write a program that determines whether a year enter by the user is a leap year not using ifelif-else statements
year=2023
#To get year(integer input)from the user
#year=int(input ("Enter a year:")) 
#divided by 100 means century year(ending with 00)
#century year divided by 400 in leap year
if(year%400==0) and (year%100==O):
  print("{0} is a leap year".format(year))
  #not divide by 100 means not a century year
#year divided by 4 is a leap year
elif(year%4==0) and (year%100!=0):
  print("{0} is leap year".format(year))
#if not divided by both 400(century year) and 4(not century year)
#year is not leap year
else: 
  print("{0} is not a leap year".format(year))

