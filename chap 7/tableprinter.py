# Date: 03/03/2020
# Topic: Manipulating Strings 

### Practice Project ###
# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column 
# right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# Your printTable() function would print the following:

#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose
# ###################################################################################################################################### 

tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(dataLists):
    colWidths = [0] * len(dataLists)  # will give [0,0,0] since list of lists has 3 list inside
    for i in colWidths:
        colWidths = max(dataLists[i], key=len)  # will give the word with max len for ex in 1 list = cherries 
        
        
           
    y = len(colWidths) # will print the length of max word for ex cherries has the length of 8
    num_of_lists = len(dataLists)           #3
    items_in_lists = len(dataLists[0])      #4
    
# this is important step as this loop will iterate apples(0,0) Alice(1,0) dogs(2,0)
#     for x in range(len(dataLists[0])):  
#         print(str(dataLists[0][x]).rjust(y) + str(dataLists[1][x]).rjust(y) + str(dataLists[2][x]).rjust(y))
     
    for col in range(items_in_list):
        for row in range(num_of_lists):
            print(str(dataLists[row][col].rjust(y)), end=" ")
        print(" ")
        

printTable(tableData)
