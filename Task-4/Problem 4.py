n=int(input("Enter the number:"))    #Takes input
a=n                                  # we create a temporary variable to store n
b=0                                  # we create a different variable which is meant to store the reverse of the number and initialize it at 0
while(n>0):                          # we start a while loop to start the process of storing the number
    x=n%10                           # we make a variable x to store the modulus operation on n wrt 10 so we get the last digit
    b=b*10+x                         # we take the obtained digit and add it to b keeping in mind the place value of the digit x in further iterations of the loop
    n=n//10                          # we divide the number n by 10 using // to obtain the the number on which we do the next iteration. this goes until the number n becomes 0 i.e there are no numbers left to iterate
if(a==b):                            # the obtained b is the reverse of number n stored as a so for n to be a palindrome a must be equal to b so we check it using if statement
    print("True") 
else:
    print("False")