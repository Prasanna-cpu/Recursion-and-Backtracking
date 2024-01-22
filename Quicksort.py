

def QuickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]

        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]

        return QuickSort(less_than_pivot) + [pivot] + QuickSort(greater_than_pivot)


arr=[5,12,1,8,4]

arr=QuickSort(arr)

print(arr)
