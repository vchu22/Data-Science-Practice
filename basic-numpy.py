import numpy as np
numbers = raw_input("Type in a list of numbers separated by space: ")
numbers = map(int, numbers.split())
print numbers
print "The average of your numbers is", np.mean(numbers)
print "The median of your numbers is", np.median(numbers)
print "The standard deviation of your numbers is", np.std(numbers)
