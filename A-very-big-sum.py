def aVeryBigSum(ar):
    #ar.remove(ar[0])
    product=0
    for i in ar:
        product=product+i
    return product

ar=[5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))
