import tkinter as tk
import subprocess
import sys

def submit_text():
    text = entry.get()
    # print("You entered:", text)
    
    if text == "a":
        text = entry.get()
        print("You entered:", text)
        subprocess.run([sys.executable, "hello_world.py"])
        subprocess.run([sys.executable, "hello_world1.py"])
        
    root.destroy()

root = tk.Tk()
root.title("Text Input")

# Create input field
entry = tk.Entry(root)
entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_text)
submit_button.pack()

root.mainloop()

# comment to show changes 



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


