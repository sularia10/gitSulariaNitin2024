import os
import random
import string

def generate_random_name():
    """Generate a random string of 4 alphabets"""
    return ''.join(random.choices(string.ascii_lowercase, k=4))

def rename_png_files(directory):
    """Rename all .png files in the given directory to 4 random alphabets"""
    for filename in os.listdir(directory):
        # Check if the file ends with .png
        if filename.endswith('.png'):
            old_path = os.path.join(directory, filename)
            
            # Generate a new random name
            new_name = generate_random_name() + '.png'
            new_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_name}')

if __name__ == "__main__":
    # Get the current directory (same folder as the script)
    current_directory = os.getcwd()
    
    # Rename all .png files in the current directory
    rename_png_files(current_directory)
