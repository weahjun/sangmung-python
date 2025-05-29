from  tkinter import *
from time import *

fnameList = ["C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif", "C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif"]
photoList = [None]*9
num = 0


def clickNext():
    global num 
    num += 1
    if num > 8:
        num = 0
        photo = PhotoImage(file = "gif/" + fnameList[num])
        pLabel.configure(image = photo)
        pLabel.image = photo




def clickPrev():
    global num 
    num -= 1
    if num > 0:
        num = 8
        photo = PhotoImage(file = "gif/" + fnameList[num])
        pLabel.configure(image = photo)
        pLabel.image = photo

    



window = Tk()
window.geometry("700x500")

file_name = Label(window, text =  fnameList[num])
btnPrev = Button(window, text = "<<이전", command=clickPrev)
btnNext = Button(window, text = "<<다음", command=clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)


btnNext.place(x=250,y=10)
btnPrev.place(x=400, y =10)
pLabel.place(x=15,y=50)
file_name.place(x = 325, y = 10)


window.mainloop()
