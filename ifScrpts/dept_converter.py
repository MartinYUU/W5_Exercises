# Write a script named dept_converter.py that uses conditional logic to determine and 
# print department name based on a department code. Make sure to test your script with 
# multiple codes. 
# 1 Marketing 
# 5 Human Resources 
# 10 Accounting 
# 12 Legal 
# 18 IT 
# 20 Customer Relations



requestedDepartment = int(input('what department do you need?' "\n" \
                                'Options are 1, 5, 10, 12, 18, 20 : '))

match requestedDepartment :
    case 1:
        print('Marketing')
    case 5:
        print('Human Resources')
    case 10:
        print('Accounting')
    case 12:
        print('Legal')
    case 18:
        print('IT')
    case 20:
        print('Customer Relations')
    case other:
        print('That is not an option.')
