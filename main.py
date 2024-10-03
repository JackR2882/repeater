import tkinter as tk
import repeater
from tkinter import messagebox
from tkinter import *

import os

# define tkinter frame
frame = tk.Tk() 
frame.title("Repeater")


# entry variables used to keep track of checkbox values
paired_e = tk.IntVar()
tf_delay_e = tk.IntVar()
randomize_delay_e = tk.IntVar()


def run_repeater():

	# redefine checkbox values into boolean varaibles
	paired = bool(paired_e.get())
	tf_delay = bool(tf_delay_e.get())
	randomize_delay = bool(randomize_delay_e.get())

	if tf_delay:
		try:
			delay = float(delay_entry.get())
		except:
			messagebox.showerror('Program Error', 'Error: please enter a valid delay!')
			return
	else:
		delay = 0

	d = (delay, randomize_delay)

	# maybe put a progress bar or something here?
	request = request_input.get(1.0, "end-1c")
	repeater.run(request, paired, d)

      
def add_symbols():

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
	

# Text box for request input
request_input = tk.Text(frame,
				height = 20, 
				width = 120)


# Labels for text boxes
l1 = tk.Label(frame, text="Paste full html request:")
l2 = tk.Label(frame, text="Delay between requests (ms):")


# button creation
add_button = tk.Button(frame, 
						text = "ADD §§", 
						command = add_symbols)

attack_button = tk.Button(frame, 
						text = "ATTACK", 
						command = run_repeater)


# checkbox creation
paired_checkbox = tk.Checkbutton(frame, text='Are variables paired?', variable=paired_e, onvalue=True, offvalue=False)
delay_checkbox = tk.Checkbutton(frame, text='Apply throttling between requests?', variable=tf_delay_e, onvalue=True, offvalue=False)
randomize_delay_checkbox = tk.Checkbutton(frame, text='Randomize delay requests?', variable=randomize_delay_e, onvalue=True, offvalue=False)


# text entry box creation
delay_entry = tk.Entry(frame, text='Enter wait time between requests')
delay_entry.insert('end', '0')


# insert elements into window
l1.grid(row=1, column=0, sticky='W', pady=2)
request_input.grid(row=1,column=1, sticky='W', pady=2)
add_button.grid(row=4, column=0, columnspan=2)
attack_button.grid(row=5, column=0, columnspan=2)
paired_checkbox.grid(row=6, column=0, columnspan=2, sticky='W')
delay_checkbox.grid(row=7, column=0, columnspan=1, sticky='W')
randomize_delay_checkbox.grid(row=7, column=1, columnspan=1, sticky='W')
l2.grid(row=8, column=0, columnspan=1, sticky='W')
delay_entry.grid(row=8, column=1, columnspan=1, sticky='W')


frame.mainloop()