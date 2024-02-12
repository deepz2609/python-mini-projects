import random as r

# Function to create a banner with given text
def create_banner(text):
    print("-" * (len(text) + 4))
    print(f"| {text} |")
    print("-" * (len(text) + 4))

# Create a banner for the dice simulator
create_banner("Welcome to the dice simulator")

# Function to generate and print a random dice face
def generate():
    number = r.randint(1, 6)
    if number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")

    elif number == 2:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")

    elif number == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")

    elif number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")

    elif number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")

    elif number == 6:    
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")

# Main function to handle user input and roll the dice
def main():
    while True:
        choice = input("\n[+] Press 'y' to roll the dice or 'n' to exit : ")
        if choice == 'y':
            generate()
        else:
            print("Exiting...")
            break

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
