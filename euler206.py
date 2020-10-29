# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

#1a2b3c4d5e6f7g8h9j0

import sys

for i in range(1400000000,999999999,-1):
    r = i**2
    if i % 1000000 == 0:
        print('Tussenstandje: ', r, i)
    if len(str(r)) == 19:
        if r % 10 == 0:
            if int(str(r)[:1]) == 1:
                if int(str(r)[2:3]) == 2:
                    if int(str(r)[4:5]) == 3:
                        if int(str(r)[6:7]) == 4:
                            if int(str(r)[8:9]) == 5:
                                if int(str(r)[10:11]) == 6:
                                    if int(str(r)[12:13]) == 7:
                                        if int(str(r)[14:15]) == 8:
                                            if int(str(r)[16:17]) == 9:
                                                print('Square: ', r,' Result:', i)
                                                sys.exit()