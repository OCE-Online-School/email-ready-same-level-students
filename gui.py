import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import main
import os

filepath_1 = ""
filepath_2 = ""

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
#root.resizable(False, False)
root.geometry('350x500')
root.configure(bg='#57caff')
root.title('Final CSV for same level students - Made by Sean')
root.resizable(True, True)

def run_application():

    if(filepath_1 == ""):
        error = "Please choose a contract file."
        tk.messagebox.showerror(title="Error", message=error)
        return
    
    if(filepath_2 == ""):
        error = "Please choose the same level students file with teacher comments."
        tk.messagebox.showerror(title="Error", message=error)
        return

    print("Send the following:")
    print("Contract filepath: ", filepath_1)
    print("Same level students filepath: ", filepath_2)

    main.create_same_level_list(filepath_1, filepath_2)

def select_file_1():

    global filepath_1

    filetypes = (
        ('csv files', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    label_1['text'] = filename 
    filepath_1 = filename
    print(filename)

def select_file_2():

    global filepath_2

    filetypes = (
        ('csv files', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    label_2['text'] = filename 
    filepath_2 = filename

title = tk.Label(root, height=2, text="final CSV for email")
title.pack()
title.configure(font=("Times New Roman", 20))
title.configure(bg='#57caff')

sub_title_1 = tk.Label(root, text="      1. Choose the contract file")
sub_title_1.pack(pady=2, anchor="w")
sub_title_1.configure(bg='#57caff')

# open button - contract file
open_button_1 = ttk.Button(
    root,
    text='Select contract csv',
    command=select_file_1
)

open_button_1.pack(pady=5)

label_1 = tk.Label(root, text="No file selected")
label_1.pack(pady=5)
label_1.configure(bg='#57caff')

sub_title_3 = tk.Label(root, text="      2. Make sure same level students file \n has same headers as\n per the guide.")
sub_title_3.pack(pady=15, anchor="w")
sub_title_3.configure(bg='#57caff')

sub_title_2 = tk.Label(root, text="      3. Choose the same level students file")
sub_title_2.pack(pady=2, anchor="w")
sub_title_2.configure(bg='#57caff')

# open button - attendance file
open_button_2 = ttk.Button(
    root,
    text='Select SMS csv',
    command=select_file_2,
)

open_button_2.pack(pady=5)

label_2 = tk.Label(root, text="No file selected")
label_2.pack(pady=10)
label_2.configure(bg='#57caff')

sub_title_4 = tk.Label(root, text="      4. Once 1, 2 & 3 complete, click Run")
sub_title_4.pack(pady=15, anchor="w")
sub_title_4.configure(bg='#57caff')

# open button - attendance file
run_button = ttk.Button(
    root,
    text='Run',
    command=run_application,
)

run_button.pack(pady=5)

# run the application
root.mainloop()
