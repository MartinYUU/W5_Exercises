# Create a script named greeting.py. Define a variable that contains the current hour (0
# 23). Display one of the greetings below based on the current hour: 
# Time 
# until 10:00am 
# 10:00am until 5:00pm 
# 5:00pm or later 

# Greeting 
# Good morning! 
# Good day! 
# Good evening! 
# Remember to test your script several times using different values for the hour.
#  Update your script to include an additional condition that will print “What are you 
# doing up so late??” if the hour is between 11pm and 4am.

currTime = input('What time is it? (Use HH:MM 24 hour format): ')

if (currTime >= '00:00' and currTime <= '04:00') or (currTime >= '23:00' and currTime <= '24:00'):
    print('What are you doin gup so late?')
elif currTime >= '04:01' and currTime <= '10:00':
    print('Good Moring!')
elif currTime >= '10:01' and currTime <= '17:00':
    print('Good day!')
elif currTime >= '17:01' and currTime <= '22:59':
    print('Good evening!')
else:
    print('Not a valid time.')