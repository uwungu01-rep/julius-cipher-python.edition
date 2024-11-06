import string
UPPER_ALPHABET, ALPHABET = [*string.ascii_uppercase], [*string.ascii_lowercase]

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
    
def main(param) -> None:
    run = True
    while run:
        user_input = [*input("Your input: ").strip()]
        if user_input:
            while run:
                shift = input("Shift (type / to cancel): ")
                if check(shift):
                    shifted =  ALPHABET[int(shift) % 26:] + ALPHABET[:int(shift) % 26]
                    shifted_upper = UPPER_ALPHABET[int(shift) % 26:] + UPPER_ALPHABET[:int(shift) % 26]
                    eval(f'print("Output:", {param}(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input))')
                elif shift == "/":
                    run = False
                else:
                    print("Input has to be an integer.")
        else:
            print("Input cannot be empty.")

while True:
    cmd = input("Type E for Enciphering, type D for Deciphering (case insensitive). Type / to end the program: ")
    if cmd == "e" or cmd == "E":
        main("Encipher")
    elif cmd == "d" or cmd ==" D":
        main("Decipher")
    elif cmd == "/":
        exit()
    else:
        print("Invalid command.")
