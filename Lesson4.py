# 3.1 Daniel Gillam J100643 02/08/2023
hours = input("Enter Hours:")
rate = float(input("Please enter the hourly rate:"))
h = float(hours)
if(h>40):
    ot=h-40
    nt=40
print(nt*rate+ot*rate*1.5)
