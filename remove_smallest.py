def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        removeList=numbers.copy()
        smallestNumber=numbers[0]
        removeIndex=0
        for i in range(len(numbers)):
            if numbers[i]<smallestNumber:
                removeIndex=i
                smallestNumber=numbers[i]
        removeList.pop(removeIndex)
        return removeList