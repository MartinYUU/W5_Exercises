pay_rate = float(input('What is your pay rate?: '))
hours_worked = float(input('How many hours did you work every week? :'))
filing_status = input('will you file your taxes jointly or single? :').lower()
annual_gross_pay = pay_rate * hours_worked * 52
tax_rate = 0

if pay_rate < 0:
    print("Wait a minute, you cant be paid less than 0!")
elif pay_rate == 0:
    print('You are working for free. Your pay is $0')
elif hours_worked < 0 :
    print('That is not possible!')
elif hours_worked == 0:
    print('You didnt work this week. You get paid $0')
elif hours_worked <= 40:
    if filing_status == 'single' and annual_gross_pay < 12000 :
        tax_rate = 0.05
    elif filing_status == 'single' and (12000 <= annual_gross_pay < 25000):
        tax_rate = 0.1
    elif filing_status == 'single' and (25000 <= annual_gross_pay < 75000):
        tax_rate = 0.15
    elif filing_status == 'single' and ( annual_gross_pay >= 75000):
        tax_rate = 0.2
    elif filing_status == 'married' and ( annual_gross_pay < 12000):
        tax_rate = 0.0
    elif filing_status == 'married' and (12000 <= annual_gross_pay < 25000):
        tax_rate = 0.06
    elif filing_status == 'married' and (25000 <= annual_gross_pay < 75000):
        tax_rate = 0.11
    elif filing_status == 'married' and ( annual_gross_pay >= 75000):
        tax_rate = 0.2
    else :
       raise ValueError("Error: That is not a valid filing status.") # used this to ensure only valid inputs
        
    weekly_gross_pay = pay_rate * hours_worked
    weekly_tax_withheld = (pay_rate * hours_worked) * tax_rate
    print('You worked', hours_worked, 'hours this period.')
    print('Because you earened $' + format(pay_rate, ".2f"), 'per hour, your gross weekly pay is $' + format(weekly_gross_pay, ".2f") )
    print('Your filing status is', filing_status)
    print('Your tax withholding for the week is $', format(weekly_tax_withheld, ".2f"))
    print('Your net pay is $' + format(weekly_gross_pay - weekly_tax_withheld, ".2f"))
elif hours_worked > 40:
    overtime_hours = hours_worked - 40
    reg_fulltime_pay = pay_rate * 40
    overtime_pay = (pay_rate * 1.5) * overtime_hours
    weekly_gross_pay = overtime_pay + reg_fulltime_pay
    annual_gross_pay = weekly_gross_pay * 52
    if filing_status == 'single' and annual_gross_pay < 12000 :
        tax_rate = 0.05
    elif filing_status == 'single' and (12000 <= annual_gross_pay < 25000):
        tax_rate = 0.1
    elif filing_status == 'single' and (25000 <= annual_gross_pay < 75000):
        tax_rate = 0.15
    elif filing_status == 'single' and ( annual_gross_pay >= 75000):
        tax_rate = 0.2
    elif filing_status == 'married' and ( annual_gross_pay < 12000):
        tax_rate = 0.0
    elif filing_status == 'married' and (12000 <= annual_gross_pay < 25000):
        tax_rate = 0.06
    elif filing_status == 'married' and (25000 <= annual_gross_pay < 75000):
        tax_rate = 0.11
    elif filing_status == 'married' and ( annual_gross_pay >= 75000):
        tax_rate = 0.2
    else :
       raise ValueError("Error: That is not a valid filing status.") # used this to ensure only valid inputs
    weekly_tax_withheld = weekly_gross_pay * tax_rate
    print('You worked', hours_worked, 'hours this period.')
    print('Because you earened $' + format(pay_rate, ".2f"), 'per hour, your gross weekly pay is $' + format(weekly_gross_pay, ".2f") )
    print('Your filing status is', filing_status)
    print('Your tax withholding for the week is $', format(weekly_tax_withheld, ".2f"))
    print('Your net pay is $' + format(weekly_gross_pay - weekly_tax_withheld, ".2f"))
   