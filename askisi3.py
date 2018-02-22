def rot13(metatropi):
    result = ""

    #epanalipsi gia olous tous xaraktires
    for v in metatropi:
        chartonum = ord(v)
        if chartonum >= ord('a') and chartonum <= ord('z'):
            if chartonum > ord('m'):
                chartonum -= 13
            else:
                chartonum += 13
        elif chartonum >= ord('A') and chartonum <= ord('Z'):
            if chartonum > ord('M'):
                chartonum -= 13
            else:
                chartonum += 13
        #prosthesi twn grammatwn sto apotelesma
        result += chr(chartonum)
    return result

while True:
        keimeno = raw_input("Grapse keimeno gia kryptografisi se ROT-13 (Grapste 0 gia eksodo):")
        if (keimeno!='0'):
            print "To kryptografimeno keimeno einai:", rot13(keimeno)
        else: break
