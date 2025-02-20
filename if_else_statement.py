# Bryant Ray Manalad
# ITELEC2
# Laboratory #09 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():

    try:
        user_input = input("Enter a number: ")
        number = int(user_input)            
        if number % 2 == 0:
            print("The number", number, "is Even.")
        else:
            print("The number", number, "is Odd.") 
            #code here
    except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()