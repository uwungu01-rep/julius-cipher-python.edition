import string
alpup, alp = [*string.ascii_uppercase], [*string.ascii_lowercase]

def sort():
    #Sorting algorithm, take the last characters in the alp/alpup and put it at the start of the cip/cipup for a ceratian almount of times, decided by shf
    #The rest of the alp/alpup get put into cip/cipup without any change
    for k in range(shf, len(alp) + shf):
        if k < len(alp):
            cip.append(alp[k])
            cipup.append(alpup[k])
            continue

        cip.append(alp[abs(k - len(alp))])
        cipup.append(alpup[abs(k - len(alp))])

def encipher(alp, cip, alpup, cipup, chr):
    oupt = ""
    #This find the position of k in alp/alpup then add the element with the same position as k in cip/cipup to oupt
    for k in chr:
        if k in alp:
            oupt += cip[alp.index(k)]
            continue
        elif k in alpup:
            oupt += cipup[alpup.index(k)]
            continue
        oupt += k
    return oupt
 
def decipher(alp, cip, cipup, alpup, chr):
    oupt = ""
    #This does the exact opposite as encipher
    for k in chr:
        if k in cip:
            oupt += alp[cip.index(k)]
        elif k in cipup:
            oupt += alpup[cipup.index(k)]
        else:
            oupt += k
    return oupt

while True:
    bck = True
    cmd = input("Type E for enciphering, type D for deciphering (case insensitive). Type / to end the program: ")
    if cmd == "e" or cmd == "E":
        while True:
            #Check if the user has input "/" to cancel enciphering or not
            if bck:
                chr = [*input("Your input: ")]
                if len([x for x in chr if x != " "]) != 0:
                    while True:
                        cip, cipup = [], []
                        shf = input("Shift (type / to cancel): ")
                        if shf.isnumeric() or "-" in [x for x in shf] and [x for x in shf].index("-") == 0:
                            shf = int(shf) % 26
                            sort()
                            print(f"Output: {encipher(alp, cip, alpup, cipup, chr)}")
                        elif shf == "/":
                            bck = False
                            break
                        else:
                            print("Input has to be an integer.")
                else:
                    print("Input cannot be empty.")
            else:
                break
                
    #This elif block essentially do the same thing as the if block above
    elif cmd == "d" or cmd ==" D":
        while True:
            if bck:
                chr = [*input("Your input: ")]
                if len([x for x in chr if x != " "]) != 0:
                    while True:
                        cip, cipup = [], []
                        shf = input("Shift (type / to cancel): ")
                        if shf.isnumeric() or "-" in [x for x in shf] and [x for x in shf].index("-") == 0:
                            shf = int(shf) % 26
                            sort()
                            print(f"Output: {decipher(alp, cip, cipup, alpup, chr)}")
                        elif shf == "/":
                            bck = False
                            break
                        else:
                            print("Input has to be an integer.")
                else:
                    print("Input cannot be empty.")
            else:
                break

    elif cmd == "/":
        exit()
    else:
        print("Invalid command.")