

num = int(input("Enter a number : "))
odd = 1
if num%2 ==0:
    for i in range(num-1):
        print(odd,end = ",")
        odd += 2

if num%2 != 0:
    for i in range(num):
        print(odd,end = ",")
        odd += 2