from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn')
except FileNotFoundError:
    original_data = pandas.read_csv('data/5000_wordlist_french.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['word_fr'], fill='black')
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, flip_card)


window = Tk()
window.title('Flash Card Fr/En')

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['word_en'], fill='white')
    canvas.itemconfig(card_background, image=back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=front_img)

back_img = PhotoImage(file='images/card_back.png')

card_title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='images/right.png')
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)

next_card()

window.mainloop()

