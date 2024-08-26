f = open("file.txt","r")
r = f.readlines()
ls = []
for i in r:
    g=i[0:-1:1]
    ls.append(g)
##################################

print("Welcome To The WordGame\n")
wrd1 = "a"
wrd2 = "a"
score1 = 0
score2 = 0

while True:

    wrd1 = input(f"Player 1 -- Enter Your Word Starts With {wrd2[-1]}: ")

    if wrd1 in ls:
        print("Correct!")
        score1 += 1
        ls.remove(wrd1)
        print("Player 1 score =", score1)

    else:
        print("Incorrect... Player 1 loses :(")
        print(f"player 1 score =",{score1})
        print(f"player 2 score =", {score2})
        break

    wrd2 = input(f"Player 2 -- Enter A Word Starts With {wrd1[-1]}: ")

    if wrd2 in ls:
        print("Correct!")
        score2 += 1
        print("Player 2 score =", score2)

    else:
        print("Incorrect... Player 2 loses :(")
        print(f"player 1 score =", {score1})
        print(f"player 2 score =", {score2})
        break
