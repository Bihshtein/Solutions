def sort(arr):
    for j in range(1,len(arr)):
        for i in range(0,len(arr)-j):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def pair_sum(arr,sum):
    start = 0
    end = len(arr)-1
    while (start != end):
        if (arr[start] + arr[end] > sum):
            end -=1
        elif (arr[start] + arr[end] < sum):
            start +=1
        else :
            return (arr[start], arr[end])
    return None
    
arr = sort([-1,5,1,4,3])
print pair_sum(arr,2)

	