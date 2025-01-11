import random

numbers = [random.randint(1, 100) for num in range(10)]
print(numbers)

def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(1,len(numbers)-i):
            if numbers[j-1] > numbers[j]:
                temp = numbers[j-1]
                numbers[j-1] = numbers[j]
                numbers[j] = temp
            else:
                continue
    return numbers
sorted_val = bubble_sort(numbers)
print(sorted_val)