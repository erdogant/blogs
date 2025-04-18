# Name of this file: setup_installer.py
from cx_Freeze import setup, Executable
import os
import shutil


#%% Function for cleaning
def remove_dirs(base_dir, dir_names):
    """
    Removes all directories matching the given names recursively from base_dir.

    :param base_dir: The root directory to search within.
    :param dir_names: A list of directory names to remove.
    """
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for folder in dirs:
            if any(name in folder for name in dir_names):
                folder_path = os.path.join(root, folder)
                print(f"Removing: {folder_path}")
                shutil.rmtree(folder_path)


# %% Setupfile for cx_Freeze
# Define the main script and the output
target = Executable(
    script="PhotoSenseDemo/main.py",  # Path to your main Streamlit app script.
    base="Console",                   # Use 'Console' for console applications or 'Win32GUI' for GUI apps without a terminal window.
    target_name="PhotoSenseDemo.exe", # Name your output executable.
)

# Include custom packages if needed.
include_files = []
# packages = ['ismember', 'pypickle']
# for package in packages:
#     package_dir = os.path.dirname(__import__(package).__file__) # Dynamically import and find the directory
#     include_files.append((package_dir, f'lib/{package}'))      # Add to include_files as (source, destination)

# Include additional directories
include_files += [
    ('.streamlit/', '.streamlit'), # Streamlit configuration directory
    ('PhotoSenseDemo/', './'),     # Include your entire project directory
]

# Define the build options (include streamlit and other dependencies)
build_options = {
    # "packages": ['streamlit_extras'],
    "include_files": include_files
    }

# Create the setup function to build the executable
setup(
    name="PhotoSenseDemo",
    version="1.0",  # Set the version
    description="PhotoSenseDemo",
    options={"build_exe": build_options},
    executables=[target],
)

# As a final step, copy
source_dir = r'C:\Users\beeld\.conda\envs\env_package_distribution\Lib\site-packages'
destination_dir = r'./build/exe.win-amd64-3.12/lib'
print(f"Copy {source_dir} to {destination_dir}..")
# Copy
shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
# Some cleaning. Remove all directories with dist-info.
remove_dirs(destination_dir, ["__pycache__", "dist-info", "tests"])