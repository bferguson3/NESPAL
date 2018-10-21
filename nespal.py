#########################################################
# NES Palette Pal - a .PAL generator for NES
#
# (c) 2018 Ben Ferguson
#
# Use Python 3!
# 
# Assembles a proper 32-byte palette file 
# for use with NES-based 6502 compilers.
# Easy point-and-click interface.
# Output is always 'output.pal' in the root folder.
##########################################################

nesPalette = [
'#7C7C7C','#0000FC','#0000BC','#4428BC','#940084','#A80020','#A81000','#881400',
'#503000','#007800','#006800','#005800','#004058','#000000','#000000','#000000',
'#BCBCBC','#0078F8','#0058F8','#6844FC','#D800CC','#E40058','#F83800','#E45C10',
'#AC7C00','#00B800','#00A800','#00A844','#008888','#000000','#000000','#000000',
'#F8F8F8','#3CBCFC','#6888FC','#9878F8','#F878F8','#F85898','#F87858','#FCA044',
'#F8B800','#B8F818','#58D854','#58F898','#00E8D8','#787878','#000000','#000000',
'#FCFCFC','#A4E4FC','#B8B8F8','#D8B8F8','#F8B8F8','#F8A4C0','#F0D0B0','#FCE0A8',
'#F8D878','#D8F878','#B8F8B8','#B8F8D8','#00FCFC','#F8D8F8','#000000','#000000'
]
palObj = []

import tkinter as tk 

currentColor = 0

app = tk.Tk()
app.title('PyPAL for NES')

def unclick_all():
    b = 0
    while b < len(palObj):
        palObj[b].unclicked()
        b += 1

class MouseoverTargetCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.lbl = 0
        self.lbl2 = 0
        self.myVal = 0
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.clicked_set)
    
    def on_enter(self, event):
        self.delete(self.lbl)
        self.lbl2 = self.create_text(17, 17, text=hex(self.myVal), fill='white')
        self.lbl = self.create_text(16, 16, text=hex(self.myVal))
    
    def on_leave(self, enter):
        self.delete(self.lbl)
        self.delete(self.lbl2)
    
    def setVal(self, num):
        self.myVal = num

    def clicked_set(self, event):
        global currentColor
        self.setVal(currentColor)
        self.config(background=nesPalette[currentColor])
        self.on_leave(self.on_leave)
        self.on_enter(self.on_enter)

class MouseoverCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.lbl = 0
        self.lbl2 = 0
        self.selector=[]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.clicked)
    
    def on_enter(self, event):
        self.delete(self.lbl)
        self.lbl2 = self.create_text(17, 17, text=hex(self.myVal), fill='white')
        self.lbl = self.create_text(16, 16, text=hex(self.myVal))
    
    def on_leave(self, enter):
        self.delete(self.lbl)
        self.delete(self.lbl2)
    
    def setVal(self, num):
        self.myVal = num

    def unclicked(self):
        b = 0
        while b < len(self.selector):
            self.delete(self.selector[b])
            b += 1

    def clicked(self, event):
        unclick_all()
        self.selector.append(self.create_line(5, 5, scale, 5, width=3, fill='yellow'))
        self.selector.append(self.create_line(5, 5, 5, scale, width=3, fill='yellow'))
        self.selector.append(self.create_line(5, scale, scale, scale, width=3, fill='yellow'))
        self.selector.append(self.create_line(scale, 5, scale, scale, width=3, fill='yellow'))
        global currentColor
        currentColor = self.myVal

scale = 40

c = 0
while c < 64:
    palObj.append(MouseoverCanvas(app, width=scale, height=scale, background=nesPalette[c]))
    palObj[c].setVal(c)
    c += 1

y = 0 
while y < 4:
    x = 0
    while x < 16:
        palObj[(y*16)+x].grid(row=y+1, column=x)
        x +=1
    y += 1

win = tk.Frame(master=app, width=600, height=400)
win.grid(row=0, columnspan=16)

