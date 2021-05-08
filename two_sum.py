def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            print(numbers[i], numbers[j])
            if numbers[i]+numbers[j]==target:
                return (i, j)

    