# define a dictionary that includes the 
# following keys and the sample values of your choice:
# name 
# address 
# city
# state 
# zip
# 2. Print the address as properly formatted for mailing. Avoid using multiple print 
# statements. Experiment with using a multi-line f-string (triple quotes), or use "\n" (new 
# line) to break the address into multiple lines. 
# 3. Remove the key:value pair for name.  
# 4. Add a new variable for full_name and assign its value as a tuple containing two 
# key:value pairs. The first key:value pair should contain the key “first name” and a first 
# name, and the second should contain the key “last name” and a last name. 
# 5. Use the .update() method to add one more key:value pair, with the key “honorific” and 
# the value set to Mr. / Ms. / Mx. / Dr. / Hon. / etc. as appropriate. 
# 6. Print the formatted address again, updating as needed to include the new dictionary items

dict1 = {'name' : 'Bruce Banner',
         'address' : '123 Hulk st',
         'city' : 'Smash City',
         'State' : 'NY',
         'zip' : '19620'
         }
# used + to line them up to the same indentations
print(dict1['name'], "\n" +\
      dict1['address'], "\n" +\
      dict1['city'], dict1['State'], dict1['zip'], "\n"
      )

dict1.pop('name')


full_name = {'first name' : 'Bruce',
             'last name' : 'Banner'
            }

full_name.update({'honoriffic' : 'Dr.'})

print(full_name['honoriffic'], full_name['first name'], full_name['last name'], "\n" +\
      dict1['address'], "\n" +\
      dict1['city'], dict1['State'], dict1['zip'] 
      )