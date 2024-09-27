def count_vowels(s):
    count = 0
    vowels = 'aeiou'
    # return sum(1 for 
    #            char in 
    #            s.lower() if 
    #            char in 
    #            vowels)
    for char in s.lower():
        if char in vowels:
            count += 1
    return "%s vowels found in %s" %(count, s)
print(count_vowels("ammaccabanane"))