# create a script to calculate gross pay given the variables 
# pay_rate and hours_worked. If the person works more than 40 hours, pay the 
# overtime hours at 1.5 times the rate of regular hours.
# 2. When you are finished, review your script with a colleague. Are your algorithms 
# similar? Do you believe each other’s code will work? 
# 3. Run your script several times with different values for pay_rate and hours_worked and 
# confirm the output is right.  
# ∗ Examples of good test data might be: 

print('I will calcualte your gorss pay given your pay rate and your hours worked')

pay_rate = float(input('What is your pay rate?: '))
hours_worked = float(input('How many hours did you work? :'))

if pay_rate < 0:
    print("Wait a minute, you cant be paid less than 0!")
elif pay_rate == 0:
    print('You are working for free. Your pay is $0')
elif hours_worked < 0 :
    print('That is not possible!')
elif hours_worked == 0:
    print('You didnt work this week. You get paid $0')
elif hours_worked <= 40:
    print('Your gross pay is $' + format(pay_rate * hours_worked, ".2f"))
elif hours_worked > 40:
    overtime_hours = hours_worked - 40
    reg_paid_hours = pay_rate * 40
    overtime_pay = (pay_rate * 1.5) * overtime_hours
    gross_pay = overtime_pay + reg_paid_hours
    print('Whoa! What a hard worker! Your gross pay is $' + format(gross_pay, ".2f"))