n=5  #No. of stars on each side of the pyramid
s= n-1 # No. of spaces before the star in each line

for i in range(0,5): #outer loop for no. of rows
    for j in range(0,s): #inner loop for no. of spaces. Values change according to s
        print(end=" ")
    s-=1   #decrementing k after each loop so that we dont get the stars start in a straight line 
    for j in range(0,i+1):   #inner loop for no. of rows and printing stars 
        print("* ",end="")
    print("\r")    # using carriage return to print the different steps of loop in different line. I'd recommend commenting out this line to see diffrence