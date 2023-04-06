# Vending Machine : You can buy beverages from here and get a recipt from your purchase
# Designed, created and crafted by SoroushMBabaei!
# Before doing anything, please enter the following command in your Terminal:
# pip install random-poem
 
# -----Libraries-----
from tkinter import Tk,Label,Button
from time import strftime,sleep
from random_poem import get_poem
# -----TKinter Window Creating-----
mainpage = Tk()
mainpage.title("Vending Machine")
# -----Functions-----
def counter(button):
    global fantaCounter,pepsiCounter,canadaCounter,sevenupCounter,spriteCounter
    if button == "FantaUp":
        fantaCounter += 1
        fantaLabel.config(text=f"Fanta:{fantaCounter}")
    elif button == "PepsiUp":
        pepsiCounter += 1
        pepsiLabel.config(text=f"Pepsi:{pepsiCounter}")
    elif button == "CanadaUp":
        canadaCounter += 1
        canadaLabel.config(text=f"Canada:{canadaCounter}")
    elif button == "SevenupUp":
        sevenupCounter += 1
        sevenupLabel.config(text=f"7Up!:{sevenupCounter}")
    elif button == "SpriteUp":
        spriteCounter += 1
        spriteLabel.config(text=f"Sprite:{spriteCounter}")
    elif button == "FantaDown":
        fantaCounter -= 1
        fantaLabel.config(text=f"Fanta:{fantaCounter}")
    elif button == "PepsiDown":
        pepsiCounter -= 1
        pepsiLabel.config(text=f"Pepsi:{pepsiCounter}")
    elif button == "CanadaDown":
        canadaCounter -= 1
        canadaLabel.config(text=f"Canada:{canadaCounter}")
    elif button == "SevenupDown":
        sevenupCounter -= 1
        sevenupLabel.config(text=f"7Up!:{sevenupCounter}")
    elif button == "SpriteDown":
        spriteCounter -= 1
        spriteLabel.config(text=f"Sprite:{spriteCounter}")

def pricing():
    global fantaCounter,pepsiCounter,canadaCounter,sevenupCounter,spriteCounter
    return [(fantaCounter * 13300),(pepsiCounter * 13300),(canadaCounter * 13300),(sevenupCounter * 13300),(spriteCounter * 13300)]

def savingFile():
    saveButton["state"] = "disabled"
    prices = pricing()
    totalPrice = 0
    for price in prices:
        totalPrice += price
    reciptTime = strftime("%H:%M:%S")
    reciptFile = open("Recipt.txt","a")
    reciptFile.write(30*".-.")
    reciptFile.write(f"\nTime of export:{reciptTime}")
    reciptFile.write(f"\nFanta:{prices[0]}\nPepsi:{prices[1]}\nCanada:{prices[2]}\n7Up!:{prices[3]}\nSprite:{prices[4]}\nTotal:{totalPrice}\n")
    reciptFile.write(f"\n{get_poem()}")
    reciptFile.close()
    sleep(3)
    saveButton["state"] = "normal"
# -----Variables-----
fantaCounter = 0
pepsiCounter = 0
canadaCounter = 0
sevenupCounter = 0
spriteCounter = 0
# -----Widgets-----
fantaLabel = Label(mainpage,text=f"Fanta:{fantaCounter}",font=("Consolas",16),bg="orange",fg="yellow")
fantaUpperButton = Button(mainpage,text="Up",font=("Consolas",16),command=lambda:counter("FantaUp"))
fantaLowerButton = Button(mainpage,text="Down",font=("Consolas",16),command=lambda:counter("FantaDown"))

pepsiLabel = Label(mainpage,text=f"Pepsi:{pepsiCounter}",font=("Consolas",16),bg="navy",fg="red")
pepsiUpperButton = Button(mainpage,text="Up",font=("Consolas",16),command=lambda:counter("PepsiUp"))
pepsiLowerButton = Button(mainpage,text="Down",font=("Consolas",16),command=lambda:counter("PepsiDown"))

canadaLabel = Label(mainpage,text=f"Canada:{canadaCounter}",font=("Consolas",16),bg="darkred",fg="white")
canadaUpperButton = Button(mainpage,text="Up",font=("Consolas",16),command=lambda:counter("CanadaUp"))
canadaLowerButton = Button(mainpage,text="Down",font=("Consolas",16),command=lambda:counter("CanadaDown"))

sevenupLabel = Label(mainpage,text=f"7Up!:{sevenupCounter}",font=("Consolas",16),bg="darkgreen",fg="yellow")
sevenupUpperButton = Button(mainpage,text="Up",font=("Consolas",16),command=lambda:counter("SevenupUp"))
sevenupLowerButton = Button(mainpage,text="Down",font=("Consolas",16),command=lambda:counter("SevenupDown"))

spriteLabel = Label(mainpage,text=f"Sprite:{spriteCounter}",font=("Consolas",16),bg="green",fg="white")
spriteUpperButton = Button(mainpage,text="Up",font=("Consolas",16),command=lambda:counter("SpriteUp"))
spriteLowerButton = Button(mainpage,text="Down",font=("Consolas",16),command=lambda:counter("SpriteDown"))

saveButton = Button(mainpage,text="Save",font=("Consolas",16),bg="darkred",fg="white",command=lambda:savingFile())
# -----Griding-----
fantaLabel.grid(row=0 ,column=0 ,sticky="nsew")
fantaUpperButton.grid(row=1 ,column=0 ,sticky="nsew")
fantaLowerButton.grid(row=2 ,column=0,sticky="nsew")
pepsiLabel.grid(row=0 ,column=1 ,sticky="nsew")
pepsiUpperButton.grid(row=1 ,column=1 ,sticky="nsew")
pepsiLowerButton.grid(row=2 ,column=1 ,sticky="nsew")
canadaLabel.grid(row=0 ,column=2 ,sticky="nsew")
canadaUpperButton.grid(row=1 ,column=2 ,sticky="nsew")
canadaLowerButton.grid(row=2 ,column=2 ,sticky="nsew")
sevenupLabel.grid(row=0 ,column=3 ,sticky="nsew")
sevenupUpperButton.grid(row=1 ,column=3 ,sticky="nsew")
sevenupLowerButton.grid(row=2 ,column=3 ,sticky="nsew")
spriteLabel.grid(row=0 ,column=4 ,sticky="nsew")
spriteUpperButton.grid(row=1 ,column=4 ,sticky="nsew")
spriteLowerButton.grid(row=2 ,column=4 ,sticky="nsew")
saveButton.grid(row=3 ,column=0 ,columnspan=5 ,sticky="nsew")
mainpage.mainloop()