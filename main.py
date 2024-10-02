import tkinter as tk
import repeater
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

import os

# define tkinter frame
frame = tk.Tk() 
frame.title("Repeater")


# used to store current selection for number of payloads
payload_count = 0


# variables used to keep track of checkbox values 
paired = False
tf_delay = False
randomize_delay = False


# update functions for checkbox variables
def update_paired():
	global paired
	paired = not paired
def update_tf_delay():
	global tf_delay
	tf_delay = not tf_delay
	print(tf_delay)
def update_randomize_delay():
	global randomize_delay
	randomize_delay = not randomize_delay
	print(randomize_delay)


def run_repeater():

	if tf_delay:
		try:
			delay = float(delay_entry.get())
		except:
			messagebox.showerror('Program Error', 'Error: please enter a valid delay!')
			return
	else:
		delay = 0

	d = (delay, randomize_delay)

	# Error checking to ensure correct number of payload files are present
	if payload_count == 1:
		if not os.path.isfile('payload1.txt'):
			messagebox.showerror('Program Error', 'Error: please create payload1.txt')
	elif payload_count == 2:
		if not (os.path.isfile('payload1.txt') and os.path.isfile('payload2.txt')):
			messagebox.showerror('Program Error', 'Error: please create payload1.txt and payload2.txt')
	elif payload_count == 3:
		if not (os.path.isfile('payload1.txt') and os.path.isfile('payload2.txt') and os.path.isfile('payload3.txt')):
			messagebox.showerror('Program Error', 'Error: please create payload1.txt, payload2.txt and payload3.txt')

	# swap this for a tkinter progress bar or something else?
	print("Running")
	request = request_input.get(1.0, "end-1c")
	
	repeater.run(request, payload_count, paired, d)

      
def add_symbols():

	global payload_count
    
	if payload_count < 3:
		try:
			index_start = request_input.index("sel.first")
			index_end = request_input.index("sel.last")
		
			# need to increment index end, to insert into next index slot
			ie_split = index_end.split('.')
			ie_plusone = ie_split[0] + '.' + str(int(ie_split[1])+1) # necessary to ensure this is handled across varying amounts of
																	 # decimal places based on content length

			request_input.insert(index_start, "§")
			request_input.insert(ie_plusone, "§")
		except:
			messagebox.showerror('Program Error', 'Error: no selection!')
	else:
		messagebox.showerror('Program Error', 'Error: no more than 3 payloads can be used!')


# Text box for request input
request_input = tk.Text(frame,
				height = 20, 
				width = 120)


# Labels for text boxes
l1 = tk.Label(frame, text = "Paste full html request:")


# button creation
add_button = tk.Button(frame, 
						text = "ADD §§", 
						command = add_symbols)

attack_button = tk.Button(frame, 
						text = "ATTACK", 
						command = run_repeater)



# checkbox creation
paired_checkbox = tk.Checkbutton(frame, text='Are variables paired?', variable=IntVar(), onvalue=True, offvalue=False, command=update_paired)
delay_checkbox = tk.Checkbutton(frame, text='Apply throttling between requests?', variable=IntVar(), onvalue=True, offvalue=False, command=update_tf_delay)
randomize_delay_checkbox = tk.Checkbutton(frame, text='Randomize delay requests?', variable=IntVar(), onvalue=True, offvalue=False, command=update_randomize_delay)


# text entry box creation
delay_entry = tk.Entry(frame, text='Enter wait time between requests')
delay_entry.insert(END, '0')


# insert elements into window
l1.grid(row=1, column=0, sticky=W, pady=2)
request_input.grid(row=1,column=1, sticky=W, pady=2)
add_button.grid(row=4, column=0, columnspan=2)
add_button.grid_rowconfigure(1, weight=1)
add_button.grid_columnconfigure(1, weight=1)
attack_button.grid(row=5, column=0, columnspan=2)
attack_button.grid_rowconfigure(1, weight=1)
attack_button.grid_columnconfigure(1, weight=1)
paired_checkbox.grid(row=6, column=0, columnspan=2)
delay_checkbox.grid(row=7, column=0, columnspan=1)
randomize_delay_checkbox.grid(row=7, column=1, columnspan=1)
delay_entry.grid(row=8, column=0, columnspan=2)




frame.mainloop()