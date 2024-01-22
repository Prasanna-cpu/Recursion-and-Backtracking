

def SubsequenceSum(arr,index,current_subsequence,k,current_sum):
    if current_sum==k:
        print(current_subsequence)

    for i in range(index,len(arr)):

        current_subsequence.append(arr[i])


        SubsequenceSum(arr,i+1,current_subsequence,k,current_sum+arr[i])

        current_subsequence.pop()

SubsequenceSum([1,2,3,4,5],0,[],5,0)



