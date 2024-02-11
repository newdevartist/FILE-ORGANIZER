python
import os
import shutil

# Specify the directory path
directory = 'path_to_your_directory'

try:
    # List all files in the directory
    files = os.listdir(directory)

    # Implement your sorting algorithm here
    # For example, you can sort based on file extension
    for file in files:
        if file.endswith('.txt'):
            # Create a 'text' directory if it doesn't exist
            if not os.path.exists('text'):
                os.mkdir('text')
            # Move the file to the 'text' directory
            shutil.move(os.path.join(directory, file), 'text')
        # Add more conditions for other file types

except OSError as e:
    # Handle any OS-related errors
    print(f"Error: {e}")

except Exception as e:
    # Handle any other unexpected errors
    print(f"An error occurred: {e}")
    #We can further customize the sorting and organizing logic based on your specific requirements. This code provides a basic framework for file organization and error handling.