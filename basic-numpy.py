import numpy as np
numbers = raw_input("Type in a list of numbers separated by space: ")
numbers = map(int, numbers.split()) # seperate the string of numbers using space character delimiter
print numbers
if len(numbers) > 0:
    print "The average of your numbers is", np.mean(numbers)
    print "The median of your numbers is", np.median(numbers)
    print "The standard deviation of your numbers is", np.std(numbers)

numbers2 = map(lambda x: x*2, numbers)  # lambda = anonymous function
numbers3 = map(lambda x: x**2, numbers)
print "The numbers times 2 is ",numbers2
print "The numbers to the power of 2 is ",numbers3
matrix = np.array([numbers, numbers2, numbers3],float)
print "The 2D array of all these is:\n",matrix

matrix2 = np.transpose(matrix)
print "The transpose of this 2D array is:\n",matrix2
print "Multiplication of the two matrices is:\n",np.dot(matrix, matrix2)