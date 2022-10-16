import arrays
import array_utils
import practice as p

def test_recursive_sum():
    array = array_utils.range_array(0, 10)
    
    result = p.recursive_sum(array)
    expected = 45

    assert result == expected

def test_recursive_sum_out_of_range():
    array = array_utils.range_array(0, 10)
    
    result = p.recursive_sum(array, 100)
    expected = 0

    assert result == expected

def test_gcd_5_10():
    num1 = 5
    num2 = 10

    result = p.gcd(num1, num2)
    expected = 5

    assert result == expected

def test_gcd_12_4():
    num1 = 12
    num2 = 4

    result = p.gcd(num1, num2)
    expected = 4

    assert result == expected

def test_gcd_60_45():
    num1 = 60
    num2 = 45

    result = p.gcd(num1, num2)
    expected = 15

    assert result == expected

def test_gcd_45_60():
    num1 = 45
    num2 = 60

    result = p.gcd(num1, num2)
    expected = 15

    assert result == expected

def test_calcule_average_adjusted_close():
    filename = 'MSFT.csv'

    result = p.calculate_average_adjusted_close(filename)
    expected = 279.64385275418994

    assert result == expected

def test_calcule_average_adjusted_close_fnf():
    filename = 'filenotfound.txt'

    result = p.calculate_average_adjusted_close(filename)
    expected = 0

    assert result == expected


def test_non_recursive_binary_search():
    array = array_utils.range_array(0, 10)

    for i in range(len(array)):
        result = p.non_recursive_binary_search(array, i)
        expected = i

        assert result == expected

def test_non_recursive_binary_search_not_in():
    array = array_utils.range_array(0, 10)
    result = p.non_recursive_binary_search(array, 100)
    expected = -1

    assert result == expected

def test_read_data():
    filename = "sorted_data.txt"

    result = p.read_data(filename)
    expected = [1, 4, 12, 19, 22, 26, 38, 41, 43, 45, 56, 58, 79, 89, 92]

    assert len(result) == len(expected)

    for i in range(len(result)):
        assert result[i] == expected[i]

def test_read_data_fnf():
    filename = "filenotfilefound.txt"

    result = p.read_data(filename)
    expected = None

    assert result is expected

def test_read_and_find():
    filename = "sorted_data.txt"
    values = [1, 4, 12, 19, 22, 26, 38, 41, 43, 45, 56, 58, 79, 89, 92]

    for i in range(len(values)):
        result = p.read_and_find(filename, values[i])
        expected = i

        assert result == expected

def test_read_and_find_not_in():
    filename = "sorted_data.txt"
    result = p.read_and_find(filename, 1000)
    expected = -1

    assert result == expected