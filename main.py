import tkinter as tk
import repeater
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

import os

# define tkinter frame
frame = tk.Tk() 
frame.title("Repeater") 
#frame.geometry('1000x600') 


# used to store current selection for number of payloads
payload_count = 0
p_count = IntVar()


def run_repeater():

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
	
	#payload_loc = []
    
	#payload_loc.append(payload_pos1.get(1.0, "end-1c"))	
	#if p_count.get() > 1: payload_loc.append(payload_pos2.get(1.0, "end-1c"))

	#payload_location = payload_pos1.get(1.0, "end-1c")
	
	repeater.run(request, payload_count) # needs to be changed to take payload_loc instead, also need
									   # to add conditionals to handle multiple payloads in repeater.py

#def func1():
    
    # clear any existing items from grid
#    l2.grid_remove()
#    payload_pos1.grid_remove()
#    l2_2.grid_remove()
#    payload_pos2.grid_remove()

	# add required items to grid
#    if p_count.get() == 1:
#        l2.grid(row=2, column=0, sticky=W, pady=2)
#        payload_pos1.grid(row=2, column=1, sticky=W, pady=2)
#    elif p_count.get() == 2:
#         l2.grid(row=2, column=0, sticky=W, pady=2)
#         payload_pos1.grid(row=2, column=1, sticky=W, pady=2)
#         l2_2.grid(row=3, column=0, sticky=W, pady=2)
#         payload_pos2.grid(row=3, column=1, sticky=W, pady=2)
      
def add_symbols():

	global payload_count
    
	if payload_count < 3:
		try:
			index_start = request_input.index("sel.first")
			index_end = request_input.index("sel.last")
			request_input.insert(index_start, "§")
			request_input.insert(str(float(index_end)+0.01), "§")
			payload_count += 1
		except:
			messagebox.showerror('Program Error', 'Error: no selection!')
			print("ERROR: no selection!")
	else:
		messagebox.showerror('Program Error', 'Error: no more than 3 payloads can be used!')


# Text box for request input
request_input = tk.Text(frame,
				height = 20, 
				width = 120)


# Text boxes to identify payload position
payload_pos1 = tk.Text(frame,
					height = 1,
					width = 20)
payload_pos2 = tk.Text(frame,
                    height = 1,
                	width = 20)

# Labels for text boxes
l1 = tk.Label(frame, text = "Paste full html request:")
#l2 = tk.Label(frame, text = "Identify payload: Must be exact match (regex).")
#l2_2 = tk.Label(frame, text = "Identify payload 2: Must be exact match (regex).")


# define radio buttons to select number of payloads
#r1 = Radiobutton(frame, text="Single payload.", variable=p_count, value=1, command=func1)
#Radio_1.pack(side = TOP, ipady = 5) 
#Radio_1.invoke() # selects by default
#r2 = Radiobutton(frame, text="Dual payload.", variable=p_count, value=2, command=func1)
#Radio_2.pack(side = TOP, ipady = 5) 


#l1.pack(side="top")
#request_input.pack(side="top")

#r1.pack(side="left")
#r1.invoke()
#r2.pack(side="left")

#l2.pack(side="bottom")
#payload_pos1.pack(side="bottom")

# button creation
add_button = tk.Button(frame, 
						text = "ADD §§", 
						command = add_symbols)

attack_button = tk.Button(frame, 
						text = "ATTACK", 
						command = run_repeater)
#attackButton.pack(side="bottom") 


# insert elements into window

#r1.grid(row=0, column=0, sticky=W, pady=2)
#r2.grid(row=0, column=1, sticky=W, pady=2)
l1.grid(row=1, column=0, sticky=W, pady=2)
request_input.grid(row=1,column=1, sticky=W, pady=2)
add_button.grid(row=4, column=0, columnspan=2)
add_button.grid_rowconfigure(1, weight=1)
add_button.grid_columnconfigure(1, weight=1)
attack_button.grid(row=5, column=0, columnspan=2)
attack_button.grid_rowconfigure(1, weight=1)
attack_button.grid_columnconfigure(1, weight=1)

# select r1 as default
#r1.invoke()



frame.mainloop()