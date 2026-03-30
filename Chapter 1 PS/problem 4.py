import os

# Sample dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Use os module to clear the screen (optional)
# Works on Windows and Linux/macOS
os.system('cls' if os.name == 'nt' else 'clear')

# Print current working directory using os module
print("Current Working Directory:", os.getcwd())
print()

# Print the contents of the dictionary
print("Contents of the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\n--- os Module Contents ---")
# Print the list of all attributes and methods in os module
print(dir(os))
