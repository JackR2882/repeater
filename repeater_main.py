import tkinter as tk
import repeater
from tkinter import *
from tkinter.ttk import *

# define tkinter frame
frame = tk.Tk() 
frame.title("User input:") 
#frame.geometry('1000x600') 


# used to store current selection for number of payloads
p_count = IntVar()


def run_repeater():
	print("Running")
	request = request_input.get(1.0, "end-1c") 
	#print(request)
	payload_location = payload_pos1.get(1.0, "end-1c")
	#print(payload_location)
	repeater.run(request, payload_location)

def func1():
    
    # clear any existing items from grid
    l2.grid_remove()
    payload_pos1.grid_remove()
    l2_2.grid_remove()
    payload_pos2.grid_remove()

	# add required items to grid
    if p_count.get() == 1:
        l2.grid(row=2, column=0, sticky=W, pady=2)
        payload_pos1.grid(row=2, column=1, sticky=W, pady=2)
    elif p_count.get() == 2:
         l2.grid(row=2, column=0, sticky=W, pady=2)
         payload_pos1.grid(row=2, column=1, sticky=W, pady=2)
         l2_2.grid(row=3, column=0, sticky=W, pady=2)
         payload_pos2.grid(row=3, column=1, sticky=W, pady=2)



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
l2 = tk.Label(frame, text = "Identify payload: Must be exact match (regex).")
l2_2 = tk.Label(frame, text = "Identify payload 2: Must be exact match (regex).")


# define radio buttons to select number of payloads
r1 = Radiobutton(frame, text="Single payload.", variable=p_count, value=1, command=func1)
#Radio_1.pack(side = TOP, ipady = 5) 
#Radio_1.invoke() # selects by default
r2 = Radiobutton(frame, text="Dual payload.", variable=p_count, value=2, command=func1)
#Radio_2.pack(side = TOP, ipady = 5) 


#l1.pack(side="top")
#request_input.pack(side="top")

#r1.pack(side="left")
#r1.invoke()
#r2.pack(side="left")

#l2.pack(side="bottom")
#payload_pos1.pack(side="bottom")


# Button Creation 
attack_button = tk.Button(frame, 
						text = "ATTACK", 
						command = run_repeater) 
#attackButton.pack(side="bottom") 


# insert elements into window

r1.grid(row=0, column=0, sticky=W, pady=2)
r2.grid(row=0, column=1, sticky=W, pady=2)
l1.grid(row=1, column=0, sticky=W, pady=2)
request_input.grid(row=1,column=1, sticky=W, pady=2)
attack_button.grid(row=5, column=0, columnspan=2)
attack_button.grid_rowconfigure(1, weight=1)
attack_button.grid_columnconfigure(1, weight=1)

# select r1 as default
r1.invoke()



frame.mainloop()