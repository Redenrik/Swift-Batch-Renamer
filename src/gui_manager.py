import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from rename_files import rename_files, truncate_filenames, simpledialog

class GUIManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Renaming Tool")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        welcome_message = "Welcome to the File Renaming Tool by Redenrik."
        welcome_label = tk.Label(self.root, text=welcome_message)
        welcome_label.pack()

        rename_button = tk.Button(self.root, text="Batch Rename Files", command=self.batch_rename)
        rename_button.pack()

        truncate_button = tk.Button(self.root, text="Batch Truncate Filenames", command=self.batch_truncate)
        truncate_button.pack()

        self.close_button = tk.Button(self.root, text="Exit", command=self.close)
        self.close_button.pack()

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.quit()

    def batch_rename(self):
        self._batch_operation("Rename")

    def batch_truncate(self):
        self._batch_operation("Truncate")

    def _batch_operation(self, operation):
        self.folder_name = filedialog.askdirectory(title=f"Select the folder for {operation}")
        if not self.folder_name:
            messagebox.showinfo("No folder selected", "Please select a folder to continue.")
            return

        if operation == "Rename":
            self._rename_files()
        else:
            self._truncate_files()

    def _rename_files(self):
        prefix = simpledialog.askstring("Input", "Enter the file prefix (e.g., short_):")
        start_number = simpledialog.askinteger("Input", "Enter the starting number for the numbering system:")
        rename_files(self.folder_name, prefix, start_number)

    def _truncate_files(self):
        max_length = simpledialog.askinteger("Input", "Enter the maximum filename length for truncation:", initialvalue=15)
        truncate_filenames(self.folder_name, max_length)
