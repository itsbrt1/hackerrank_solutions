def contains_duplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # False (no duplicates)
print(contains_duplicate([1, 2, 3, 4, 1]))  # True (1 appears twice)