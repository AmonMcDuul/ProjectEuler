# A common security method used for online banking is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

cards = set()
for item in open("euler79passcodes.txt", "r"):
    cards.add(item.strip()) 

print(sorted(cards))

# resultaat: 73162890

# Met de hand:
# /129
# /160
# /162
# /168
# /180
# /289
# /290
# /316
# /318
# /319
# /362
# /368
# /380
# /389
# /620
# /629
# /680
# /689
# /690
# /710
# /716
# /718
# /719
# /720
# /728
# /729
# /731
# /736
# /760
# /762
# /769
# /790
# /890