# Date: 03/03/2020
# Topic: Manipulating Strings



tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(dataLists):
    colWidths = [0] * len(dataLists)
    for i in colWidths:
        colWidths = max(dataLists[i], key=len)
        
        
           
    y = len(colWidths)
    
        
    for x in range(len(dataLists[0])):
        print(str(dataLists[0][x]).rjust(y) + str(dataLists[1][x]).rjust(y) + str(dataLists[2][x]).rjust(y))


printTable(tableData)
