### sbpang: write a python to quickly search for a file with given keyword from a given folder and its sub-folder

import os,sys
import tkinter as tk
from tkinter import Listbox
import subprocess


def search_files(keyword, format, folder):
    output = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if format in file.split('.')[-1]:
                if keyword.lower() == '':
                    output.append(os.path.relpath(os.path.join(root, file), folder))
                elif keyword.lower() in file.lower() or keyword.lower() in root.lower():
                    output.append(os.path.relpath(os.path.join(root, file), folder))
            elif (keyword.lower() in file.lower() or keyword.lower() in root.lower()) and format == '':
                output.append(os.path.relpath(os.path.join(root, file), folder))
    return sorted(output)


def on_search():
    keyword = keyword_entry.get()
    format = format_entry.get()
    results = search_files(keyword, format, directory)
    
    # Calculate the maximum width needed
    max_width = max(len(result) for result in results) if results else 0
    result_listbox.config(width=max_width)
    
    result_listbox.delete(0, tk.END)
    for result in results:
        result_listbox.insert(tk.END, result)


def on_result_select(event):
    selected_path = result_listbox.get(result_listbox.curselection())
    absolute_path = os.path.join(directory, selected_path)
    subprocess.Popen(f'explorer /select,"{absolute_path}"')


if len(sys.argv) > 1:
    directory = sys.argv[1]

    # Create the main window
    root = tk.Tk()
    root.title("Search Files")

    # Label for keyword
    keyword_label = tk.Label(root, text="Keyword (blank if all file):")
    keyword_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    # Entry for keyword
    keyword_entry = tk.Entry(root)
    keyword_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    # Label for format
    format_label = tk.Label(root, text="Format (without '.'):")
    format_label.grid(row=0, column=2, padx=10, pady=10, sticky='e')

    # Entry for format
    format_entry = tk.Entry(root)
    format_entry.grid(row=0, column=3, padx=10, pady=10, sticky='w')

    # Search button
    search_button = tk.Button(root, text="Search", command=on_search)
    search_button.grid(row=0, column=4, padx=10, pady=10)

    # Bind the <Return> event to the on_search function
    keyword_entry.bind('<Return>', lambda event=None: on_search())

    # Bind the <Return> event to the on_search function
    format_entry.bind('<Return>', lambda event=None: on_search())

    # Listbox for search results with a scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=1, column=5, sticky='ns')

    result_listbox = Listbox(root, yscrollcommand=scrollbar.set, height=20)
    result_listbox.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
    result_listbox.bind('<Double-Button-1>', on_result_select)

    scrollbar.config(command=result_listbox.yview)

    root.mainloop()

"""
output = []
keyword = '20211025'
format = 'che'

for root, dirs, files in os.walk(r'\\vircon_Station\P0215_EPHLC'):
    for file in files:
        if format in file.split('.')[-1]:
            # check if keyword in filepath
            if keyword.lower() == '':
                print(os.path.relpath(os.path.join(root, file), r'\\vircon_Station\P0215_EPHLC'))
            elif keyword.lower() in file.lower() or keyword.lower() in root.lower():
                print(os.path.relpath(os.path.join(root, file), r'\\vircon_Station\P0215_EPHLC'))
            else:
                pass"""


                
