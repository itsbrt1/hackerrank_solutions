def ifunique(arr):
    if len(arr) == len(set(arr)):
        return True
    return False

print(ifunique([1, 2, 3, 4, 5]))