def first_repeating(arr):
    hashset = set()
    for n in arr:
        if n in hashset:
            return n
        hashset.add(n)
    return -1

print (first_repeating([1,2,3,4,1,2,3,4]))