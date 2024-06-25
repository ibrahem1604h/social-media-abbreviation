from tkinter import *
import webbrowser

root=Tk()
root.title("abbreviation")
root.geometry("500x200")
root.configure(bg="#12617D")

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

frame=Frame(root)
frame.grid(row=1,column=0)

def youtupe():
    webbrowser.open("https://www.youtube.com/")
def feacbock():
    webbrowser.open("https://www.facebook.com/")
def tiktok():
    webbrowser.open("https://www.tiktok.com/foryou")
def tweter():
    webbrowser.open("https://x.com/home")

lable_frame=Frame(root)
lable_frame.grid(row=0,column=0,pady=10)

label=Label(lable_frame,text="Choose social media website:",font=("Arial",20))
label.grid(row=0,column=0)

youtupe_buttom=Button(frame,text="YOUTUPE",fg="white",bg="red",command=youtupe)
feacbock_buttom=Button(frame,text="FACEBOOK",fg="white",bg="blue",command=feacbock)
tiktok_buttom=Button(frame,text="TIKTOK",fg="white",bg="black",command=tiktok)
X_buttom=Button(frame,text="TWETER",fg="white",bg="#1DA1F2",command=tweter)

youtupe_buttom.grid(row=0,column=4)
feacbock_buttom.grid(row=0,column=6)
tiktok_buttom.grid(row=0,column=8)
X_buttom.grid(row=0,column=9)

frame.grid_columnconfigure(0,weight=1)
frame.grid_columnconfigure(0,weight=2)
frame.grid_columnconfigure(0,weight=3)
frame.grid_columnconfigure(0,weight=4)

root.mainloop()
