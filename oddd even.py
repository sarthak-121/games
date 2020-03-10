from tkinter import *
import random


root = Tk()
root.title('Odd Even')
root.configure( background='#777E8B')

batting = 0
computer = 0
human = 0
scoreComputer = 0
scoreHuman = 0

LabelComputer = Label(root, text="Computer - {0}".format(scoreComputer), bg="#E71C23").grid(row=1, column=6, sticky=W)
LabelHuman = Label(root, text=" Human - {0}".format(scoreHuman), bg="#E71C23").grid(row=0, column=6, sticky=W)
currentHuman = Label(root, text="Human - {0}".format(human), bg="#F4C724").grid(row=2, column=0, sticky=W)
currentComputer = Label(root, text="Computer - {0}".format(computer), bg="#F4C724").grid(row=2, column=6, sticky=E)


def buttonClicked(button):
    global computer ,human
    computer = random.randint(0, 6)
    if(button['text'] == '0'):
        human =  0
    elif(button['text'] == '1'):
        human = 1
    elif(button['text'] == '2'):
        human = 2
    elif(button['text'] == '3'):
        human = 3
    elif(button['text'] == '4'):
        human = 4
    elif(button['text'] == '5'):
        human = 5
    elif(button['text'] == '6'):
        human = 6

    currentHuman = Label(root, text="Human - {0}".format(human), bg="#F4C724").grid(row=2, column=0, sticky=W)
    currentComputer = Label(root, text="Computer - {0}".format(computer), bg="#F4C724").grid(row=2, column=6, sticky=E)
    check()


def check():
        global batting ,computer ,human ,scoreComputer ,scoreHuman

        if(computer == human and batting <= 1 ):
            out = Label(root, text="Out", bg="#F4C724").grid(row=0+batting, column=5, sticky=W)
            batting += 1
            if(batting == 2):
                checkWin()
        elif(batting == 0):
            scoreHuman += human
            LabelHuman = Label(root, text=" Human - {0}".format(scoreHuman), bg="#E71C23").grid(row=0, column=6, sticky=W)
        elif(batting == 1):
            scoreComputer += computer
            LabelComputer = Label(root, text="Computer - {0}".format(scoreComputer), bg="#E71C23").grid(row=1, column=6, sticky=W)


def checkWin():
    if(scoreComputer == scoreHuman):
        result = Label(root, text="Draw", bg="#45CE30").grid(row=2, column=2, sticky=W)
    elif(scoreHuman > scoreComputer):
        result = Label(root, text="You Win!!", bg="#45CE30").grid(row=2, column=2, sticky=W)
    elif(scoreComputer > scoreHuman):
        result = Label(root, text="computer Wins!!", bg="#45CE30").grid(row=2, column=2, sticky=W)

def restart():
    global batting, computer, human, scoreComputer, scoreHuman
    batting = 0
    computer = 0
    human = 0
    scoreComputer = 0
    scoreHuman = 0
    LabelComputer['text'] = '0'
    LabelHuman['text'] = '0'
    currentComputer['text'] = 0
    currentHuman['text'] = 0
    result['text'] = ' '
    out['text'] = ' '



button0 = Button(root, text='New Game', height=2, font=("Verdana", "10", "bold"), width=8, command=lambda: restart(), bg="#0ABDE3")
button0.grid(row=0, column=0, sticky=W)

button1 = Button(root, text='0', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button1), bg="#0ABDE3")
button1.grid(row=5, column=0, sticky=NSEW)
button2 = Button(root, text='1', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button2), bg="#0ABDE3")
button2.grid(row=5, column=1, sticky=NSEW)
button3 = Button(root, text='2', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button3), bg="#0ABDE3")
button3.grid(row=5, column=2, sticky=NSEW)
button4 = Button(root, text='3', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button4), bg="#0ABDE3")
button4.grid(row=5, column=3, sticky=NSEW)
button5 = Button(root, text='4', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button5), bg="#0ABDE3")
button5.grid(row=5, column=4, sticky=NSEW)
button6 = Button(root, text='5', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button6), bg="#0ABDE3")
button6.grid(row=5, column=5, sticky=NSEW)
button7 = Button(root, text='6', height=5, font=("Verdana", "5", "bold"), width=5, command=lambda: buttonClicked(button7), bg="#0ABDE3")
button7.grid(row=5, column=6, sticky=NSEW)

root.mainloop()
