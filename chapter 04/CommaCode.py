# Date: 02/24/2020
# Chapter: List


# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, 
# tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty 
# list [] is passed to your function.

########################################################################################################################################

def sentence_maker(mylist):
    
    
    sentence=''
    for i in range(0,len(mylist)-1):
        sentence+=mylist[i]+', '
    try:
        sentence+='and '+mylist[-1]
    except:
        print('[]')
    else:
        if len(mylist)==1:
            print(mylist[0])
        else:
            print(sentence)
    
    another approach
    if len(mylist)==1:
        print(mylist[0])
    else:
        mylist.insert(len(mylist)-1,'and')
        print(*mylist, sep=', ')
    
    
    
spam = ['apples', 'bananas', 'tofu', 'cats' , 'eggs' , 'ketchup']  #testcase1
spam = ['apples', 'oranges' , 'eggs']                              #testcase2
spam= []                                                           #testcase3

sentence_maker(spam)
