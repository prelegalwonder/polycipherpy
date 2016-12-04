#!/usr/bin/python

import string
import sys
import math

# This would be equivalent to hardcoded public key.
# Ideally this would be passed in as a dict instead of
# stored within the script.
# Every letter is assigned a prime.

preshiftEncode = {'A':2,'B':3,'C':5,'D':7,'E':11}
preshiftEncode.update({'F':13,'G':17,'H':19,'I':23,'J':29,'K':31})
preshiftEncode.update({'L':37,'M':41,'N':43,'O':47,'P':53,'Q':59})
preshiftEncode.update({'R':61,'S':67,'T':71,'U':73,'V':79,'W':83})
preshiftEncode.update({'X':89,'Y':97,'Z':101})

# For all intents, wordEncode is the algorithm. This
# algorithm takes the value of the current letter in
# preshiftencode and multiplies it by the value of the
# next letter in the array to arrive at a semiprime
# for the current letter. Rinse and repeat.

def wordEncode(word):

    wordArray = word.upper().split(' ')
    encWordArray = []

    for word in wordArray:
        ltrArray = list(word)
        encLtrArray = []
        ltrpos = 0
        for ltr in ltrArray:
            # in the event of a single letter word,
            # multiply by a unique prime outside of
            # the assigned matrix for easier factoring
            # in the reassembly.
            if len(ltrArray) < 2:
                curltr = preshiftEncode[ltr]
                newltr = int(curltr) * 103
            # is letter first pos in word?
            # if so use next letter for multiplier
            elif ltr == ltrArray[0]:
                curltr = preshiftEncode[ltr]
                nxtltr = preshiftEncode[ltrArray[1]]
                newltr = int(curltr) * int(nxtltr)
            # is letter last pos in word?
            # if so use first letter for multiplier
            elif ltr == ltrArray[-1]:
                curltr = preshiftEncode[ltr]
                fstltr = preshiftEncode[ltrArray[0]]
                newltr = int(curltr) * int(fstltr)
            # is letter in the middle?
            # if so identify next letter
            else:
                arrayPos = ltrpos + 1
                curltr = preshiftEncode[ltr]
                nxtltr = preshiftEncode[ltrArray[arrayPos]]
                newltr = int(curltr) * int(nxtltr)
            encLtrArray.append(newltr)
            ltrpos = ltrpos+1

        encodedWord = ''.join(str(encLtrArray))
        encWordArray.append(encodedWord)
    print encWordArray


word = sys.argv[1]
wordEncode(word)
