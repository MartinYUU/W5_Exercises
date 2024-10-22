# 3.0 Federal taxes are 23% of your salary every month. You make X 
# amount of money. How much is withheld for taxes?


monthlyTaxRate = 0.23
monthlySalary = 5000
monthlyTaxWithheld = monthlySalary * monthlyTaxRate

print(monthlyTaxWithheld)

print('$' + format(monthlyTaxWithheld, ".2f") + ' is withheld for taxes every month!')