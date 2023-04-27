import tkinter as tk
from tkinter import filedialog
from rename_files import rename_files

def get_user_input():
    def submit():
        prefix = entry_prefix.get()
        start_number = int(entry_start_number.get())
        root.destroy()
        return prefix, start_number

    root = tk.Tk()
    root.title("File Renaming Tool")

    label_prefix = tk.Label(root, text="Enter the file prefix (e.g., short_):")
    label_prefix.pack()

    entry_prefix = tk.Entry(root)
    entry_prefix.pack()

    label_start_number = tk.Label(root, text="Enter the starting number for the numbering system:")
    label_start_number.pack()

    entry_start_number = tk.Entry(root)
    entry_start_number.pack()

    button = tk.Button(root, text="Submit", command=root.quit)
    button.pack()

    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()

    return entry_prefix.get(), int(entry_start_number.get())

def run_gui():
    print("Launching the File Renaming Tool...")

    root = tk.Tk()
    root.withdraw()

    folder_name = filedialog.askdirectory(title="Select the folder containing the files to rename")

    if not folder_name:
        print("No folder selected. Exiting...")
        return

    file_prefix, start_number = get_user_input()

    print(f"Renaming files in the folder '{folder_name}' with prefix '{file_prefix}' and starting number {start_number}...")

    renamed_folder = rename_files(folder_name, file_prefix, start_number)

    print("\nFiles renamed successfully in the folder '{}'!".format(renamed_folder))