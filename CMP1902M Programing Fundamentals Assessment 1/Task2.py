"""Task 2: write a function that compares the age of a user with your age"""

def compare_ages():
    #Take the users age
    my_age = 18
    #take the age that ypou want to compare to
    user_age = int(input("Please enter your age: "))
    #compare the ages
    #the same age
    if my_age == user_age:
        print("You are the same age as me")
        #if the user is one year younger
    elif user_age < my_age:
        #work out the difference in age
        age_diff_younger = my_age - user_age
        #if younger by one print year instead of years
        #display if they are younger
        if age_diff_younger == 1:
            print("you are", age_diff_younger, "year younger than me")
            #else print years
        else:
            print("You are", age_diff_younger, "years younger than me")
        #if the user is two years older
    elif user_age > my_age:
        #work out the difference in age
        age_diff_older = user_age - my_age
        #if older by one print year instead of years
        #display if they are older
        if age_diff_older == 1:
            print("you are", age_diff_older, "year older than me")
        else:
            #if the user is two years older
            print("you are", age_diff_older, "years older than me")
            
compare_ages()