"""Task 1:Write a function that puts string a and string b together"""
def str_abba():

    #Ask the user to input the first string
    strA = input("please input a word: ")

    #Ask the user to input a second string
    strB = input("please input another word: ")

    #add the two strings together
    strAdd = strA + strB + strB + strA

    #Display added value
    return(strAdd)

str_abba(strADD)