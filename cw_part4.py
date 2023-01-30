#date of submission:2023.1.30
#author: Yihang Fang 
from tkinter import *
#show the new window
def blanks(root):
	blank = Blank(root)  #blank
	subblank1 = Blank(blank, left_above=0)  # left blank above
	subblank2 = Blank(blank, left_below=0)
	subblank3 = Blank(blank, right=0)
	root.config(blank=blank)    #add the blank

	entry = Entry(root, font=('Arial', 12))
def button:
	button_cancelled = button(column=0, row=2)
	button_confirmed = button(k/l)

#help with calculation
def calculation:
	if click button_confirmed:
		clear(cancelled)
	if click button_cancelled:
		clear(subblank1, subblank2)

#delete one input letter
def back(input):
	input.delete(len(input)-1)

#delete all imput values
def cancelled:
	input.delete(0)
