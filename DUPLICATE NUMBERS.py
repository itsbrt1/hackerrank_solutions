def contains_duplicate_number(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
        return False

    return False

nums = [1, 2, 3, 1]
print(contains_duplicate_number(nums))