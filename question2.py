# find if the given number is a palindrome or not?

num = int(input("Enter the number:"))

r = 0
temp = num

while temp > 0:
    r = r * 10 + (temp % 10)
    temp = temp // 10
if r == num:
    print("Palindrome")
else:
    print("Not palindrome")
