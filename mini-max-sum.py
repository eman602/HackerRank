def miniMaxSum(arr):
    arr.sort()
    print(arr)
    newlist=[]
    for i in arr:
        newlist.append(i)

    newlist.remove(newlist[0])
    result1=0
    result2=0
    for i in newlist:
        result1+=i
    #print(result1)

    arr.remove(arr[len(arr)-1])
    for j in arr:
        result2+=j

    print(result2, result1)




arr=[1,3,7,5,9]
miniMaxSum(arr)