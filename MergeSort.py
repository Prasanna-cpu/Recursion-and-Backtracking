

def merge(arr,left,right):


    i=j=k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1

        else:
            arr[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

def MergeSort(arr):

    if len(arr)>1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        MergeSort(left)
        MergeSort(right)

        merge(arr, left, right)

arr=[4,3,9,10,7,18,5]
MergeSort(arr)


print(arr)

