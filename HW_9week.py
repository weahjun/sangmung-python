from tkinter import *
window = Tk()

photo = PhotoImage(file="C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif")
label = Label(window, image = photo)

photo2 = PhotoImage(file ="C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif")
label2 = Label(window, image = photo)


label.pack(side=RIGHT)
label2.pack(side=LEFT)


window.mainloop()
