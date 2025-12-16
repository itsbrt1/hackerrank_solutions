def frequency(num):
    freq ={}
    for n in num:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq

print(frequency([1,2,2,3,4,4,4,5]))


