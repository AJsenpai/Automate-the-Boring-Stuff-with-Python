# Author : Ajay 
# Date : 02/20/2020
# Chapter 03: Functions

# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and 
# return this value. If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns 
# the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! 
# Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest 
# impossible math problem.”)
# ########################################################################################################################################

def collatz(number):
    return number//2 if number%2==0 else  3 * (number+1)

while  True:
        try:
            takeval= int(input())
            if collatz(takeval)!=1:
                print(collatz(takeval))
            else:
                print(collatz(takeval))
                break
        except:
            print("The Value must be an integer")   
