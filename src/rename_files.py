import os
import re
from tkinter import simpledialog, messagebox

def rename_files(folder_name, file_prefix, start_number):
    txt_counter = start_number
    png_counter = start_number

    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext == ".txt":
                new_filename = f"{file_prefix}{txt_counter}{file_ext}"
                txt_counter += 1
            elif file_ext == ".png":
                new_filename = f"{file_prefix}{png_counter}{file_ext}"
                png_counter += 1
            else:
                continue

            new_file_path = os.path.join(folder_name, new_filename)
            os.rename(file_path, new_file_path)

    return folder_name

def find_and_rename(dir, list_of_files_names, upper_bound=1000):
    list_of_files_names = [(prefix.split('.')[0], prefix.split('.')[1]) for prefix in list_of_files_names]
    list_of_files_in_dir = os.listdir(dir)

    for file_in_dir in list_of_files_in_dir:
        file_in_dir_full_path = os.path.join(dir, file_in_dir)
        if os.path.isfile(file_in_dir_full_path):
            for file_name in list_of_files_names:
                if re.match('{}_\w+\.{}'.format(file_name[0], file_name[1]), file_in_dir):
                    ideal_new_file_name = '.'.join(file_name)
                    if os.path.isfile(os.path.join(dir, ideal_new_file_name)):
                        for index in range(upper_bound):
                            next_best_name = file_name[0] + '_' + str(index) + '.' + file_name[1]
                            if not os.path.isfile(os.path.join(dir,next_best_name)):
                                os.rename(file_in_dir_full_path, os.path.join(dir, next_best_name))
                                break
                    else:
                        os.rename(file_in_dir_full_path, os.path.join(dir, ideal_new_file_name))


def truncate_filenames(master_dir, max_length):
    for path, subdirs, files in os.walk(master_dir):
        for file_name in files:
            new_name = file_name[:max_length] + '.' + file_name.split('.')[-1]

            # If the new name already exists in the directory, append a number to the end of the name
            if os.path.isfile(os.path.join(path, new_name)):
                for index in range(1, 1000):  # limit to 1000 to prevent infinite loops
                    indexed_name = new_name[:max_length] + '_' + str(index) + '.' + file_name.split('.')[-1]
                    if not os.path.isfile(os.path.join(path, indexed_name)):
                        new_name = indexed_name
                        break

            # Rename the file
            os.rename(os.path.join(path, file_name), os.path.join(path, new_name))

        # If there are any filename conflicts, ask the user how they want to proceed
        if len(set(os.listdir(path))) < len(os.listdir(path)):
            conflict_resolution = simpledialog.askstring("Filename Conflict", "Two or more files would end up with the same name. Would you like to:\n1. Add a number to the end of the conflicting filenames\n2. Move the conflicting files to a separate folder\nEnter the number of your choice:")
            if conflict_resolution == "1":
                # Add a number to the end of the conflicting filenames
                find_and_rename(path, os.listdir(path))
            elif conflict_resolution == "2":
                # Move the conflicting files to a separate folder
                if not os.path.exists(os.path.join(master_dir, "homonymous")):
                    os.mkdir(os.path.join(master_dir, "homonymous"))
                for file_name in os.listdir(path):
                    if os.listdir(path).count(file_name) > 1:
                        os.rename(os.path.join(path, file_name), os.path.join(master_dir, "homonymous", file_name))
            else:
                messagebox.showinfo("Invalid Option", "Please enter a valid option.")
                return