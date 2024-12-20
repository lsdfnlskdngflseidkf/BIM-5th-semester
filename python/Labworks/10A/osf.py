import os

try:
    # Get the current working directory
    cwd = os.getcwd()
    print(f"Current directory: {cwd}")

    # Define paths for the new and renamed directories
    newd = "/home/nullproj/Documents/BIM-5th-semester/python/test"
    red = "/home/nullproj/Documents/BIM-5th-semester/python/test_renamed"

    # Create the new directory if it doesn't exist
    if not os.path.exists(newd):
        os.mkdir(newd)
        print(f"Directory '{newd}' created")
    else:
        print(f"Directory '{newd}' already exists")

    # Change to the new directory
    os.chdir(newd)
    print(f"Changed to new directory: {os.getcwd()}")

    # List files in the new directory
    print(f"Files in the new folder: {os.listdir()}")

    # Rename the directory
    os.chdir(cwd)  # Ensure you're not inside the directory being renamed
    os.rename(newd, red)
    print(f"Directory renamed to: '{red}'")

    # Remove the renamed directory
    if not os.listdir(red):  # Check if the directory is empty
        os.rmdir(red)
        print(f"Successfully deleted directory '{red}'")
    else:
        print(f"Directory '{red}' is not empty. Cannot delete.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Change back to the original directory
    os.chdir(cwd)
    print(f"Changed back to original directory: {cwd}")
    print(f"Files in original folder: {os.listdir()}")