univ_lbl = tk.Label(win, text="$3f00\nBG Color 0 (trans):")
univ_lbl.grid(row=0, column=0)
bg_lbls = tk.Label(win, text="$3f01-03\nBG Palette 0:")
bg_lbls.grid(row=1, column=0)
bg_lbls1 = tk.Label(win, text="$3f05-07\nBG Palette 1:")
bg_lbls1.grid(row=2, column=0)
bg_lbls2 = tk.Label(win, text="$3f09-0b\nBG Palette 2:")
bg_lbls2.grid(row=3, column=0)
bg_lbls3 = tk.Label(win, text="$3f0d-0f\nBG Palette 3:")
bg_lbls3.grid(row=4, column=0)
sp_lbls = tk.Label(win, text="$3f11-13\nSPR Palette 0:")
sp_lbls.grid(row=1, column=4)
sp_lbls1 = tk.Label(win, text="$3f15-17\nSPR Palette 1:")
sp_lbls1.grid(row=2, column=4)
sp_lbls2 = tk.Label(win, text="$3f19-1b\nSPR Palette 2:")
sp_lbls2.grid(row=3, column=4)
sp_lbls3 = tk.Label(win, text="$3f1d-1f\nSPR Palette 3:")
sp_lbls3.grid(row=4, column=4)

univ_bg = MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[0])
univ_bg.setVal(0)
univ_bg.grid(row=0, column=1)

bg_pal = []
c = 0
while c < 3:
    bg_pal.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[1+c]))
    bg_pal[c].grid(row=1, column=c+1)
    bg_pal[c].setVal(c+1)
    c += 1

bg_pal2 = []
c = 0
while c < 3:
    bg_pal2.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[4+c]))
    bg_pal2[c].grid(row=2, column=c+1)
    bg_pal2[c].setVal(c+4)
    c += 1

bg_pal3 = []
c = 0
while c < 3:
    bg_pal3.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[7+c]))
    bg_pal3[c].grid(row=3, column=c+1)
    bg_pal3[c].setVal(c+7)
    c += 1

bg_pal4 = []
c = 0
while c < 3:
    bg_pal4.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[10+c]))
    bg_pal4[c].grid(row=4, column=c+1)
    bg_pal4[c].setVal(c+10)
    c += 1

sp_pal0 = []
c = 0
while c < 3:
    sp_pal0.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[13+c]))
    sp_pal0[c].grid(row=1, column=c+5)
    sp_pal0[c].setVal(c+13)
    c += 1

sp_pal1 = []
c = 0
while c < 3:
    sp_pal1.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[16+c]))
    sp_pal1[c].grid(row=2, column=c+5)
    sp_pal1[c].setVal(c+16)
    c += 1

sp_pal2 = []
c = 0
while c < 3:
    sp_pal2.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[19+c]))
    sp_pal2[c].grid(row=3, column=c+5)
    sp_pal2[c].setVal(c+19)
    c += 1

sp_pal3 = []
c = 0
while c < 3:
    sp_pal3.append(MouseoverTargetCanvas(win, width=scale, height=scale, background=nesPalette[22+c]))
    sp_pal3[c].grid(row=4, column=c+5)
    sp_pal3[c].setVal(c+22)
    c += 1

def write_pal():
    output_bytes=[]
    output_bytes.append(univ_bg.myVal)
    y = 0
    while y < 3:
        output_bytes.append(bg_pal[y].myVal)
        y += 1
    y = 0
    while y < 3:    
        output_bytes.append(bg_pal2[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(bg_pal3[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(bg_pal4[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(sp_pal0[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(sp_pal1[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(sp_pal2[y].myVal)
        y += 1
    y = 0
    while y < 3:
        output_bytes.append(sp_pal3[y].myVal)
        y += 1
    output_bytes.insert(4,univ_bg.myVal)
    output_bytes.insert(8,univ_bg.myVal)
    output_bytes.insert(12,univ_bg.myVal)
    output_bytes.insert(16,univ_bg.myVal)
    output_bytes.insert(20,univ_bg.myVal)
    output_bytes.insert(24,univ_bg.myVal)
    output_bytes.insert(28,univ_bg.myVal)

    output = bytearray(output_bytes)
    f = open('output.pal', 'wb')
    f.write(output)
    f.close()

save_btn = tk.Button(win, text='Save PAL file', command=write_pal)
save_btn.grid(row=2, column=9)

app.config(background='black')
app.mainloop()