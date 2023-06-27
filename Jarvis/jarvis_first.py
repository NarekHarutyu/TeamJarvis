# import tkinter as tk
# import subprocess
# import sys

# def submit_text():
#     text = entry.get()
#     # print("You entered:", text)
    
#     if text == "a":
#         text = entry.get()
#         print("You entered:", text)
#         subprocess.run([sys.executable, "hello_world.py"])
#         subprocess.run([sys.executable, "hello_world1.py"])
        
#     root.destroy()

# root = tk.Tk()
# root.title("Text Input")

# # Create input field
# entry = tk.Entry(root)
# entry.pack()

# # Create submit button
# submit_button = tk.Button(root, text="Submit", command=submit_text)
# submit_button.pack()

# root.mainloop()

# comment to show changes 

from tkinter import * 
import tkinter as tk
import subprocess
import sys
import os
import signal

def submit_text():
    text = entry.get()
    # print("You entered:", text)
   
    if text == "a":
        text = entry.get()
        print("You entered:", text)
       
        proc1 = subprocess.Popen([sys.executable, "hello_world.py"])
        proc2 = subprocess.Popen([sys.executable, "hello_world1.py"])
       
        pid1 = proc1.pid
        pid2 = proc2.pid
       
        # You can kill the processes later if needed like this:
        # os.kill(pid1, signal.SIGTERM)
        # os.kill(pid2, signal.SIGTERM)
       
    root.destroy()

root = tk.Tk()
root.title("Text Input")

# Create input field
input_text = StringVar()
entry = tk.Entry(root, textvariable = input_text, justify = CENTER)
entry.pack(side = TOP, ipadx = 30, ipady = 6)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_text)
submit_button.pack(side = TOP, ipadx = 5, ipady = 5)

root.mainloop()