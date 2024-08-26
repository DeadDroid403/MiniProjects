#! /usr/bin/python3
# tic tac toe game
import sys

list1 = ["1","2","3"]
list2 = ["4","5","6"]
list3 = ["7","8","9"]
print(list1)
print(list2)
print(list3)

def player1():
    number = input("Player O , Enter A Number: ")
    if number in list1:
        index = list1.index(number)
        list1.pop(index)
        list1.insert(index, "O")
        print(list1)
        print(list2)
        print(list3)
    elif number in list2:
        index = list2.index(number)
        list2.pop(index)
        list2.insert(index, "O")
        print(list1)
        print(list2)
        print(list3)
    elif number in list3:
        index = list3.index(number)
        list3.pop(index)
        list3.insert(index, "O")
        print(list1)
        print(list2)
        print(list3)
    else:
        print("Worng Number...")
        player1()

def player2():
    number2 = input("Player X , Enter A Number: ")
    if number2 in list1:
        index = list1.index(number2)
        list1.pop(index)
        list1.insert(index, "X")
        print(list1)
        print(list2)
        print(list3)
    elif number2 in list2:
        index = list2.index(number2)
        list2.pop(index)
        list2.insert(index, "X")
        print(list1)
        print(list2)
        print(list3)
    elif number2 in list3:
        index = list3.index(number2)
        list3.pop(index)
        list3.insert(index, "X")
        print(list1)
        print(list2)
        print(list3)
    else:
        print("Wrong Number...")
        player2()

for i in range(9):
    if "X" in list1 and list1[0] == list1[1] == list1[2]:
        print("X is the Winner....")
        sys.exit()
    if "X" in list2 and list2[0] == list2[1] == list2[2]:
        print("X is the Winner....")
        sys.exit()
    if "X" in list3 and list3[0] == list3[1] == list3[2]:
        print("X is the Winner....")
        sys.exit()
    if "X" in list1 and list1[0] == list2[0] == list3[0]:
        print("X is the Winner....")
        sys.exit()
    if "X" in list2 and list2[1] == list1[1] == list3[1]:
        print("X is the Winner....")
        sys.exit()
    if "X" in list3 and list1[2] == list2[2] == list3[2]:
        print("X is the Winner....")
        sys.exit()
    if "X" == list1[0] and "X" == list2[1] and "X" == list3[2]:
        print("X is the Winner....")
        sys.exit()
    if "X" == list1[2] and "X" == list2[1] and "X" == list3[0]:
        print("X is the Winner....")
        sys.exit()
####################################################################
    if "O" in list1 and list1[0] == list1[1] == list1[2]:
        print("O is the Winner....")
        sys.exit()
    if "O" in list2 and list2[0] == list2[1] == list2[2]:
        print("O is the Winner....")
        sys.exit()
    if "O" in list3 and list3[0] == list3[1] == list3[2]:
        print("O is the Winner....")
        sys.exit()
    if "O" in list1 and list1[0] == list2[0] == list3[0]:
        print("O is the Winner....")
        sys.exit()
    if "O" in list2 and list2[1] == list1[1] == list3[1]:
        print("O is the Winner....")
        sys.exit()
    if "O" in list3 and list1[2] == list2[2] == list3[2]:
        print("O is the Winner....")
        sys.exit()
    if "O" == list1[0] and "O" == list2[1] and "O" == list3[2]:
        print("O is the Winner....")
        sys.exit()
    if "O" == list1[2] and "O" == list2[1] and "O" == list3[0]:
        print("o is the Winner....")
        sys.exit()
    if i%2==0:
        player1()
    else:
        player2()