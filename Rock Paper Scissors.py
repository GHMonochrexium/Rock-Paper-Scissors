import tkinter as tk
import random
CPUChoice = ["Rock","Paper","Scissors"]
screen = tk.Tk()
screen.title("Rock Paper Scissors")
screen.geometry("400x400")
screen.config(bg="grey")
score = 0
cpuscored = 0
def Rock():
    global CPUChoice
    CPUChoice = random.choice(CPUChoice)
    if CPUChoice == "Rock":
        result_label.config(text="It's a tie!")
    elif CPUChoice == "Paper":
        result_label.config(text="CPU wins!")
    else:
        result_label.config(text="Player wins!")
    Score()




def Paper():
    global CPUChoice
    CPUChoice = random.choice(CPUChoice)
    if CPUChoice == "Rock":
        result_label.config(text="Player wins!")
    elif CPUChoice == "Paper":
        result_label.config(text="It's a tie!")
    else:
        result_label.config(text="CPU wins!")
    Score()


def Scissors():
    global CPUChoice
    CPUChoice = random.choice(CPUChoice)
    if CPUChoice == "Rock":
        result_label.config(text="CPU wins!")
    elif CPUChoice == "Paper":
        result_label.config(text="Player wins!")
    else:
        result_label.config(text="It's a tie!")
    Score()

def Score():
    global score,cpuscored
    if result_label.cget("text") == "Player wins!":
        score += 1
        playerscore.config(text="Player Score: " + str(score))
    elif result_label.cget("text") == "CPU wins!":
        cpuscored += 1
        cpuscore.config(text="CPU Score: " + str(cpuscored)) 

label1 =   tk.Label(screen, text="Welcome to Rock Paper Scissors!", font=("Arial", 16), bg="grey")
label1.place(x=50, y=50)
label2 = tk.Label(screen, text="Choose your option:", font=("Arial", 14), bg="grey")
label2.place(x=50, y=80)
rock = tk.Button(screen, text="Rock", font=("Arial", 14), bg="white", command=Rock)
rock.place(x=50, y=150)
paper = tk.Button(screen, text="Paper", font=("Arial", 14), bg="blue", command=Paper)
paper.place(x=150, y=150)
scissors = tk.Button(screen, text="Scissors", font=("Arial", 14), bg="red", command=Scissors)
scissors.place(x=250, y=150)
playerscore = tk.Label(screen, text="Player Score: 0", font=("Arial", 14), bg="grey",)
playerscore.place(x=50, y=250)
cpuscore = tk.Label(screen, text="CPU Score: 0", font=("Arial", 14), bg="grey")

cpuscore.place(x=50, y=280)
result_label = tk.Label(screen, text="", font=("Arial", 14), bg="grey")
result_label.place(x=50, y=350)
screen.mainloop()