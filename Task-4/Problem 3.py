from importlib import import_module
from turtle import pd
import pandas              # import pandas to make table
criteria=["R.No.","Name","Marks"]     #criteria list

marksheet=[]
no_of_criterion=3
no_of_students=int(input("Enter number of students: "))
Sno=[k for k in range(no_of_students) ]
for i in range (no_of_criterion):
    marksheet.append([])
    for j in range(0,no_of_students):
        Enter_details=input("Enter details of each student in R.No., Name, Marks order only: ")
        marksheet[i].append(Enter_details)          

print("part1")
pd = pandas.DataFrame(marksheet,Sno,criteria,)
print(pd)

print("part 2")
print(marksheet[1])

