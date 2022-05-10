'''Task 5, count the frequency of each letter in the word and display in descending order'''
def cal_frequncey():
    #allows the program to tell what 
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #gets a users inout and stores it as a string.
    sentence = str(input("please enter a sentence: ")).lower()
    #opens an array to sotre the frequency in so it can be sorted later
    freq = [ ]
    #runs through for each letter of the alphabet for every letter in the string
    for i in range(0,26):
        #adds one to the count for each letter that is in the string
        freq_count = (sentence.count(alphabet[i]))
        #checks to see if the letter has a frequency greater than 0
        if freq_count > 0:
            #collects the letter and the frequency of it and stores it togehter
            freq_sort = (freq_count, '=', alphabet[i])
            #adds this to the freqency list to be sorted
            freq.append(freq_sort)
    #sort the frequency list in order from biggest to smallest        
    freq.sort(reverse = True)
    print (freq)
    
cal_frequncey()