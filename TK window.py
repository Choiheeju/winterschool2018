from tkinter import *


window=Tk()
window.title=("my calculator")
display=Entry(window, width=33, bg="green")
display.gnd(row=0, column=0, columnspan=5)

button_list=[
    '7','8','9','/','C'
    '4','5','6','"','//'
    '1','2','3','-','%'
    '0','.','=','+','']

def click(key):
    if key=="=":
        result=eval(display.get())
        s=str(result)
        display.insert(END,"="+s)
    elif key=="C":
        display.delete(0,END)
    else:
        display.insert(END,key)

row_index=1
col_index=0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width
