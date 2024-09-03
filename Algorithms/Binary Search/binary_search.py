# An array containing a list of strings
list_of_names = [
    "John",
    "Carl",
    "Erick",
    "Brad",
    "Jenny",
    "Kyle",
    "Merly",
    "Patricia",
    "Ashley",
    "Chad",
    "Jolie",
    "Kylie",
    "Angela",
    "Henry"
]

# Sort for efficiency
list_of_names.sort()

# Binary search function
def search(key, arr, lo=None, hi=None):
    # instantiate variables
    length = len(arr)
    if lo == None: lo = 0
    if hi == None: hi = length - 1 # Because the indexing starts at index 0
    if lo > hi:
        return -1
    
    # Finding the middle index
    mid = lo + (hi - lo) // 2

    # If the middle element matches the key, return the index
    if arr[mid] == key:
        return mid
    # Otherwise if the middle element is less than the value of the key
    elif arr[mid] < key:
        # Recursive search
        return search(key, arr, mid + 1, hi)
    # Other cases
    else:
        # Recursive search
        return search(key, arr, lo, mid - 1)

# Query
index = search("Henry", list_of_names)

# Prompt
if index == -1:
    print("key not found!")
else:
    print(f"Found {list_of_names[index]} at index {index}")
