# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?
# Code the script in a file named rentals.py
# Test your script with 38 tourists. Now do some calculations by hand to check your
# work.
# ∗ How much money did your script say you had to charge per person?
# ∗ If you multiply that out, how much did you collect?
# ∗ How much were the vans?
# ∗ Why do you have leftover money?

import math

vanCapacity = 15
vanCostDay = 250
partySize = 38

minVans = math.ceil(partySize / vanCapacity)

totalVanCost = minVans * vanCostDay

costPerPerson = totalVanCost / partySize

print('We need at least',minVans, 'vans.')
print(minVans, 'vans will cost $' + str(totalVanCost))
print('each person will need to pay $' + format(costPerPerson, ".2f"))

# 19.74 * 38 = 750.12
# there are 12 extra cents because the cost per person was rounded