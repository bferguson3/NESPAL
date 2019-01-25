#######################################################
# NES PAL Tool for Python 3- (c) 2018 Ben Ferguson
# SET to PPU Converter
#
# Usage: $ python3 settoppu.py
#
# Takes one file: INPUT.SET (saved from YY-CHR)
# Outputs two files: OUTPUT.NAM (1kB namespace file)
#    and OUTPUT.ATR (64-byte attribute file)
#
# version 1.1:
#  Optional usage: $ python3 settoppu.py <inputfile>.set
#   This usage will output <inputfile>.nam and <inputfile>.atr!
#
# Both of these files can be loaded directly into RAM
# using your favorite NES assembler!
#######################################################

import sys 

if len(sys.argv) == 2:
    filenam_arg = sys.argv[1]

bytes_read = [] 

if len(sys.argv) == 1:
    with open("input.set", "rb") as f:
        bytes_read = f.read()
    f.close()
elif len(sys.argv) == 2:
    with open(filenam_arg, "rb") as f:
        bytes_read = f.read()
    f.close()

output = bytearray()
output2 = bytearray()

c = 0 
while c < 960:
    output.append(bytes_read[c])
    c += 1

c = 960
while c < (960*2):
    n = 0
    while n < 32:
        parsed = bytes_read[c+n]
        parsed = parsed & 3
        output2.append(parsed) 
        n += 2
    c += 64    

atr_out = bytearray()

v = 0
while v < 224:
    n = 0
    while n < 16:
        parsing = output2[17+v+n] << 6
        parsing = parsing | (output2[16+v+n] << 4)
        parsing = parsing | (output2[1+v+n] << 2)
        parsing = parsing | output2[0+v+n]
        atr_out.append(parsing)
        n += 2
    v += 32

v = 224
while v < 256:
    n = 0
    while n < 16:
        parsing = (output2[1+v+n] << 2)
        parsing = parsing | (output2[v+n])
        atr_out.append(parsing)
        n +=2
    v += 32

if len(sys.argv) == 2:
    f = open(filenam_arg[:-4]+'.nam', "wb")
    f.write(output)
    f.close()
    f = open(filenam_arg[:-4]+'.atr', "wb")
    f.write(atr_out)
    f.close()
    print(filenam_arg[:-4]+'.nam and '+filenam_arg[:-4]+'.atr written successfully.')
else:
    f = open("output.nam", "wb")
    f.write(output)
    f.close()
    f = open("output.atr", "wb")
    f.write(atr_out)
    f.close()
    print('output.nam and output.atr written successfully.')
 