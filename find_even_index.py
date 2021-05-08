def find_even_index(arr):
    for i in range(len(arr)):
        splitLeft=arr[:i]
        splitRight=arr[i+1:]
        totalLeft=sum(splitLeft)
        totalRight=sum(splitRight)
        print('index: ', i)
        print('left total: ', totalLeft)
        print('right total: ', totalRight)
        if totalLeft==totalRight:
            return i
    return -1
