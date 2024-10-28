# . Create a script named savings_goal.py. 
# 2. Create a variable for your starting bank balance, another that sets your savings goal, 
# and a third with your weekly savings amount. 
# 3. Use a while loop to compare your bank balance to your savings goal, if you haven’t 
# met your goal yet, add the weekly savings amount to your bank balance. For each loop, 
# print the statement, “This week my balance increased to ___.” Once your savings goal 
# is met, print the statement, “Goal met! My current balance is ___.” 

# Try adding additional logic to your loop:  
# ∗ If your balance is more than halfway to your goal, print the message, “Almost there! 
# This week my balance is up to ___.” 
# ∗ If your balance is at least 75% of your goal, add a calculation to buy yourself a little 
# treat. Print the message, “So close! After treating myself, my balance is up to ___.”


starting_balance = 1000
savings_goal = 5000
weekly_savings_amt = 120
treat_cost = 20

while starting_balance < savings_goal:
    starting_balance += weekly_savings_amt
    if starting_balance <= savings_goal / 2:
        print('This week my balace is $' + format(starting_balance, ".2f"))
    elif starting_balance > savings_goal / 2 and starting_balance < savings_goal * 0.75:
        print('Almost there! This week my balace is uo to $' + format(starting_balance, ".2f"))
    elif starting_balance >= savings_goal * 0.75:
        starting_balance -= treat_cost
        print('So close! After treating myself, my balance is up to $' + format(starting_balance, ".2f"))



print('Goal met! My current balance is ' + format(starting_balance, ".2f"))
