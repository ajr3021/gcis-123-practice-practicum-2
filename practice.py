import csv
import arrays

def recursive_sum(array, index=0):
    if index >= len(array):
        return 0
    return array[index] + recursive_sum(array, index + 1)

def gcd(n, m):
    if n == m:
        return n
    elif n > m:
        return gcd(n - m, m)
    elif n < m:
        return gcd(n, m - n)

def calculate_average_adjusted_close(filename):
    ADJ_CLOSE_INDEX = 5
    try:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            array = arrays.Array(179)
            index = 0
            for line in reader:
                array[index] = float(line[ADJ_CLOSE_INDEX])
                index += 1
        return recursive_sum(array) / len(array)
    except FileNotFoundError:
        return 0


def non_recursive_binary_search(array, target):
    if array is None:
        return -1
    
    start = 0
    end = len(array) - 1

    while(start <= end):
        index = (end + start) // 2
        if array[index] == target:
            return index
        elif target < array[index]:
            end = index - 1
        else:
            start = index + 1
    return -1 

def read_data(filename):
    try:
        with open(filename) as file_:
            first = True
            index = 0
            for line in file_:
                if first:
                    array = arrays.Array(int(line.strip()), 0)
                    first = False
                else:
                    array[index] = int(line.strip())
                    index += 1
        return array
    except FileNotFoundError:
        return None

def read_and_find(filename, target):
    array = read_data(filename)
    return non_recursive_binary_search(array, target)
