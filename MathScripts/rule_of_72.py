# How long will it take a savings account worth X to double in value based on an interest 
# rate of IR? (Hint: Look up the rule of 72) 

savingsAccoount = 100000
interestRate = 6


print('At a ' + format(interestRate) + '%', 'interest rate, your savings account'\
      + 'will be worth $' + format(savingsAccoount * 2, ".2f"), 'in', format(72/interestRate, ".1f"), 'years.'\
      )