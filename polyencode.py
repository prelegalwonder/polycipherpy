#!/usr/bin/python

import string
import sys

preshiftEncode = {'A':1,'B':2,'C':3,'D':4,'E':5}
preshiftEncode.update({'F':6,'G':7,'H':8,'I':9,'J':10,'K':11})
preshiftEncode.update({'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17})
preshiftEncode.update({'R':18,'S':19,'T':20,'U':21,'V':22,'W':23})
preshiftEncode.update({'X':24,'Y':25,'Z':0})

preshiftDecode = {1:'A',2:'B',3:'C',4:'D',5:'E'}
preshiftDecode.update({6:'F',7:'G',8:'H',9:'I',10:'J',11:'K'})
preshiftDecode.update({12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q'})
preshiftDecode.update({18:'R',19:'S',20:'T',21:'U',22:'V',23:'W'})
preshiftDecode.update({24:'X',25:'Y',0:'Z'})

def wordEncode(word):

    wordArray = word.upper().split(' ')
    encWordArray = []

    for word in wordArray:
        ltrArray = list(word)
        encLtrArray = []
        if len(ltrArray) < 2:
            ltrDec = preshiftDecode[abs(0)]
            encLtrArray.append(ltrDec)
            encodedWord = ''.join(encLtrArray)
            encWordArray.append(encodedWord)
            continue
        ltrpos = 0
        for ltr in ltrArray:
            if ltr == ltrArray[0]:
                curltr = preshiftEncode[ltr]
                nxtltr = preshiftEncode[ltrArray[1]]
                newltr = int(curltr) - int(nxtltr)
                ltrDec = preshiftDecode[abs(newltr)]
            elif ltr == ltrArray[-1]:
                curltr = preshiftEncode[ltr]
                fstltr = preshiftEncode[ltrArray[0]]
                newltr = int(curltr) - int(fstltr)
                ltrDec = preshiftDecode[abs(newltr)]
            else:
                arrayPos = ltrpos + 1
                curltr = preshiftEncode[ltr]
                nxtltr = preshiftEncode[ltrArray[arrayPos]]
                newltr = int(curltr) - int(nxtltr)
                ltrDec = preshiftDecode[abs(newltr)]
            encLtrArray.append(ltrDec)
            ltrpos = ltrpos+1

        encodedWord = ''.join(encLtrArray)
        encWordArray.append(encodedWord)
    print encWordArray


word = sys.argv[1]
wordEncode(word)
