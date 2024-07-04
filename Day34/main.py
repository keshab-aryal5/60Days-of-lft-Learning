# Day 34: File Handling and Error Management in Python

def read_file(file_path):
    """
    Reads the content of a file and returns it.
    If the file does not exist, it returns an error message.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_file(file_path, content):
    """
    Writes content to a file.
    If an error occurs during the writing process, it returns an error message.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"

def append_to_file(file_path, content):
    """
    Appends content to a file.
    If an error occurs during the appending process, it returns an error message.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            return "Content appended successfully."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
file_path = 'example.txt'

# Write to file
write_result = write_file(file_path, "This is the initial content of the file.\n")
print(write_result)

# Append to file
append_result = append_to_file(file_path, "This is the appended content.\n")
print(append_result)

# Read from file
read_result = read_file(file_path)
print(read_result)
