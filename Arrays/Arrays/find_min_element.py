# Find minimum element in an array

arr = [3, 7, 2, 9, 5]
min_val = arr[0]

for num in arr:
    if num < min_val:
        min_val = num

print(min_val)
