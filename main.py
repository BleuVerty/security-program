from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as sc
import os
import time
import threading

# ===== Window Render =====
root = Tk()
root.geometry('870x558')
root.resizable(False, False)
root.title('Security [BlueVerty]')
root.configure(background='Whitesmoke')
root.iconbitmap('icone.ico')

# ===== Functions =====
def openfile():
    global tf
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/",
        title = '[BlueVerty] Ouvrir un fichier',
        filetypes=(("Text Files", "*.txt"), 
                ("PDF Files", "*.pdf"), 
                ("WORD Files", "*.docx"), 
                ("PPT Files", "*.pptx"), 
                ("Obsidian Files", "*.md"))
    )

    en1.insert(END, tf)
    global filesize1
    filesize1 = os.path.getsize(tf) 
    f2_l2_en.insert(END, filesize1)

def secure():
    while True:
        size = os.path.getsize(tf)
        if filesize1 == size :
            txt.insert('end', '[✅]>', 'Normal')
            txt.insert('end', ' Ce fichier est sain : ', 'Green')
            txt.insert('end', time.ctime(), 'Normal')
            txt.insert('end', '\n\n')
            get_time = int(f2_l3_en.get())
            time.sleep(get_time)
            continue
        else:
            txt.insert('end', '[❌]>', 'Normal')
            txt.insert('end', ' Une menace a été détecté : ', 'Red')
            txt.insert('end', time.ctime(), 'Normal')
            txt.insert('end', '\n----------------------------------------------------------------------\n')
            break

def launch():
    threading.Thread(target=secure).start()

# ===== Title Top =====
title = Label(root, 
            text='Programme de sécurité | v_1.0.0', 
            font=('Inter',16), 
            bg='#5588AA', 
            fg='white'
            )
title.pack(fill=X)

# ===== Image Label =====
image = PhotoImage(file='logo.png')
panel = Label(root, image=image)
panel.place(x=4, y=36)

# ===== Button Load File =====
button = Button(root, 
                text='Séléctionner le fichier', 
                cursor='hand2', 
                bg='#5588AA', 
                fg='white', 
                bd=0, relief=RIDGE,
                command=openfile
                )
button.place(x=6, y=236, width=275, height=34)

# ===== Entry to path =====
en1 = Entry(root, font=('Inter',12))
en1.place(x=6, y=286, width=275, height=34)

# ===== Frame : Label with Entry =====
f2 = Frame(root, width=275, height=216, bg='white', bd=0, relief=GROOVE)
f2.place(x=6, y=336)

# ===== 1er Title Frame =====
f2_l1 = Label(f2, 
            text='Propriétés du fichier :', 
            bg='white', fg='black', 
            font=('Inter',12))
f2_l1.place(x=5, y=10)

# ===== File size Label 2 =====
f2_l2 = Label(f2, 
            text='Taille du fichier', 
            bg='white', fg='black', 
            font=('Inter',11))
f2_l2.place(x=15, y=50)
# ===== File size Entry =====
f2_l2_en = Entry(f2, 
                font=('Inter',11), 
                justify=CENTER, 
                bg='whitesmoke')
f2_l2_en.place(x=15, y=74, width=124, height=32)

# ===== File size Label 3 =====
f2_l3 = Label(f2, 
            text='Temps', 
            bg='white', 
            fg='black', 
            font=('Inter',11))
f2_l3.place(x=160, y=50)
# ===== File size Entry Label 3 =====
f2_l3_en = Entry(f2, 
                font=('Inter',11), 
                justify=CENTER, 
                bg='whitesmoke')
f2_l3_en.place(x=160, y=74, width=82, height=32)

# ===== Title Security Label =====
f2_l4 = Label(f2, 
            text='Démarrer la sécurité de votre ficher', 
            bg='white', fg='black', 
            font=('Inter',11))
f2_l4.place(x=10, y=118)

# ===== Start Button =====
scan_logo = PhotoImage(file='scan.png')
f2_b1 = Button(f2, text='   Vérifier maintenant', 
            cursor='hand2', 
            image=scan_logo, compound=LEFT, 
            width=240, 
            bd=0, relief=RIDGE, 
            bg='#5588AA',
            fg='#FFF',
            command=launch
            )
f2_b1.place(x=10, y=150)

#===== Text Results =====
txt = sc.ScrolledText(root, bg='#FFF')
txt ['font'] = ('Iner', '12')
txt.place(x=295, y=37, width= 575, height=516)
txt.tag_config('Green', background='green', foreground='white')
txt.tag_config('Normal', background='white', foreground='black')
txt.tag_config('Red', background='red', foreground='white')


# ===== Window Render =====
root.mainloop()