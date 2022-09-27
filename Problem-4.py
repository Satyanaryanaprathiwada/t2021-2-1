# Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]


numbers_list = [1,2,3,4,5,6,7,8,9]
input_list = [1,2,8,9,12,46,76,82,15,20,30]
result = {}
count = 0
for i in numbers_list:
    for j in input_list:
        if j%i==0:
            count +=1
            result[i]=count
        elif count==0:
            result[i]=count
    count = 0
print(result)