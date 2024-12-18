unit = int(input("How many units of electricity did u consumed: "))

if (unit < 50) :
    amt = unit*2.60
    tax = 25
elif (unit <= 100) :
    amt = 130 + ((unit - 50) *3.25)
    tax = 35
elif (unit <= 200) :
    amt = 130 + 162.50 + ((unit - 100) *5.26)
    tax = 45
else:
    amt = 130 + 162.50 + 526 + ((unit - 200) *8.45)
    tax = 75
total = amt + tax 
print("/nElectricity bill = %.2f" %total)
