import string
UPPER_ALPHABET, ALPHABET = [*string.ascii_uppercase], [*string.ascii_lowercase]

def Sort(shift) -> None:
    #Sorting algorithm, take the last characters in the ALPHABET/UPPER_ALPHABET and put it at the start of the shifted/shifted_upper for a ceratian almount of times, decided by shift
    #The rest of the ALPHABET/UPPER_ALPHABET get put into shifted/shifted_upper without any change
    for k in range(shift, len(ALPHABET) + shift):
        if k < len(ALPHABET):
            shifted.append(ALPHABET[k])
            shifted_upper.append(UPPER_ALPHABET[k])
        else:
            shifted.append(ALPHABET[abs(k - len(ALPHABET))])
            shifted_upper.append(UPPER_ALPHABET[abs(k - len(ALPHABET))])

def Encipher(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input) -> str:
    output = ""
    #This find the position of k in ALPHABET/UPPER_ALPHABET then add the element with the same position as k in shifted/shifted_upper to output
    for k in user_input:
        if k in ALPHABET:
            output += shifted[ALPHABET.index(k)]
        elif k in UPPER_ALPHABET:
            output += shifted_upper[UPPER_ALPHABET.index(k)]
        else:
            output += k
    return output
 
def Decipher(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input) -> str:
    output = ""
    #This does the exact opposite as Encipher
    for k in user_input:
        if k in shifted:
            output += ALPHABET[shifted.index(k)]
        elif k in shifted_upper:
            output += UPPER_ALPHABET[shifted_upper.index(k)]
        else:
            output += k
    return output

def check(shift) -> bool:
    try:
        int(shift)
        return True
    except ValueError:
        return False

while True:
    run = True
    cmd = input("Type E for Enciphering, type D for Deciphering (case insensitive). Type / to end the program: ")
    if cmd == "e" or cmd == "E":
        while run:
            #Check if the user has input "/" to cancel Enciphering or not
            user_input = [*input("Your input: ").strip()]
            if user_input:
                while run:
                    shifted, shifted_upper = [], []
                    shift = input("Shift (type / to cancel): ")
                    if check(shift):
                        Sort(int(shift) % 26)
                        print(f"Output: {Encipher(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input)}")
                    elif shift == "/":
                        run = False
                    else:
                        print("Input has to be an integer.")
            else:
                print("Input cannot be empty.")
                
    #This elif block essentially do the same thing as the if block above
    elif cmd == "d" or cmd ==" D":
        while run:
            user_input = [*input("Your input: ").strip()]
            if user_input:
                while run:
                    shifted, shifted_upper = [], []
                    shift = input("Shift (type / to cancel): ")
                    if check(shift):
                        Sort(int(shift) % 26)
                        print(f"Output: {Decipher(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input)}")
                    elif shift == "/":
                        run = False
                    else:
                        print("Input has to be an integer.")
            else:
                print("Input cannot be empty.")

    elif cmd == "/":
        exit()
    else:
        print("Invalid command.")
