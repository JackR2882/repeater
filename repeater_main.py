import tkinter as tk
import repeater

# Top level window 
frame = tk.Tk() 
frame.title("User input:") 
frame.geometry('1000x600') 
# Function for getting Input 
# from textbox and printing it 
# at label widget 

def run_repeater():
	print("Running")
	request = request_input.get(1.0, "end-1c") 
	#print(request)
	payload_location = payload_pos.get(1.0, "end-1c")
	#print(payload_location)
	repeater.run(request, payload_location)

# Text box for request input
request_input = tk.Text(frame,
				height = 20, 
				width = 120)

# Text box to identify payload position
payload_pos = tk.Text(frame,
					 height = 1,
					 width = 20)

# Labels for text boxes
l1 = tk.Label(frame, text = "Paste full html request:")
l2 = tk.Label(frame, text = "Identify payload: Must be exact match (regex).")

l1.pack()
request_input.pack()
l2.pack()
payload_pos.pack()

# Button Creation 
printButton = tk.Button(frame, 
						text = "ATTACK", 
						command = run_repeater) 
printButton.pack() 

frame.mainloop()