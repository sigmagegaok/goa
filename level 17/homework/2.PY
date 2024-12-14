
def main():
    
    first_number = input("Enter the first number: ")

    numbers = [first_number]

    print("Enter additional numbers. Press Enter without typing to finish.")

    while True:
        number = input("Number: ")
        if number == "":  
            break
        numbers.append(number)

    print(f"You entered {len(numbers)} numbers.")

if __name__ == "__main__":
    main()
