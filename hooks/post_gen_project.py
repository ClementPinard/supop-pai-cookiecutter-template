import os
import shutil
import sys

# Get the path where Cookiecutter just dropped the temporary folder
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)

try:
    # Move all files and subdirectories up to the current working directory
    for item in os.listdir(current_dir):
        source_path = os.path.join(current_dir, item)
        destination_path = os.path.join(parent_dir, item)
        
        if os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        else:
            shutil.copy2(source_path, destination_path)

    # Clean up the temporary directory created by Cookiecutter
    # We must schedule its removal because Python is executing inside it right now
    os.chdir(parent_dir)
    shutil.rmtree(current_dir)

except Exception as e:
    print(f"Error flattening directory structure: {e}")
    sys.exit(1)
