import tkinter as tk
import repeater
from tkinter import messagebox

import os

# define tkinter frame
frame = tk.Tk() 
frame.title("Repeater")


# used to store current selection for number of payloads
payload_count = 0


# variables used to keep track of checkbox values
paired = tk.IntVar()
tf_delay = tk.IntVar()
randomize_delay = tk.IntVar()


def run_repeater():

	# redefine checkbox values into boolean varaibles
	paired = bool(paired.get())
	tf_delay = bool(tf_delay.get())
	randomize_delay = bool(randomize_delay.get())


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
paired_checkbox = tk.Checkbutton(frame, text='Are variables paired?', variable=paired, onvalue=True, offvalue=False)
delay_checkbox = tk.Checkbutton(frame, text='Apply throttling between requests?', variable=tf_delay, onvalue=True, offvalue=False)
randomize_delay_checkbox = tk.Checkbutton(frame, text='Randomize delay requests?', variable=randomize_delay, onvalue=True, offvalue=False)


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