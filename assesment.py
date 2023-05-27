#Question. 1

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)



#Question 2

def get_file_type(extension_type_mapping, filenames):
    mapping_list = extension_type_mapping.split(';')
    extension_dict = {}

    # Create a dictionary from the extension:type mapping
    for item in mapping_list:
        extension, file_type = item.split(',')
        extension_dict[extension] = file_type

    result_dict = {}

    # Iterate through the filenames and determine their types
    for filename in filenames:
        file_parts = filename.split('.')
        if len(file_parts) > 1:
            extension = file_parts[-1]
            if extension in extension_dict:
                result_dict[filename] = extension_dict[extension]
            else:
                result_dict[filename] = 'unknown'
        else:
            result_dict[filename] = 'unknown'

    return result_dict


# Example usage
extension_type_mapping = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_type_dict = get_file_type(extension_type_mapping, filenames)
print(file_type_dict)




#Question 3


def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list


# Example usage
list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(list_of_dicts, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(list_of_dicts, "color")
print(sorted_list_by_color)



#Question 4

def switch_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

# Example usage
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

switched_dict = switch_key_value(input_dict)
print(switched_dict)



#Question 5

def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements


# Example usage
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, non_common = compare_lists(mainstream, must_watch)
print("Common elements:", common)
print("Non-common elements:", non_common)




Question 6


def get_every_other_sublist(lst, start_idx, end_idx):
    sub_list = lst[start_idx:end_idx+1]
    every_other_sub_list = sub_list[::2]
    return every_other_sub_list


# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_every_other_sublist(input_list, start_index, end_index)
print(result)



Question 7

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Example usage
number = 5
result = factorial(number)
print(result)


Question 8

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]


Question 9

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between the dates
    date_difference = abs((to_date - from_date).days)

    # Check if the difference is less than the specified value
    if date_difference < difference:
        return True
    else:
        return False

# Example usage
result1 = check_date_difference('21-05-10', '21-05-20', 7)
print(result1)  # True

result2 = check_date_difference('21-05-10', '21-05-20', 5)
print(result2)  # False



#Question 10


from datetime import datetime, timedelta

def get_date_before(date, n):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the date before
    date_before = date_obj - timedelta(days=n)

    # Convert the date before to a string representation
    date_before_str = date_before.strftime('%y-%m-%d')

    return date_before_str

# Example usage
result = get_date_before('16-12-10', 11)
print(result)  # '16-11-29'


Question 11

def f(x, l=None):
    if l is None:
        l = []
    for i in range(x):
        l.append(i*i)
    print(l)

