myFavMovies = ['Inception', 'Shutter Island', 'Cars', 'Insidius']

print()
print('The list myFavMovies include my top', len(myFavMovies), 'favorite movies.')
print(myFavMovies)
print()

print(sorted(myFavMovies))
print(myFavMovies)
print()

myFavMovies.sort()
print(myFavMovies)

# Sorted() did not change the order of the list assigned the original variable
# which is why when you print the list again, the list is not sorted
# .sort() sorted the list and changed the order in the original variable
