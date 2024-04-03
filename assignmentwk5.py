# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 987\n")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied to create file.")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied to read file.")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 1\n")
        file.write("67890\n")
        file.write("Another line appended: 543\n")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied to append to file.")
finally:
    print("File appending completed.")
