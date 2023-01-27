#ans1
print(input("Please enter any String:-")[::-1])

#ans2
a = int(input("Enter the start of the range: "))
b = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))
for i in range(a , b + 1):
 if i % divisor == 0:
  print(i)

#ans3
a=int(input("PLEASE ENTER THE FIRST SIDE OF THE TRIANGLE:-"))
b=int(input("PLEASE ENTER THE SECOND SIDE OF THE TRIANGLE:-"))
c=int(input("PLEASE ENTER THE THIRD SIDE OF THE TRIANGLE:-"))
s=b+c+a/3
Area=(s*s-a*s-b*s-c)**0.5
if (a+b > c) and (b+c > a) and (c+a > b):
    print(Area)
else:
    print("This is not a triangle please enter some valid values")

#ans5
n = int(input("Enter the number of rows: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1, n+1):
    for j in range(i):
        print(alphabet[j % len(alphabet)], end=" ")
    print()

#ans6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
def count_primes(start, end):
    count = 0
    for i in range(start, end+1):
        if is_prime(i):
            count += 1
    return count
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
print("Number of prime numbers between", start, "and", end, ":", count_primes(start, end))

#ans8
result = []
for i in range(1, 501):
    if i % 7 == 0 and i % 11 == 0:
        result.append(i)
print("Numbers which are multiple of 7 and divisible by 11 between 1 and 500:",result)

#ans9
from collections import Counter

words = input("Enter words separated by space: ").split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")



