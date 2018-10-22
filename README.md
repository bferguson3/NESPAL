# NESPAL
A set of Python tools for NES Assembly

1. nespal.py - NES .PAL creation tool
2. SETtoPPU.py - Splits yy-chr .SET into two NES-ASM compatible files:
   960-byte .NAM (nametable) and 
   64-byte .ATR (attribute)

![alt text](https://github.com/bferguson3/NESPAL/blob/master/nespal.png)

# NES Palette Pal - a .PAL generator for NES

 (c) 2018 Ben Ferguson

 Use Python 3!
 
 Assembles a proper 32-byte palette file 
 for use with NES-based 6502 compilers.
 Easy point-and-click interface.

Usage is super easy.
Uses only tkinter library, so it should work on any Python3 compatible system.

$ python3 nespal.py

If 'output.pal' already exists in the script folder, it will be loaded automatically.

Click the color you want, then click the palette number to assign it.
When you're done, click the Save PAL file button, and 'output.pal' file will be created in the same folder in which you ran the pyton script. 

(The unused spaces in the PPU palette block stored in $3f04 etc. are filled in with duplicates of $3f00.)

Example usage:
```     
        lda #$3f
        sta $2006
        lda #$00
        sta $2006     ; set PPU write address to $3f00
        ldx #0
pal_loop:
        lda PalData,x
        sta $2007
        inx 
        cpx #32
        bne pal_loop
```
Then include:
```
PalData:
        .incbin "output.pal"
```

Enjoy!

# SET to PPU - A yy-chr to assembly converter

(c) 2018 Ben Ferguson / Python3

For now, this tool only works if an 'input.set' file is in the same folder as the .py file.

Usage:

$ python3 settoppu.py

If found, it will output two files in the same directory: 'output.nam', a 960-byte namespace file, and 'output.atr', a 64-byte attribute file (normally loaded at the end of namespaces, e.g. @ $23c0).

Example usage:
```
; Fill In Background
        lda #$20
        sta $2006
        lda #$00        
        sta $2006        ; namespace address $2000
        ldx #0
.FillLoop:
        lda MapData,x 
        sta $2007
        inx
        cpx #255
        bne .FillLoop   
        
        ldx #0
.FillLoop2:
        lda MapData+256,x
        sta $2007 
        inx 
        cpx #255 
        bne .FillLoop2

        ldx #0
.FillLoop3:
        lda MapData+512,x
        sta $2007 
        inx 
        cpx #255 
        bne .FillLoop3

        ldx #0
.FillLoop4:
        lda MapData+(256*3),x 
        sta $2007 
        inx 
        cpx #$c0
        bne .FillLoop4
        
        lda #$23
        sta $2006
        lda #$c0
        sta $2006
        ldx #0
.color_bg_loop:
        lda MapAttr,x
        sta $2007
        inx 
        cpx #64
        bcc .color_bg_loop
```
Included with:
```
MapData:
    .incbin "output.nam"
MapAttr:
    .incbin "output.atr"
```
