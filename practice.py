"""
Create function that, given an array of numbers, will recursively
calculate the sum of those numbers. 

Return: the sum of all numbers in the array
"""
def recursive_sum(array, index=0):
    return 0

"""
Create a function that will calculate the gretest common denominator
of n and m according to the algorithm shown in gcd.jpg.

Return: the greatest common denominator of n and m
"""
def gcd(n, m):
    return 0

"""
Create a function that, given the name of csv file that contains stock data, 
will calculate the average adjusted close price by reading in the values
into an array, summing them using recursive_sum function, and dividing by length.

The adjusted closer price will be at index 5 and the array will be of length 179.
Take at look at MSFT.csv to see what the data looks like.

If the file passed in does not exist, the function should return 0

Return: The average adjusted close price or 0 if the file does not exist
"""
def calculate_average_adjusted_close(filename):
    ADJ_CLOSE_INDEX = 5
    ARRAY_LENGTH = 179
    return 0

"""
Create a binary search algorithm that does not use recursion.
If the array given is None, return -1

Return: index of the target value or -1 if the target does not exist or the array is None
"""
def non_recursive_binary_search(array, target):
    return 0

"""
Create a function that, given a filename, will return an array of 
all numbers in the file.

The first number in the file will be the length of the array. This should NOT
be included in your returned array.

Each line will only have one number. The data will also be in sorted order.
See sorted_data.txt.

If the file does not exist, return None

Return: An array of all numbers in the given file or None if the file does not exist
"""
def read_data(filename):
    return None

"""
Create a function that combines the two previous functions. It should create
a sorted array from a given filename and return the index of the target value.

Return: Same as non_recursive_binary_search
"""
def read_and_find(filename, target):
    return 0
