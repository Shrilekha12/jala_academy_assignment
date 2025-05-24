# read_file.py

# Replace 'example.txt' with your file name
file_path = 'example.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")