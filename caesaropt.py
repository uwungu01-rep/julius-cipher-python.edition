import string       
alpup, alp = [*string.ascii_uppercase], [*string.ascii_lowercase]

def sort():
    #Sorting algorithm, take the last characters in the alp/alpup and put it at the start of the cip/cipup for a ceratian almount of times, decided by shf
    #The rest of the alp/alpup get put into cip/cipup without any change
    for k in range(int(shf), len(alp) + int(shf)):
        if k in range(len(alp)):
            cip.append(alp[k])
            cipup.append(alpup[k])
        else:
            cip.append(alp[abs(k - len(alp))])
            cipup.append(alpup[abs(k - len(alp))])

def encipher(alp, oupt, cip, alpup, cipup, chr):
    oupt = ""
    #This find the position of k in alp/alpup then add the element with the same position as k in cip/cipup to oupt
    for k in chr:
        if k in alp:
            oupt += cip[alp.index(k)]
        elif k in alpup:
            oupt += cipup[alpup.index(k)]
        else:
            oupt += k
    return oupt
 
def decipher(alp, oupt, cip, cipup, alpup, chr):
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
    bck = False
    cmd = input("Type e for enciphering, type d for deciphering (case insensitive). Type / to end the program: ")
    if cmd == "e" or cmd == "E":
        while True:
            #Check if the user has input "/" to cancel enciphering or not
            if bck:
                break
            chr = [*input("Type your string: ")]
            while True:
                cip, cipup = [], []
                shf = input("Shift (from 1 to 25) (type / to cancel): ")
                if shf.isnumeric() == True and 1 <= int(shf) <= 25:
                    sort()
                    print("Output:", encipher(alp, cip, alpup, cipup, chr))
                elif shf == "/":
                    bck = True
                    break
                else:
                    print("Input has to be an interger from 1 to 25.")
                
    #This elif block essentially do the same thing as the if block above
    elif cmd == "d" or cmd ==" D":
        while True:
            if bck:
                break
            chr = [*input("Type your enciphered string: ")]
            while True:
                cip, cipup = [], []
                shf = input("Shift (from 1 to 25) (type / to cancel): ")
                if shf.isnumeric() == True and 1 <= int(shf) <= 25:
                    sort()
                    print("Output:", decipher(alp, cip, cipup, alpup, chr))
                elif shf == "/":
                    bck = True
                    break
                else:
                    print("Input has to be an interger from 1 to 25.")
    elif cmd == "/":
        exit()
    else:
        print("Invalid command.")
