from tkinter import*
import random

root=Tk()
root.geometry("600x500")

items=['bottle','blanket','food','tennis racket','shoes','tissues']

lbl=Label(root)
anslbl=Label(root)
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
anslbl.place(relx=0.5,rely=0.7,anchor=CENTER)

lbl['text']="Items:" +str(items)

def num():
    k=random.randint(0,len(items)-1)
    pick=items[k]
    anslbl['text']='put the ' +pick+ ' in the bag'
    
btn=Button(root,text='which item goes in the bag?',command=num)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)   

root.mainloop()

