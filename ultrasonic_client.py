import tkinter as tk
import tkinter.font
from gpiozero import LED

root=tk.Tk()
root.title("Your LED Buttons")
myFont=tkinter.font.Font(family='Helvetica', size=12, weight="bold")
led=LED(21)
def ledToggle():
  if led.is_lit:
    led.off()
    ledButton["text"]="Turn on your LED"
  else:
    led.on()
    ledButton["text"]="Turn off your LED"
def exitProgram():
    root.quit()

ledButton=tk.Button(root, text="Turn on your LED", font=myFont, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=0, sticky=tk.NSEW)
exitButton=tk.Button(root, text='Goodbye', font=myFont, command=exitProgram, bg='cyan', height=1, width=6)
exitButton.grid(row=1, sticky=tk.E)

tk.mainloop()
