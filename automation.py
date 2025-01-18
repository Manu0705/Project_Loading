import os
import shutil

def organize_files(directory):
    # Create directories for images, documents, and other types
    image_dir = os.path.join(directory, 'Images')
    document_dir = os.path.join(directory, 'Documents')
    others_dir = os.path.join(directory, 'Others')

    # Create the directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(document_dir, exist_ok=True)
    os.makedirs(others_dir, exist_ok=True)

    # Supported file types for image and document
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    document_extensions = ['.pdf', '.docx', '.txt', '.xls', '.ppt']

    # Loop through files in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Move the file to the corresponding directory based on its extension
        if extension.lower() in image_extensions:
            shutil.move(file_path, os.path.join(image_dir, filename))
        elif extension.lower() in document_extensions:
            shutil.move(file_path, os.path.join(document_dir, filename))
        else:
            shutil.move(file_path, os.path.join(others_dir, filename))

    print("Files have been organized!")

# Main function
if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    if os.path.exists(directory):
        organize_files(directory)
    else:
        print(f"Error: The directory {directory} does not exist.")
