#allows the files to get the exact time and date.
import datetime
now = datetime.datetime.now()

name = input("Hello, Please enter your name: ").upper()#asks the user for their name
print("Hello", name, "what would you like to do")
Which_quiz = input("if you would like to play quiz one, please enter 1, or if you want to play quiz two type 2: ").lower()#Allows tge user to selcet which quiz they play
#allows the user to access all to do with quiz one
if Which_quiz == '1':

#Opens the file where the quiz info is stored
    quiz = open("quiz.txt", "r")#opens the first quizes files
    #set up arrys to store the info from the file for each question.
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []

    #appends the questions from the file to arrays so they can be used for the questions
    q1.append(quiz.read(55))
    q2.append(quiz.read(76))
    q3.append(quiz.read(57))
    q4.append(quiz.read(83))
    q5.append(quiz.read(51))
    q6.append(quiz.read(55))
    q7.append(quiz.read(131))
    q8.append(quiz.read(66))
    q9.append(quiz.read(96))
    q10.append(quiz.read())

    #anwsners for the quiz(q1a = question 1 answers)
    q1a = '1955'
    q2a = 'jupiter'
    q3a = 'pod'
    q4a = 'alexander fleming'
    q5a = '12'
    q6a = 'real'
    q7a = 'copper and tin'
    q8a = 'fungi'
    q9a = 'no charge'
    q10a = 'nitrogen'


    #allows the user to select what they want to do.
    todo = input("For leader board type L or for the quiz type q: ").lower()
    #runs the quiz
    if todo == 'q':

    #sets play to true for the play again feature
        play = True
        score = 0
    #runs a loop while they want to keep playing
        while play:
            print("Question 1: ",q1)
            a1 = input("Answer: ").lower()#sets all answers to lower so cases wont affect score.
            a_no_space1 = a1.strip()#gets rid of any spaces entered in the users anwsers
            if a_no_space1 == q1a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 2: ",q2)
            a2 = input("Answer: ").lower()
            a_no_space2 = a2.strip()
            if a_no_space2 == q2a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 3: ",q3)
            a3 = input("Answer: ").lower()
            a_no_space3 = a3.strip()
            if a_no_space3 == q3a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 4: ",q4)
            a4 = input("Answer: ").lower()
            a_no_space4 = a4.strip()
            if a_no_space4 == q4a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 5: ",q5)
            a5 = input("Answer: ").lower()
            a_no_space5 = a5.strip()
            if a_no_space5 == q5a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 6: ",q6)
            a6 = input("Answer: ").lower()
            a_no_space6 = a6.strip()
            if a_no_space6 == q6a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 7: ",q7)
            a7 = input("Answer: ").lower()
            a_no_space7 = a7.strip()
            if a_no_space7 == q7a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 8: ",q8)
            a8 = input("Answer: ").lower()
            a_no_space8 = a8.strip()
            if a_no_space8 == q8a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 9: ",q9)
            a9 = input("Answer: ").lower()
            a_no_space9 = a9.strip()
            if a_no_space9 == q9a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 10: ",q10)
            a10 = input("Answer: ").lower()
            a_no_space10 = a10.strip()
            if a_no_space10 == q10a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
            #A set of outputs to show you fi=nished the quiz and show score
            print("Well done", name, "you have finished the quiz")
            print("You scored", score, "out of 10")
            savescore = open("leaderBroad.txt", "a")
            savescore.write(str(score))
            savescore.write("=score")
            savescore.write(" ")
            savescore.write(name)
            savescore.write(" ")
            savescore.write(str(now))
            savescore.write('\n')
            savescore.close()
            #ask the user if they want to play again
            again = input("would you like to play agian [Y/N}?: ").lower()
            #if no the program terminates
            if again == 'n':
                play = False
            elif again == 'y':
                #if they do runs the question again and sets score back to 0
                play = True
                score = score-score
            else:
                print("sorry, that is an invaild")
                
    #runs the leaderboards            
    elif todo == 'l':
        #opens a list to display the leaderboard
        scores = []
        #opens the file
        with open('leaderBroad.txt') as sort:
            for line in sort:
                #splits the file
                score = line.split()
                #adds the sorted score to the list
                scores.append((str(score)))

        scores.sort(reverse=True)#sorts the list in reverse so the highest value is firts.
        print(scores)
        
    quiz.close()
    
