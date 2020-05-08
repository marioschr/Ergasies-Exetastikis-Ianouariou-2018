from __future__ import print_function # Για να μπορούν να τυπωθούν οι χαρακτήρες ο ένας δίπλα από τον άλλο

def bf(text, left, right, data, index):
    if len(text) == 0: return
    if left < 0: left = 0
    if left >= len(text): left = len(text) - 1
    if right < 0: right = 0
    if right >= len(text): right = len(text) - 1

    array = [0] * 30000
    pointer = 0
    i = left
    print ('To metafrasmeno keimeno einai: ', end="")
    while i <= right:
        s = text[i]
        if s == '>':
            pointer += 1
            if pointer >= len(array):
                pointer = 0
        elif s == '<':
            pointer -= 1
            if pointer < 0:
                pointer = len(array) - 1
        elif s == '+':
            array[pointer] += 1
        elif s == '-':
            array[pointer] -= 1
        elif s == '.':
            print(chr(array[pointer]), end="")
        elif s == ',':
            if index >= 0 and index < len(data):
                array[pointer] = ord(data[index])
                index += 1
            else:
                array[pointer] = 0
        elif s =='[':
            if array[pointer] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = text[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = text[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1

#main
text = raw_input("Dose kodika se brainfuck: ")
bf(text,0,len(text)-1,"",0)
