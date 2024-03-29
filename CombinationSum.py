

def CombinationSum(candidates,target):
    def backtrack(start,target,path):
        if target==0:
            result.append(path[:])
            return

        for i in range(start,len(candidates)):
            if target-candidates[i]>=0:
                path.append(candidates[i])
                backtrack(i,target-candidates[i],path)
                path.pop()

    candidates.sort()
    result=[]
    backtrack(0,target,[])
    return result




if __name__=='__main__':
    print(CombinationSum([2,3,6,7],7))