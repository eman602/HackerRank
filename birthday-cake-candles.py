def birthdayCakeCandles(candles):
    count=0
    themax = max(candles)
    for i in candles:
        if i==themax:
            count+=1

    print(count)





candles=[4,4,1,3]

birthdayCakeCandles(candles)
