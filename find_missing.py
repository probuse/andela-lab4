def find_missing(list1, list2):
    if set(list1) == set(list2):
        return 0
    if len(list1) < len(list2):
        new_list = set(list2) - set(list1)
    else:
        new_list = set(list1) - set(list2)
    return new_list.pop()
    
print find_missing([1, 2, 3], [1, 2, 3, 4])
print find_missing([4, 66, 7], [66, 77, 7, 4])
print find_missing([], [])
print find_missing([2], [2])
print find_missing([4], [4])
print find_missing([7], [7])
print find_missing([1, 2], [1, 2, 5])
print find_missing([4, 6, 8], [4, 6, 8, 10])
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
