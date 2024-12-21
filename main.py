import string
from os import system
import tkinter
import tkinter.filedialog

root = tkinter.Tk()
root.withdraw()
FILETYPES = [("All files", "*.*")]

ALPHABET, ALPHABET_UPPER = [*string.ascii_lowercase], [*string.ascii_uppercase]
COMMAND = [*"12"]

def check(arg1, arg2) -> bool:
    for k in arg1:
        if k in arg2:
            return True
    return False

def Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, user_input) -> str:
    output = ""
    for k in user_input:
        if k in ALPHABET:
            output += shifted[ALPHABET.index(k)]
        elif k in ALPHABET_UPPER:
            output += shifted_upper[ALPHABET_UPPER.index(k)]
        else:
            output += k
    return output

def fileProcessor(file_name, ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, output_file) -> None:
    try:
        with open(file_name, encoding="utf-8") as data:
            with open(output_file, "w", encoding="utf-8") as out:
                out.write(Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, data.read()))
    except UnicodeDecodeError:
        with open(file_name, encoding="latin-1") as data:
            with open(output_file, "w", encoding="latin-1") as out:
                out.write(Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, data.read()))

def IsInt(inp) -> bool:
    try:
        int(inp)
        return True
    except ValueError:
        return False

def main() -> None:
    system("cls")
    while True:
        cmd = input("""1. Enciphering.
2. Deciphering. 
3. Exit. \n
Your input: """).strip()
        if cmd == "3":
            exit(0)
        elif not cmd:
            system("cls")
            print("Invalid input: Empty input.")
            continue
        elif cmd not in COMMAND:
            system("cls")
            print("Invalid input: Command does not exist.")
            continue
        
        system("cls")
        mode = input("""1. Input from keyboard.
2. Input from file.
3. Cancel. \n
Your input: """).strip()
        if mode == "3":
            system("cls")
            continue

        elif mode == "1":
            while True:
                user_input = [*input("Your input: ").strip()]
                if not user_input:
                    print("Invalid input: Empty input.")
                else:
                    break
        
            while True:
                system("cls")
                shift = input("Shift (type / to cancel): ").strip()
                if IsInt(shift) and cmd == "1":
                    shift = int(shift)
                    shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
                    shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
                    print(f"Output: {Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, user_input)}")
                elif IsInt(shift) and cmd == "2":
                    shift = -int(shift)
                    shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
                    shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
                    print(f"Output: {Caesar(ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, user_input)}")
                elif shift == "/":
                    break
                elif not shift:
                    print("Invalid input: Empty input.")
                else:
                    print("Invalid input: Not an integer.")

        elif mode == "2":
            system("cls")
            input_file = tkinter.filedialog.askopenfilename(title="Choose your input file (cancel to go back to menu)", filetypes=FILETYPES)
            if not input_file:
                continue

            system("cls")
            while True:
                output_file = input("""Type the name of your output file, leave empty for the default name (output.txt)
(If the name does not contain an extension then the program will automatically add a .txt extension): """).strip()
                if check(output_file, [*'\\/:*?"<>|']) and len(output_file) != 0:
                    print("Invalid input: Illegal file name (file name cannot contains \"\\/:*?\"<>|\").")
                elif not output_file:
                    output_file = "output.txt"
                    break
                elif output_file[len(output_file) - 1] != "." or "." not in output_file:
                    output_file += ".txt"
                    break

            while True:
                system("cls")
                shift = input("Shift (type / to cancel): ").strip()
                if IsInt(shift) and cmd == "1":
                    shift = int(shift)
                    shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
                    shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
                    fileProcessor(input_file, ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, output_file)
                elif IsInt(shift) and cmd == "2":
                    shift = -int(shift)
                    shifted =  ALPHABET[shift % 26:] + ALPHABET[:shift % 26]
                    shifted_upper = ALPHABET_UPPER[shift % 26:] + ALPHABET_UPPER[:shift % 26]
                    fileProcessor(input_file, ALPHABET, shifted, ALPHABET_UPPER, shifted_upper, output_file)
                elif shift == "/":
                    system("cls")
                    break
                elif not shift :
                    print("Invalid input: Empty input.")
                else:
                    print("Invalid input: Not an integer.")
        else:
            print("Invalid input: Not a valid option.")
        
if __name__ == "__main__":
    main()
