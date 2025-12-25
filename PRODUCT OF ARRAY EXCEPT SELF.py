def product_except_self(nums):
    # Create an array 'answer' with the same length as nums, filled with 1s
    # This will eventually store the final product for each index
    answer = [1] * len(nums)

    # Start a variable to store the running product from the left side
    left_product = 1

    # First pass: fill 'answer' with products of all elements to the LEFT of each index
    for i in range(len(nums)):
        # Store the current left product in answer[i]
        answer[i] = left_product
        
        # Update left_product by multiplying it with nums[i]
        # so it represents product of all elements before the next index
        left_product *= nums[i]

    # Start a variable to store the running product from the RIGHT side
    right_product = 1

    # Second pass: move from right to left, multiplying right-side products into answer
    for i in range(len(nums) - 1, -1, -1):
        # Multiply the already stored left-product with the right-product
        answer[i] *= right_product

        # Update right_product by multiplying it with nums[i]
        # so it represents product of all elements after the next index on the left
        right_product *= nums[i]
    return answer

nums = [1, 2, 3, 4]
print(product_except_self(nums))