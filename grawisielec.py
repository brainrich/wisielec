import random
def hangman(wordlist):
    wrong = 0
    stages = ["",
              "_________           ",
              "|                   ",
              "|        |          ",
              "|        0          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   ",
              ]
    rletters = list(wordlist)
    board = ["_"] * len(wordlist)
    win = False
    print("Gra w wisielca")

    while wrong < len(stages) - 1:
        print("\n")
        msg= "Odgadnij literę: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]= char
            rletters[cind]= '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Wygrałeś!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(wordlist))

hangman("rabarbar")