st = input("do you want to play the game,(yes or no):- ")

if st == "yes" :
    print("ok! Let's begin ")
elif st == "no" :
    exit()
else:
    print("invalid statement")
    exit()

print("welcome to the word guess game.")
print("we will give you the length of the word and you have three chances to guess it right")

words = ["table","window","knife","almira","terrace","floor","bathroom","toilet"]
import random

mw = random.choice(words)
l = len(mw)
print("The length of the word is:- ", l)
print("The word starts with :- " , mw[0])

count = 0

while count < 3:
    usr = input("guess the name:- ")
    if usr == mw:
        count += 1
        print("congratulations ! You got it right in", count)
        exit()

    elif usr != mw:
        print("sorry ! that's wrong:")
        count += 1
        print("you have",3 - count,"chances left.")
        if count == 1:
            print("the word starts with these two character :-",mw[0]+mw[1])
        elif count == 2:
            print("the word has these three characters in starting :-",mw[0]+mw[1]+mw[2])
        elif count == 3:
            print("well tried ! but you losed the game")
            print("the right word was - ",mw)





