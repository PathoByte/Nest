# File read and write 
with open("/home/crystal/Memoire_Vault/Glass/WK-4-ASSIGNMENT/example.txt", "r") as file:
    content = file.read()

modified = content.upper()

with open("/home/crystal/Memoire_Vault/Glass/WK-4-ASSIGNMENT/new_example.txt", "w") as file:
    file.write(modified)

print("File has been modified and saved as 'new_example.txt'")


# Error handling

# Ask the user for the filename
filename = input("Enter the filename: ")

try:
    # Try to open the file in read mode
    with open("/home/crystal/Memoire_Vault/Glass/WK-4-ASSIGNMENT/example.txt", "r") as file:
        print("File opened successfully!")
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

