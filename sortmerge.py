def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)

'''

Consider an unsorted array: 
38
,
27
,
43
,
3
,
9
,
82
,
10
38,27,43,3,9,82,10

Divide:
Divide the array into two halves: 
38
,
27
,
43
0,
3
38,27,43,3 and 
9
,
82
,
10
9,82,10
Recursively divide each half until we have subarrays containing only one element:
38
,
27
38,27, 
43
,
3
43,3, 
9
,
82
9,82, 
10
10
Now, each subarray is considered sorted.
Conquer:
Begin merging the sorted subarrays:
Merge 
38
38 and 
27
27 to get 
27
,
38
27,38
Merge 
43
43 and 
3
3 to get 
3
,
43
3,43
Merge 
9
9 and 
82
82 to get 
9
,
82
9,82
Leave 
10
10 as it is since it's already sorted.
Merge Subarrays:
Merge the pairs of subarrays: 
27
,
38
027,38 and 
3
,
43
3,43 to get 
3
,
27
,
38
,
43
3,27,38,43
Merge 
9
,
82
9,82 with 
10
10 to get 
9
,
10
,
82
9,10,82
Final Merge:
Merge the two halves 
3
,
27
,
38
,
43
3,27,38,43 and 
9
,
010
,
82
9,10,82 to get the final sorted array: 
3
,
9
,
10
,
27
,
38
,
43
,
82
3,9,10,27,38,43,82
Now, the array is fully sorted: 
3
,
9
,
10
,
27
,
38
,
43
,
82
3,9,10,27,38,43,82.

'''
