
def print_subsequences(arr, index, current_subsequence):
        # Print the current subsequence
        print(current_subsequence)

        # Explore all subsequences that include the element at the current index
        for i in range(index, len(arr)):
                # Include the current element in the subsequence
                current_subsequence.append(arr[i])

                # Recur for the next index
                print_subsequences(arr, i + 1, current_subsequence)

                # Exclude the current element to backtrack and explore other subsequences
                current_subsequence.pop()


print_subsequences([1,2,3],0,[])