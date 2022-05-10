def no_three_sum(number1, number2, number3):
               
               # call the fix_three function to 'fix' the three numbers...
               output1 = fix_three(number1)
               output2 = fix_three(number2)
               output3 = fix_three(number3)
 
               # add the outputs together and print to the screen...
               total = output1 + output2 + output3
               print(total)

def fix_three(number):
               
               # calcualtions for number...
               #checks if number is between 20 and 30
               if number >= 20 and number <= 29:
                   #if yes return number regardless
                    output = number
               
               
            #if not between 20 and 30,check if number divisable by 3
               elif not number % 3:
                   #if so set number top 0
                    output = 0
               
               else:
                   #if not divisable by 3 return the number
                    output = number
               #returns the number calculated by the function               
               return output
#takes three user inputs
number1 = int(input("Please enter a 1st number:"))
number2 = int(input("Please enter a 2nd number:"))
number3 = int(input("Please enter a 3rd number:"))
#runs the function with the three user inputs.
no_three_sum(number1, number2, number3)