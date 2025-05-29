from tkinter import *
from tkinter import messagebox


#함수 선언 부분
def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린키"+chr(event.keycode))


def keyEvent(event):
    key_name = ""
    
    if event.keysym == "Up":
        key_name = "↑"
    elif event.keysym == "Down":
        key_name = "↓"
    elif event.keysym == "Left":
        key_name = "←"
    elif event.keysym == "Right":
        key_name = "→"
    else:
        key_name = event.keysym  # 기본값 (예: 문자 키)

    messagebox.showinfo("키보드 이벤트", f"눌린 키: {key_name}")



#메인 코드 부분
window = Tk()

window.bind("<Shift-Up>",keyEvent)
window.bind("<Shift-Down>",keyEvent)
window.bind("<Shift-Left>",keyEvent)
window.bind("<Shift-Right>",keyEvent)



window.mainloop()
