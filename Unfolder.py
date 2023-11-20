import os
import shutil

def flatten_folders(source_folder):
    # Get a list of all files in the source folder and its subfolders
    all_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Move all files to the parent folder
    for file_path in all_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(source_folder, file_name)

        # Handle name conflicts by adding a number to the file name
        counter = 1
        while os.path.exists(destination_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = f"{base_name}_{counter}{extension}"
            destination_path = os.path.join(source_folder, new_name)
            counter += 1

        shutil.move(file_path, destination_path)
        print(f"Moved '{file_name}' to '{source_folder}'.")

    # Delete empty subfolders
    for root, dirs, _ in os.walk(source_folder, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):  # Check if the folder is empty
                os.rmdir(folder_path)
                print(f"Deleted empty folder '{folder_path}'.")

if __name__ == "__main__":
    # Specify the path to the parent folder
    parent_folder = "C:\\Users\\chaud\\Desktop\\Random"

    # Call the flatten_folders function
    flatten_folders(parent_folder)
