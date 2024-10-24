#  Start by creating two tuples: one that lists at least 3 types of candy that can come in 
# fruit flavors, and another than lists at least 3 fruity flavors. (Feel free to get creative with 
# your flavor ideas…) 
# 3. Now create a new variable to store candy combinations as a set. Using the index of 
# each tuple, add at least one combination of each candy and flavor to the new set – for 
# example, putting together tuple1[0] and tuple2[1] 
# 4. Create an output message that says, “Today’s candy options include:” and then prints 
# the contents of the set. 
# 5. Print the output multiple times. What do you notice about the order of the items as you 
# repeat the output?

candies = ('starburst', 'skittles', 'sour patch')

flavors = ('watermelon', 'strawberry', 'raspberry')

combos = {flavors[0] + ' ' + candies[0],
          flavors[1] + ' ' + candies[2],
          flavors[2] + ' ' + candies[1],
          flavors[0] + ' ' + candies[1],
          }

# order of the output is different every time the print statement is run
print('Todays candy options include: ', combos)
