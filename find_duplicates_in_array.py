def find_duplicates(arr):
    hashset = set()
    duplicates =set()
    
    for n in arr:
        if n in hashset:
            duplicates.add(n)
        else:
            hashset.add(n)
    return list(duplicates)
    
print (find_duplicates([1,2,3,4,5,1,6,7,3,8,9,7,0,8,6,7]))