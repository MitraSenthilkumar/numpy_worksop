#write a program to find the sum of digits of a given number'
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print("The sum of numbers from  is", sum)
