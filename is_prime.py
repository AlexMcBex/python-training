def is_prime(n):
    # print(int(n ** 0.5) + 1)
    if n<2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        print(i)
        if n % i == 0:
            print(n," is divisible by " ,i)
            return False
    return True

print(is_prime(17))