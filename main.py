import string
ALPHABET, ALPHABET_UPPER = [*string.ascii_lowercase], [*string.ascii_uppercase]
COMMAND = ["e", "E", "d", "D"]

def Caesar(ALPHABET, shifted, UPPER_ALPHABET, shifted_upper, user_input) -> str:
    output = ""
    for k in user_input:
        if k in ALPHABET:
            output += shifted[ALPHABET.index(k)]
        elif k in UPPER_ALPHABET:
            output += shifted_upper[UPPER_ALPHABET.index(k)]
        else:
            output += k
    return output

def IsInt(inp):
    try:
        int(inp)
        return True
    except ValueError:
        return False

while True:
    cmd = input("Type E for Enciphering, type D for Deciphering (case insensitive). Type / to end the program: ")
    if cmd == "/":
        exit(0)
    elif cmd not in COMMAND:
        print("Invalid command.")
        continue

    while True:
        user_input = [*input("Your input: ").strip()]
        if not user_input:
            print("Input cannot be empty.")
        else:
            break
    
    while True:
        shift = input("Shift (type / to cancel): ")
        if IsInt(shift) and (cmd == "e" or cmd == "E"):
            shift = int(shift)
            shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
            shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
            print(f"Output: {Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, user_input)}")
        elif IsInt(shift) and (cmd == "d" or cmd == "D"):
            shift = -int(shift)
            shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
            shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
            print(f"Output: {Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, user_input)}")
        elif shift == "/":
            break
        else:
            print("Input has to be an integer.")
