def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        # For each number, calculate the value needed to reach the target
        complement = target - num
        
        if complement in seen:
            # If yes, we have found the two numbers that add up to the target
            # Return their indices: index of complement (from dictionary) and current index (i)
            return (seen[complement], i)
        
        seen[num] = i
        
    return None # Return None if no pair is found

inputs = [2, 7, 11, 15]
target = 9

result = two_sum(inputs, target)
print(result)