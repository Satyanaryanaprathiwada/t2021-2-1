# With a single integer as the input, generate the following until a = x

num = int(input("Enter a number: "))
odd = 1
for i in range(num):
    odd += 2
    print(odd,end = ",")