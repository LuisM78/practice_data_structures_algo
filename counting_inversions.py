# Alternative solution to the problem in https://www.geeksforgeeks.org/counting-inversions/

ct=[0]
def MergeSort(arr):
    if len(arr)> 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        MergeSort(left_arr)
        MergeSort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]  < right_arr[j]:
                arr[k]  = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                ct[0] += (mid-i)
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    print("merging",arr,ct[0])
   
arr = [1, 20, 6, 4, 5,7,8,0]
ct=[0]
MergeSort(arr)
arr
ct
Output
#merging [1] 0
#merging [20] 0
#merging [1, 20] 0
#merging [6] 0
#merging [4] 0
#merging [4, 6] 1
#merging [1, 4, 6, 20] 3
#merging [5] 3
#merging [7] 3
#merging [5, 7] 3
#merging [8] 3
#merging [0] 3
#merging [0, 8] 4
#merging [0, 5, 7, 8] 6
#merging [0, 1, 4, 5, 6, 7, 8, 20] 14
[14]
