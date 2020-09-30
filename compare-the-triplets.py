a=[17,28,30]
b=[99,16,8]
alice=0
bob=0


for i in range(len(a)):
    if a[i]>b[i]:
        alice=alice+1
    if a[i]<b[i]:
        bob=bob+1
    if a[i]==b[i]:
        alice=alice+0
        bob=bob+0

#print(alice, " ", bob)
    
    

def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice=alice+1
        if a[i]<b[i]:
            bob=bob+1
        if a[i]==b[i]:
            alice=alice+0
            bob=bob+0
    return alice, bob 

print(compareTriplets(a,b))