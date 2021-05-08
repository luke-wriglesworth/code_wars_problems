def high_and_low(numbers):  
    stringArray=numbers.split()
    intArray=[int(i) for i in stringArray]
    intArray.sort()
    return str(intArray[len(intArray)-1]) + ' ' + str(intArray[0])




