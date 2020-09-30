
def diagonalDifference(arr):
    mylist=[]
    secondlist=[]
    count=0
    m1 =0
    m2=0
    scount=len(arr)-1
    for i in range(len(arr)):
        if count<len(arr):
            mylist.append(arr[i][count])
            count=count+1
    #print(mylist)

    for i in range(len(arr)):
        secondlist.append(arr[i][scount])
        scount=scount-1
    #print(secondlist)
        
    for j in mylist:
        m1=m1+j
        abs(m1)

    for m in secondlist:
        m2=m2+m
        abs(m2)
    
    return abs(m1-m2)
