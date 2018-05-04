import random

array = []
for i in range(19):
    array.append(random.randrange(0, 2000, 1, int))
print(array)
temp_arr = []
k = 0
inpt = random.randrange(0, 2000, 1, int) # заданное число
print(inpt)
for i in range(len(array)):
    while k < 3:
        if array[i] > inpt:
            temp_arr.append(array[i])
            k = k + 1
            break
        else:
            break
print(temp_arr)
