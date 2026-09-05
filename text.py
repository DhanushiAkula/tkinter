from tkinter import *
from tkinter . filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("codingal the text editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(0,minsize=800,weight=1)
def open_file():
    """open a file for editing"""
    filepath=askopenfilename(
        filetypes=[("text files","*.txt"),("all files","*.*")]
        )
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"codingle itext editor-{filepath}")
def save_file():
    filepath=asksaveasfilename(
        defaulttextension="txt",
        filetypes=[("Text Files","*.txt"),("ALL Files","*.*")])

    if not filepath:
        return
    with open(filepath,"w")as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"codingle text editor -{filepath}")
txt_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="Open",command=open_file)
btn_save=Button(fr_button,text  ="Save_As...",command=save_file)
btn_open.grid(row=0,column=0,sticky="ew",padx=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)
fr_button.grid(row=0,column=0,sticky="ew",padx=5)
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()



    
