from tkinter import *
from Prob1_source import Prob1Ans
from Prob2_source import Prob2Ans
from Prob3_source import Prob3Ans
from Prob4_source import Prob4Ans
from Prob5_source import Prob5Ans
from Prob6_source import Prob6Ans
from Prob7_source import Prob7Ans


# ===================================================================== #
# 4 Things to change (for adding new problem):                          #
# import module (make module first, named Probn_Ans)                    #
# def Probn():                          > copy from def Prob1():        #
# reveal answer (elif prob...)          > copy from Problem 2           #
# and check answer (elif prob...)       > copy from Problem 2           #
# ===================================================================== #


def Prob1():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\n\n\nIf we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.\n\n\n\n\n\n")
    prob_number.config(text="Problem 1")

    if var.get() == 1:
        main = Prob1Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob2():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\nEach new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:\n\n1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.\n\n\n")
    prob_number.config(text="Problem 2")

    if var.get() == 1:
        main = Prob2Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob3():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\n\n\nThe prime factors of 13195 are 5, 7, 13 and 29.\n\n                        What is the largest prime factor of the number 600851475143 ?                       \n\n\n\n\n")
    prob_number.config(text="Problem 3")

    if var.get() == 1:
        main = Prob3Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob4():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\n\nA palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\n\nFind the largest palindrome made from the product of two 3-digit numbers.\n\n\n\n\n")
    prob_number.config(text="Problem 4")

    if var.get() == 1:
        main = Prob4Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob5():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\n\n2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\n\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n\n\n\n")
    prob_number.config(text="Problem 5")

    if var.get() == 1:
        main = Prob5Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob6():
    # Change this (Adjust spacing too)
    question.config(text="\nThe sum of the squares of the first ten natural numbers is,\n1^2 + 2^2 + ... + 10^2 = 385\n\nThe square of the sum of the first ten natural numbers is,\n(1 + 2 + ... + 10)^2 = 55^2 = 3025\n\nHence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.\n\nFind the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n")
    prob_number.config(text="Problem 6")

    if var.get() == 1:
        main = Prob6Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob7():
    # Change this (Adjust spacing too)
    question.config(text="\n\n\n\nBy listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\n\nWhat is the 10,001st prime number?\n\n\n\n\n")
    prob_number.config(text="Problem 7")

    if var.get() == 1:
        main = Prob7Ans()
    # until here
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="brown")
        user_answer.config(bg="brown")
        answer.config(bg="brown")
    else:
        answer.config(text="The answer will be shown here")
        answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)
        frame.config(bg="darkGray")
        user_answer.config(bg="darkGray")
        answer.config(bg="darkGray")


def Prob8():
    pass


def Prob9():
    pass


def Prob10():
    pass


def reveal_answer():
    if prob_number["text"] == "Problem 1":
        Prob1()
    elif prob_number["text"] == "Problem 2":
        Prob2()
    elif prob_number["text"] == "Problem 3":
        Prob3()
    elif prob_number["text"] == "Problem 4":
        Prob4()
    elif prob_number["text"] == "Problem 5":
        Prob5()
    elif prob_number["text"] == "Problem 6":
        Prob6()
    elif prob_number["text"] == "Problem 7":
        Prob7()


def check_answer():
    if prob_number["text"] == "Problem 1":
        main = Prob1Ans()
    elif prob_number["text"] == "Problem 2":
        main = Prob2Ans()
    elif prob_number["text"] == "Problem 3":
        main = Prob3Ans()
    elif prob_number["text"] == "Problem 4":
        main = Prob4Ans()
    elif prob_number["text"] == "Problem 5":
        main = Prob5Ans()
    elif prob_number["text"] == "Problem 6":
        main = Prob6Ans()
    elif prob_number["text"] == "Problem 7":
        main = Prob7Ans()

    if str(main.answer) == user_answer_field.get():
        user_answer_field.delete(0, END)
        user_answer_field.insert(0, "CORRECT!")
        answer.config(text=main.answer)
        answer.place(x=winwidth / 2 - str_offset(answer), y=winheight - 20)
        frame.config(bg="green")
        user_answer.config(bg="green")
        answer.config(bg="green")

    else:
        user_answer_field.delete(0, END)
        user_answer_field.insert(0, "FALSE!")
        frame.config(bg="red")
        user_answer.config(bg="red")
        answer.config(bg="red")


def str_offset(label):
    return 2.8 * len(str(label["text"]))


# ------------------------------------------------------------------------------------- #
#                     CODE BELOW NO NEED TO BE CHANGED. IT'S THE UI                     #
# ------------------------------------------------------------------------------------- #


# Start
window = Tk()
window.title("Project Euler")
winwidth = 500
winheight = 300

# Create a blank window
frame = Frame(window, width=winwidth, height=winheight, bg="darkGray")
frame.pack()

# Create menu on top
menu = Menu(window)
window.config(menu=menu)

# Create submenu 1 with dropdown list
sub01_05 = Menu(menu)
menu.add_cascade(label="Prob 1 - 5", menu=sub01_05)
sub01_05.add_command(label="Prob 1", command=Prob1)
sub01_05.add_command(label="Prob 2", command=Prob2)
sub01_05.add_command(label="Prob 3", command=Prob3)
sub01_05.add_command(label="Prob 4", command=Prob4)
sub01_05.add_command(label="Prob 5", command=Prob5)

# Create submenu 2 with dropdown list
sub06_10 = Menu(menu)
menu.add_cascade(label="Prob 6 - 10", menu=sub06_10)
sub06_10.add_command(label="Prob 6", command=Prob6)
sub06_10.add_command(label="Prob 7", command=Prob7)
sub06_10.add_command(label="Prob 8", command=Prob8)
sub06_10.add_command(label="Prob 9", command=Prob9)
sub06_10.add_command(label="Prob 10", command=Prob10)


# Now working with content
# Text on upper left
prob_number = Label(window, text="Problem 0", font=("Courier", 15), bg="darkGray", fg="red")
prob_number.place(x=10, y=10)

# The Question
question = Message(window, text="\n\n\n\n\n\n                                                    The question will be shown here                                               \n\n\n\n\n\n", width=winwidth - 20, bg="lightGray", justify=CENTER)
question.place(x=10, y=10)

# User Answer goes here
user_answer = Label(window, text="Your Answer", bg="darkGray")
user_answer.place(x=winwidth / 2 - 175, y=winheight - 77)

user_answer_field = Entry(window)
user_answer_field.place(x=winwidth / 2 - 100, y=winheight - 75)

# Button to check answer
check_answer_button = Button(window, text="Check", command=check_answer, height=3, width=15)
check_answer_button.place(x=winwidth / 2 + 30, y=winheight - 78)

# Checklist to reveal answer
var = IntVar()
ansbutton = Checkbutton(window, text="Reveal the answer anyway", command=reveal_answer, variable=var)
ansbutton.place(x=winwidth / 2 - str_offset(ansbutton) - 75, y=winheight - 50)

# The Answer
answer = Label(window, text="The answer will be shown here", bg="darkGray", font=("Arial Bold", 8))
answer.place(x=winwidth / 2 - str_offset(answer) - 15, y=winheight - 20)


window.mainloop()
