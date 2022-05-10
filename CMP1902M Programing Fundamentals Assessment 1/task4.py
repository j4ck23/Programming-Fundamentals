'''Task 4, take a string and turn it into pig latin'''
def pig_latin():
    #take a word as a user input and splits it in to seperate words
    sentence = str(input("Please enter a sentence: ")).split()
    #sets a vairable to add ay to the end of the word
    end = 'ay'
    #a for loop to do this process for all the words inputed
    for word in sentence:
        #takes the first later of the word and moves it to the end
        pigLatin = (word[1:] + word[0])
        #adds the pre made end viarble that contains ay to the end of the word
        pigLatin = pigLatin + end
        #prints out the new words on one line till a blank is returned
        print(pigLatin, end = ' ')
        
pig_latin()