import tkinter as tk
import repeater
from tkinter import *
from tkinter.ttk import *

# define tkinter frame
frame = tk.Tk() 
frame.title("User input:") 


def something():
    try:
        index_start = request_input.index("sel.first")
        index_end = request_input.index("sel.last")
        request_input.insert(index_start, "§")
        request_input.insert(str(float(index_end)+0.01), "§")
    except:
        print("ERROR: no selection!")

def attack():
    print('Attacking!')
    #replaced_json = re.sub(r''+str(p_l), payload, str(replaced_json))

    input = request_input.get(1.0, "end-1c")

    indexes = []
    i = 0
    # read through string and generate array of index pairs for every set of '§' symbols
    for x in input:
        if x == "§":
            indexes.append(i)
        i += 1

    from numpy import array

    #arr = array(zip(array(indexes[0::2]), array(indexes[1::2])))
    #print(arr)
    #print(arr.shape())

    replaced = "!@!@!@"

    first_array = array(indexes[0::2])
    second_array = array(indexes[1::2])

    offset = 0

    for x in range(0, len(first_array)):
        # doesn't take into account that symbols are now offset as replacement text has been inserted
        # does now, but not a particularly clean solution - might need to think about a replacement one

        input = input[:first_array[x]+offset] + replaced + input[second_array[x]+offset+1:]
        print(input)

        offset = offset + (len(replaced) - (second_array[x] - first_array[x])) - 1
        #print(offset)



default_text = "some §text§ here for testing purposes §only§"


# Text box for request input
request_input = tk.Text(frame,
				height = 20, 
				width = 120)
request_input.insert(END, default_text)

add_button = tk.Button(frame, 
						text = "ADD §§", 
						command = something) 

attack_button = tk.Button(frame, 
						text = "ATTACK", 
						command = attack)

request_input.pack()
add_button.pack()
attack_button.pack()

mainloop()

