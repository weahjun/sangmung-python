from tkinter import *

#전역 변수 선언
btlist = [None]*9
fnameList = ["C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif","C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\19-52-56-478_512.gif"]
photolist = [None]*9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0


#메인 코드 부분
window = Tk()
window.geometry("210x210")

for i in range(0,9):
    photolist[i] = PhotoImage(file ="gif/"+fnameList[i])
    btlist[i] = Button(window, image = photolist[i])


for i in range(0,3):
    for k in range(0,3):
        btlist[num].place(x=xPos,y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70



window.mainloop()
