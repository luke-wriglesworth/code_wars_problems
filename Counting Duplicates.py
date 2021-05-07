def duplicate_count(text):
    textLower=text.lower()
    dupedList=[]
    for i in range(len(textLower)):
        countOfEachChar=textLower.count(textLower[i])
        print(textLower[i], countOfEachChar)
        if countOfEachChar>1 and dupedList.count(textLower[i])==0:
            dupedList.append(textLower[i])
    return len(dupedList)





