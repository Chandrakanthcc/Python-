def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

'''

Consider an array: 
5
,
3
,
8
,
4
,
2
5,3,8,4,2

Pass 1:
Compare 5 and 3. Since 5 > 3, swap them. Now the array becomes: 
3
,
5
,
8
,
4
,
2
3,5,8,4,2
Compare 5 and 8. No swap needed.
Compare 8 and 4. Since 8 > 4, swap them. Now the array becomes: 
3
,
5
,
4
,
8
,
2
3,5,4,8,2
Compare 8 and 2. Since 8 > 2, swap them. Now the array becomes: 
3
,
5
,
4
,
2
,
8
3,5,4,2,8
Pass 2:
Compare 3 and 5. No swap needed.
Compare 5 and 4. Since 5 > 4, swap them. Now the array becomes: 
3
,
4
,
5
,
2
,
8
3,4,5,2,8
Compare 5 and 2. Since 5 > 2, swap them. Now the array becomes: 
3
,
4
,
2
,
5
,
8
3,4,2,5,8
Compare 5 and 8. No swap needed.
Pass 3:
Compare 3 and 4. No swap needed.
Compare 4 and 2. Since 4 > 2, swap them. Now the array becomes: 
3
,
2
,
4
,
5
,
8
3,2,4,5,8
Compare 4 and 5. No swap needed.
Compare 5 and 8. No swap needed.
Pass 4:
Compare 3 and 2. Since 3 > 2, swap them. Now the array becomes: 
2
,
3
,
4
,
5
,
8
2,3,4,5,8
Compare 3 and 4. No swap needed.
Compare 4 and 5. No swap needed.
Compare 5 and 8. No swap needed.
Now, the array is fully sorted: 
2
,
3
,
4
,
5
,
8
2,3,4,5,8.

'''
