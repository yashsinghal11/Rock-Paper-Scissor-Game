from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Initialize window
window = Tk()
window.title("ROCK PAPER AND SCISSORS GAME")
window.configure(background="black")

# Load images
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor 1 (1).png"))

image_rock2 = ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png"))

# Labels to display images
label_player = Label(window, image=image_scissor1, bg="black")
label_computer = Label(window, image=image_scissor2, bg="black")
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Indicators (title above scores)
player_indicator = Label(window, font=("arial", 40, "bold"), text="PLAYER", bg="grey", fg="black")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="grey", fg="black")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

# Final message display
final_message = Label(window, font=("arial", 20, "bold"), bg="lightgrey", fg="black")
final_message.grid(row=3, column=2)

# Score labels
score_computer = Label(window, text=0, font=('arial', 60, "bold"), bg="lightgrey", fg="black")
score_player = Label(window, text=0, font=('arial', 60, "bold"), bg="lightgrey", fg="black")

score_computer.grid(row=1, column=1)
score_player.grid(row=1, column=3)

# Function to update final message
def updateMessage(msg):
    final_message['text'] = msg

# Update computer score
def computer_update():
    final = int(score_computer['text'])
    final += 1
    score_computer["text"] = str(final)

# Update player score
def player_update():
    final = int(score_player['text'])
    final += 1
    score_player["text"] = str(final)

# Winner logic
def winner_check(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("Computer wins!")
            computer_update()
        else:
            updateMessage("Player wins!")
            player_update()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Computer wins!")
            computer_update()
        else:
            updateMessage("Player wins!")
            player_update()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Computer wins!")
            computer_update()
        else:
            updateMessage("Player wins!")
            player_update()

# Choices
to_select = ["rock", "paper", "scissor"]

def choice_update(player_choice):
    computer_choice = to_select[randint(0, 2)]

    # Update computer image
    if computer_choice == "rock":
        label_computer.configure(image=image_rock2)
    elif computer_choice == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    # Update player image
    if player_choice == "rock":
        label_player.configure(image=image_rock1)
    elif player_choice == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(player_choice, computer_choice)

# Buttons
button_rock = Button(window, width=16, height=3, text="ROCK",
                     font=("Arial", 14), bg="lightgray", command=lambda: choice_update("rock"))
button_rock.grid(row=2, column=1)

button_paper = Button(window, width=16, height=3, text="PAPER",
                      font=("Arial", 14), bg="lightgray", command=lambda: choice_update("paper"))
button_paper.grid(row=2, column=2)

button_scissor = Button(window, width=16, height=3, text="SCISSOR",
                        font=("Arial", 14), bg="lightgray", command=lambda: choice_update("scissor"))
button_scissor.grid(row=2, column=3)

# Run the window
window.mainloop()
