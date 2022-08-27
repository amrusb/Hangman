from random import randint
from re import search

NUM_OF_NOUNS = 100
GALLOW = [
    "     ╔═══╗",    # 7-10
    "     ║   O",    # 8-10
    "     ║  /│\\",  # 9-10
    "     ║  / \\",  # 10
    "     ║    ",    # 2-6
    " ════╩═════"   # 1-10
]

class Game:
    def __init__(self):
        self.word = wordDraw()
        self.guess = settingLines(self.word)
        self.usedLetters = []
        self.fails = 0
    
    def printGuess(self):
        for item in self.guess:
            print(item, end=" ")
        print()
    
    def drawGallow(self):
        print()
        if self.fails == 1:
            print(GALLOW[-1], end="\t")
            self.printGuess()
        elif self.fails > 1 and self.fails < 7:
            for i in range(self.fails - 1):
                print(GALLOW[-2])
            print(GALLOW[-1], end="\t")
            self.printGuess()
        elif self.fails == 7:
            print(GALLOW[0])
            for i in range(self.fails - 2):
                print(GALLOW[-2])
            print(GALLOW[-1], end="\t")
            self.printGuess()
        elif self.fails == 8:
            print(GALLOW[0])
            print(GALLOW[1])
            print(GALLOW[-2])
            print(GALLOW[-2])
            print(GALLOW[-2])
            print(GALLOW[-1], end="\t")
            self.printGuess()
        elif self.fails == 9:
            print(GALLOW[0])
            print(GALLOW[1])
            print(GALLOW[2])
            print(GALLOW[-2])
            print(GALLOW[-2])
            print(GALLOW[-1], end="\t")
            self.printGuess()
        elif self.fails == 10:
            print(GALLOW[0])
            print(GALLOW[1])
            print(GALLOW[2])
            print(GALLOW[3])
            print(GALLOW[4])
            print(GALLOW[-1], end="\t")
            self.printGuess()
            
def gameInfo():
    print("""┌───────────────────────────────────────────────┐
│                                               │
│   ║   ║ ╔═══╗ ╔═══╗ ╔═══╗ ╔═╦═╗ ╔═══╗ ╔═══╗   O
│   ╠═══╣ ╠═══╣ ║   ║ ║  ═╗ ║ ║ ║ ╠═══╣ ║   ║  /│\\
│   ║   ║ ║   ║ ║   ║ ╚═══╝ ║ ║ ║ ║   ║ ║   ║  / \\
│                                               
└────────────────────────────────────────────────
    """)
    print("Welcome in 'Hangman' game!")
    print("To win this game you have to guess a word letter by letter. To do this you have 10 changes.")
    print("Good luck!\n")
    print("made by: Batosz Surma")
    print("github: @amrusb\n")

def wordDraw():
    num = randint(1, NUM_OF_NOUNS)
    word = ''
    with open("nouns.txt", 'r') as nounsFile:
        for i in range(1, num):
            nounsFile.readline()
        word = nounsFile.readline()
    return word

def settingLines(word):
    lines = []
    for c in word:
        if c.isalpha():
            lines.append('_')
    return lines

def takingGuess(game):
    c = input("\nEnter a letter:\n>>>\t")
    c = c.lower()
    #wrong input
    while len(c) != 1 or c.isdigit():
        c = input("\nError! Try again:\n>>>\t")
    #letter is used
    while c in game.usedLetters:
        c = input("\nThis letter has been used. Try again:\n>>>\t")
    game.usedLetters.append(c)
    return c

def checkGuess(game, letter):
    if letter in game.word:
        for i in range(len(game.word)):
            if(game.word[i] == letter):
                game.guess[i] = letter
        game.drawGallow()
    else:
        game.fails += 1
        game.drawGallow()

def checkGame(game):
    if game.fails == 10:
        print("Unfortunately you weren't able to guess the word.")
        print("Word to guess during this game: {}".format(game.word))
        return True
    else:
        for i in range(len(game.word) - 1):
            if game.word[i] != game.guess[i]:
                return False
    print("Congratulations! You have guessed the word!")
    return True

gameInfo()
while(True):
    menu = 0
    while(True):
        try:
            menu = int(input("Press:\n[1] to start the game\n[2] to quit\n>>>\t"))
            if menu > 2 or menu < 1:
                print("Entered wrong input!\n")
                continue
            else:
                break
        except ValueError:
            print("Entered wrong input!\n")
            continue
    if menu == 2:
        print("Game has been ended.")
        print("See you again!")
        break
    gamePlay = Game()   
    print() 
    gamePlay.printGuess()
    end = False
    while(not end):
        print()
        letter = takingGuess(gamePlay)
        checkGuess(gamePlay, letter)
        end = checkGame(gamePlay)