if Which_quiz == '2':#allows the user to access all of quiz 2
    quiz = open("quiz_two.txt", "r")#opens the second quies file
    #set up arrys to store the info from the file for each question.
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []

    #appends the questions from the file to arrays so they can be used for the questions
    q1.append(quiz.read(56))
    q2.append(quiz.read(48))
    q3.append(quiz.read(82))
    q4.append(quiz.read(113))
    q5.append(quiz.read(66))
    q6.append(quiz.read(76))
    q7.append(quiz.read(72))
    q8.append(quiz.read(104))
    q9.append(quiz.read(67))
    q10.append(quiz.read())

    #anwsners for the quiz(q1a = question 1 answers)
    q1a = '1945'
    q2a = '1760'
    q3a = 'hydrogen'
    q4a = 'winston churchill'
    q5a = 'london'
    q6a = '1985'
    q7a = 'jeff bezos'
    q8a = 'jeff bezos'
    q9a = 'asia'
    q10a = '1919'


    #allows the user to select what they want to do.
    todo = input("For leader board type L or for the quiz type q: ").lower()
    #runs the quiz
    if todo == 'q':

    #sets play to true for the play again feature
        play = True
        score = 0
    #runs a loop while they want to keep playing
        while play:
            print("Question 1: ",q1)
            a1 = input("Answer: ").lower()#sets all answers to lower so cases wont affect score.
            a_no_space1 = a1.strip()
            if a_no_space1 == q1a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 2: ",q2)
            a2 = input("Answer: ").lower()
            a_no_space2 = a2.strip()
            if a_no_space2 == q2a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 3: ",q3)
            a3 = input("Answer: ").lower()
            a_no_space3 = a3.strip()
            if a_no_space3 == q3a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 4: ",q4)
            a4 = input("Answer: ").lower()
            a_no_space4 = a4.strip()
            if a_no_space4 == q4a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 5: ",q5)
            a5 = input("Answer: ").lower()
            a_no_space5 = a5.strip()
            if a_no_space5 == q5a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 6: ",q6)
            a6 = input("Answer: ").lower()
            a_no_space6 = a6.strip()
            if a_no_space6 == q6a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 7: ",q7)
            a7 = input("Answer: ").lower()
            a_no_space7 = a7.strip()
            if a_no_space7 == q7a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 8: ",q8)
            a8 = input("Answer: ").lower()
            a_no_space8 = a8.strip()
            if a_no_space8 == q8a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 9: ",q9)
            a9 = input("Answer: ").lower()
            a_no_space9 = a9.strip()
            if a_no_space9 == q9a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
                
            print("Question 10: ",q10)
            a10 = input("Answer: ").lower()
            a_no_space10 = a10.strip()
            if a_no_space10 == q10a:
                print("correct")
                score = score+1
            else:
                print("sorry that was incorrect")
            #A set of outputs to show you finished the quiz and show score
            print("Well done", name, "you have finished the quiz")
            print("You scored", score, "out of 10")
            savescore = open("leaderBroad2.txt", "a")
            savescore.write(str(score))
            savescore.write("=score")
            savescore.write(" ")
            savescore.write(name)
            savescore.write(" ")
            savescore.write(str(now))
            savescore.write('\n')
            savescore.close()
            #ask the user if they want to play again
            again = input("would you like to play agian [Y/N}?: ").lower()
            #if no the program terminates
            if again == 'n':
                play = False
            elif again == 'y':
                #if they do runs the question again and sets score back to 0
                play = True
                score = score-score
            else:
                print("sorry, that is an invaild answer")
                
    #runs the leaderboards            
    elif todo == 'l':
        #opens a list to display the leaderboard
        scores = []
        #opens the file
        with open('leaderBroad2.txt') as sort:
            for line in sort:
                #splits the file
                score = line.split()
                #adds the sorted score to the list
                scores.append((str(score)))

        scores.sort(reverse=True)#sorts the list in reverse so the highest value is firts.
        print(scores)

    #closes the quiz file   
    quiz.close()
    
else:
    print("That is an invaild answer")
            
       

        