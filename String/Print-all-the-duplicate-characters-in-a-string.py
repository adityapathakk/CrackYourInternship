def printDuplicates(str):
    charList = sorted(str) # converting string to sorted list of characters
    print(charList)
    
    i = 0 # loop through sorted list to find duplicates
    while i < len(charList):
        count = 1
        
        # counting the occurrences of each character
        while i < len(charList) - 1 and charList[i] == charList[i + 1]:
            count += 1
            i += 1
        
        # printing the duplicate character and its count
        if count > 1:
            print(charList[i], ", count = ", count)
        i += 1

testStr = "test string"
printDuplicates(testStr)