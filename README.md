# NESPAL
Python NES .PAL assembler
![alt text](https://github.com/bferguson3/NESPAL/blob/master/nespal.png)

 NES Palette Pal - a .PAL generator for NES

 (c) 2018 Ben Ferguson

 Use Python 3!
 
 Assembles a proper 32-byte palette file 
 for use with NES-based 6502 compilers.
 Easy point-and-click interface.

Usage is super easy.
Uses only tkinter library, so it should work on any Python3 compatible system.

$ python3 nespal.py

Click the color you want, then click the palette number to assign it.
When you're done, click the Save PAL file button, and 'output.pal' file will be created in the same folder in which you ran the pyton script. 

(The unused spaces in the PPU palette block stored in $3f04 etc. are filled in with duplicates of $3f00.)

Example usage:
```       
        ldx #0
pal_loop:
        lda PalData,x
        sta $2007
        inx 
        cpx #32
        bne pal_loop
        
PalData:
        .incbin "output.pal"
```

Enjoy!
