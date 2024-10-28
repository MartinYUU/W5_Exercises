# . Create a script named savings_goal.py. 
# 2. Create a variable for your starting bank balance, another that sets your savings goal, 
# and a third with your weekly savings amount. 
# 3. Use a while loop to compare your bank balance to your savings goal, if you haven’t 
# met your goal yet, add the weekly savings amount to your bank balance. For each loop, 
# print the statement, “This week my balance increased to ___.” Once your savings goal 
# is met, print the statement, “Goal met! My current balance is ___.” 


starting_balance = 1000
savings_goal = 5000
weekly_savings_amt = 120

while starting_balance < savings_goal:
    starting_balance += weekly_savings_amt
    print('This week my balace is $' + format(starting_balance, ".2f"))

print('Goal met! My current balance is ' + format(starting_balance, ".2f"))
