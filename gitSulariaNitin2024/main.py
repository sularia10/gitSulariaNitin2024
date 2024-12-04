import os

def rename_png_files(directory, prefix='new_'):
    # Get all files in the directory
    for filename in os.listdir(directory):
        # Check if the file ends with .png
        if filename.endswith('.png'):
            old_path = os.path.join(directory, filename)
            
            # Create a new name for the file
            new_filename = prefix + filename
            
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    # Define the folder where the PNG files are located
    folder_path = input("foto")
    
    # Optionally, change the prefix here
    rename_png_files(folder_path, prefix='new_')  # You can customize the prefix
