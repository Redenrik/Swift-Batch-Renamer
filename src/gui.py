import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from rename_files import rename_files, truncate_filenames
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from rename_files import rename_files, truncate_filenames

class RenamingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renaming Tool")
        self.create_widgets()

    def create_widgets(self):
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set("Rename")

        ttk.Label(self.root, text="Welcome to Redenrik's File Renaming Tool!").grid(column=0, row=0, padx=10, pady=10)

        ttk.Button(self.root, text="Rename Files", command=self.rename_files_gui).grid(column=0, row=1, padx=10, pady=10)
        ttk.Button(self.root, text="Truncate Filenames", command=self.truncate_filenames_gui).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).grid(column=0, row=3, padx=10, pady=10)

    def rename_files_gui(self):
        self.operation_var.set("Rename")
        self.folder_name = filedialog.askdirectory(title="Select the folder containing the files to rename")
        if not self.folder_name:
            return
        self.file_prefix = tk.simpledialog.askstring("Input", "Enter the file prefix (e.g., short_):", parent=self.root)
        self.start_number = tk.simpledialog.askinteger("Input", "Enter the starting number for the numbering system:", parent=self.root)
        self.perform_operation()

    def truncate_filenames_gui(self):
        self.operation_var.set("Truncate")
        self.folder_name = filedialog.askdirectory(title="Select the folder containing the files to truncate")
        if not self.folder_name:
            return
        self.max_length = tk.simpledialog.askinteger("Input", "Enter the maximum filename length for truncation:", initialvalue=15, parent=self.root)
        self.perform_operation()

    def perform_operation(self):
        operation = self.operation_var.get()
        if operation == "Rename":
            print(f"Renaming files in the folder '{self.folder_name}' with prefix '{self.file_prefix}' and starting number {self.start_number}...")
            try:
                rename_files(self.folder_name, self.file_prefix, self.start_number)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return
        else:
            print(f"Truncating filenames in the folder '{self.folder_name}' to a maximum length of {self.max_length} characters...")
            try:
                truncate_filenames(self.folder_name, self.max_length)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                return
        print("\nOperation completed successfully!")
        messagebox.showinfo("Success", "Operation completed successfully!")

def run_gui():
    print("Welcome to Redenrik's File Renaming Tool!")
    print("Please choose your operation...")

    operation = input("Choose operation [rename/truncate]: ")
    if operation.lower() not in ["rename", "truncate"]:
        print("Invalid operation. Exiting...")
        return

    folder_name = filedialog.askdirectory(title="Select the folder containing the files to rename")
    if not folder_name:
        print("No folder selected. Exiting...")
        return

    if operation == "rename":
        file_prefix = input("Enter the file prefix (e.g., short_): ")
        start_number = int(input("Enter the starting number for the numbering system: "))
        print(f"Renaming files in the folder '{folder_name}' with prefix '{file_prefix}' and starting number {start_number}...")
        try:
            renamed_folder = rename_files(folder_name, file_prefix, start_number)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        max_length = int(input("Enter the maximum filename length for truncation [default is 15]: ") or "15")
        print(f"Truncating filenames in the folder '{folder_name}' to a maximum length of {max_length} characters...")
        try:
            truncated_folder = truncate_filenames(folder_name, max_length)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    print("\nOperation completed successfully!")
    again = messagebox.askyesno("Continue", "Do you want to perform another operation?")
    if not again:
        print("Thank you for using Redenrik's File Renaming Tool. Goodbye!")


if __name__ == "__main__":
    run_gui()
    root = tk.Tk()
    app = RenamingTool(root)
    root.mainloop()