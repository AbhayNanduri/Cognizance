string = input("Enter a string: " )    #takes string input
n=len(string)                          #variable storing lenght of the string
i=0                                    #a variable is made for the string index and initialized at 0
while i<n:                             #while loop is started and the loop goes on until index is less than n(since the string numbering starts from 0)
    print(string[i],end='')            #prints the letter corresponding to the string at index i and end parameter is set to no space so that the next inputs dont go into other line 
    i+=2                               # i is incremented by 2 each time
