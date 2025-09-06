userString = str(input("Please enter something questionable: "))
print("""
What action would you like performed?
    1. Convert to uppercase
    2. Convert to lowercase
    3. Take a specified substring
    4. Display the length
    5. Print each character on a newline 
""")
userChoice = int(input("Please enter your choice: "))
match userChoice:
    case 1:
        print(userString.upper())
    case 2:
        print(userString.lower())
    case 3:
        substringStart = input("Please enter a starting character, zero-indexed: ")
        substringEnd = input("Please enter a ending character, zero-indexed: ")
        if substringStart.isdigit() and substringEnd.isdigit():
            substringStart = int(substringStart)
            substringEnd = int(substringEnd)
            if (substringStart < substringEnd) and substringEnd <= len(userString):
                print(userString[substringStart:substringEnd])
        else:
            print("You entered some kind of invalid data. Tough luck, I'm not adding in custom messages for every case.")
    case 4:
        print(len(userString))
    case 5:
        for char in userString:
            print(char)
    case _:
        print("Please only enter a number from 1-5. There are no secret options.")
