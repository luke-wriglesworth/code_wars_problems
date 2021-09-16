def gimme(input_array):
    sorted_array=[]
    sorted_array=sorted(input_array)
    middle_number=sorted_array[1]

    for i in range(0,len(input_array)):
        if input_array[i]==middle_number:
            return i
