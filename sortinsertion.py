def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)

print("Sorted array is:", arr)

'''
Initial State: The algorithm starts with the assumption that the first element
of the array is already sorted.
Iterative Process:
It then considers each element in turn, starting from the second element.
For each element, the algorithm compares it with the elements to its left,
moving them one position to the right until it finds the correct position for
the current element.
This process effectively "inserts" the current element into its
correct position within the already sorted portion of the array.

Repeat: The algorithm repeats this process for each element in the array until the entire array is sorted.


Consider an array: 
5
,
2
,
4
,
6
,
1
,
3
5,2,4,6,1,3

Step 1: Assume the first element (5) is already sorted.
Step 2: Consider the second element (2). Since 2 is smaller than 5, we move 5 one position to the right and insert 2 before 5. Now the array becomes: 
2
,
5
,
4
,
6
,
1
,
3
2,5,4,6,1,3
Step 3: Consider the third element (4). We compare it with the elements to its left. Since 4 is greater than 2 but smaller than 5, it belongs between 2 and 5. We insert 4 at the correct position. Now the array becomes: 
2
,
4
,
5
,
6
,
1
,
3
2,4,5,6,1,3
Step 4: Consider the fourth element (6). Since 6 is greater than all the elements to its left, it remains in its current position.
Step 5: Consider the fifth element (1). We compare it with the elements to its left. Since 1 is smaller than 6, we move 6 one position to the right. We continue this process until we find the correct position for 1. Now the array becomes: 
1
,
2
,
4
,
5
,
6
,
3
1,2,4,5,6,3
Step 6: Consider the sixth element (3). We compare it with the elements to its left. Since 3 is smaller than 6, we move 6 one position to the right. We continue this process until we find the correct position for 3. Now the array becomes: 
1
,
2
,
3
,
4
,
5
,
6
1,2,3,4,5,6
'''