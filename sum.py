def simpleArraySum(ar):
    product = 0
    for i in ar:
        product = product + i
        
    return product

na = [1,2,3,4]
print(simpleArraySum(na))


from functools import reduce

product = reduce((lambda x,y: x+y), na)
print(product)