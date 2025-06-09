# Performed of linear search is O(n), where n is the number of elements in the array.
#In the worst case, it checks each element until it finds the target or reaches the end of the list with O(n) time complexity.
# In the best case, it finds the target at the first position with O(1) time complexity.
def linear_search(arr, target):
    """
    Perform a linear search for a target value in an array.

    Parameters:
    arr (list): The list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Performance of linear search is O(log n), where n is the number of elements in the array was sorted.
# In the worst case, it checks each element until it finds the target or reaches the end of the list with O(log n) time complexity.
# In the best case, it finds the target at the mid position with O(1) time complexity.
# With arr have 1000000 elements, the performance of binary search is significantly better than linear search, only need 20 times to compare.
def binary_search(arr, target):
    """
    Perform a binary search for a target value in a sorted array.

    Parameters:
    arr (list): The sorted list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Performence of interpolation search is O(log log n), where n is the number of elements in the array was sorted.
# In the worst case, it checks each element until it finds the target or reaches the end of the list with O (n) time complexity.
# In the best case, it finds the target at the first position with O(1) time complexity.
# But in case arr is unsorted or the target is not in the array, it may perform poorly, it is special note when using searching.
# Interpolation search is more efficient than binary search for uniformly distributed data.
# However, it is not suitable for all types of data distributions.
# Interpolation search is an improved version of binary search that uses the distribution of values to find the target.
# It calculates the position of the target based on the values at the low and high indices,
# which can lead to faster searches in certain cases.
# In the case the value is not uniformly distributed, the performance may degrade to O(n) in the worst case.
def interpolation_search(arr, target):
    """
    Perform an interpolation search for a target value in a sorted array.

    Parameters:
    arr (list): The sorted list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Calculate the position using interpolation formula
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Performence of jump search is O(sqrt(n)), where n is the number of elements in the array was sorted.
# In the worst case, it checks each element until it finds the target or reaches the end of the list with O(sqrt(n)) time complexity.
# In the best case, it finds the target at the first position with O(1) time complexity.
# Jump search is a searching algorithm for sorted arrays that divides the array into blocks of fixed size (usually the square root of the array length).
def jump_search(arr, target):
    """
    Perform a jump search for a target value in a sorted array.

    Parameters:
    arr (list): The sorted list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    n = len(arr)
    step = int(n**0.5)  # Optimal jump size
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1

# Performence of exponential search is O(log n), where n is the number of elements in the array was sorted.
# In the worst case, it checks each element until it finds the target or reaches the end of the list with O(log n) time complexity.
# In the best case, it finds the target at the first position with O(1) time complexity.
# Exponential search is a searching algorithm that works on sorted arrays.
# It starts with a small range and exponentially increases the range until it finds a range that contains the target.
# After finding the range, it performs a binary search within that range.
def exponential_search(arr, target):
    """
    Perform an exponential search for a target value in a sorted array.

    Parameters:
    arr (list): The sorted list to search through.
    target (any): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    if arr[0] == target:
        return 0

    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    # Perform binary search in the found range
    left = index // 2
    right = min(index, len(arr) - 1)
    
    return binary_search(arr[left:right + 1], target)