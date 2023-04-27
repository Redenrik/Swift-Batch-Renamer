import os

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
