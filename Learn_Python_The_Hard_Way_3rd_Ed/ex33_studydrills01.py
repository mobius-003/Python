def funct (n):
    numbers =[]
    i = 0
    while i < n:
        print (f"List is: {i}")
        numbers.append(i)
        i += 1
    print(numbers)

print (f"\n Using funct with n = {funct}")
funct(17)
