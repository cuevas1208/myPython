def sortList(listLengh):
    listValues.sort(key=str.lower)
    tempString = ""
    for counter in range(0,len(listValues),1):
        tempString = tempString + listValues[counter] +', '
    return tempString

while True:
    print ('how many members on the list?')
    try:
        listLenght = int(input())
        break
    except ValueError:
        pass
        print ('Error: enter a decimal number')

    
print ('enter a member of the list')
listValues = [input(),]
for counter in range(1,listLenght,1):
    listValues.append(input())

stringList = sortList(listValues)
print (stringList)
