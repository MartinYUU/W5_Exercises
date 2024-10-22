# Define known values 
food_cost = 79.25 
tax = 6.54 
tip = 12.00 
# Calculate the unknown 
total_due = food_cost + tax + tip 
# Display the results 
#print("The total due is " + str(total_due))

print('food cost is ' + str(food_cost) + ' and tax is ' + str(tax)) 
#print('tip is ' + str(tip)) 
print('Total due is ' + str(total_due)) 


# Bonus Q: Note that you can’t simply copy and paste the above text into VSCode. 
# Why is that?
#Because the double qoutes used wont paste as the ones python uses to make strings


print("Tip is " + format(tip, ".2f")) 