#write a program to find the factorial of a nummber
n = int(input("Enter a number: "))
factorial = 1

if n < 0:
    print("No negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of is", factorial)
