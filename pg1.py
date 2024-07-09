'''def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from user
        n = int(input("Enter an value for n: "))
        # Calculating the factorial of n
        result = factorial(n)
        # Displaying the result
        print(f"The product of all integers from 1 to {n} is {result}")'''

n = int(input('Enter the val = '))
prod =1
s = ''
for i in range (1,n+1):
    prod = prod*i
    s = s+str(i)+'*'
print ('Factorial of {0} is {1} = {2}'.format(n,s[:-1],prod))

