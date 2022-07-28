from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

#An exception to catch the FileNotFounderror if the program is ran for the first time
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#Function that is called to flip to the next card every 3 sec and randomly chooses a card from the french_word csv
def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = screen.after(3000, func=flip_card)

#Function the is called to flip the card over to reveal the translation of the word in English
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)

#Function that removes the current card that the user knows and store in a new csv file
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#Create the display screen
screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
screen.grid()
#Flip the card after 3 seconds
flip_timer = screen.after(3000, func=flip_card)

#Display the image that the text will be displayed on
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="/Users/chefy/PycharmProject/flashcardApp/images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
#Create the language text
card_title = canvas.create_text(400, 150, text="", fill= "black", font=("Ariel", 40, "italic"))
#Create the "word" text
card_word = canvas.create_text(400, 253, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Create the "X" Button
x_img = PhotoImage(file="/Users/chefy/PycharmProject/flashcardApp/images/wrong.png")
button_x = Button(image=x_img, highlightthickness=0, command=next_card)
button_x.grid(row=1, column=0)

#Cretea the Check Button
check_img = PhotoImage(file="/Users/chefy/PycharmProject/flashcardApp/images/right.png")
button_check = Button(image=check_img, highlightthickness=0, command=is_known)
button_check.grid(row=1, column=1)

#Call the next card function
next_card()




screen.mainloop()