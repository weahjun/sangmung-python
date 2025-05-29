inFp = None
inStr = ""

inFp = open("C:\\Users\\weahj\\OneDrive\\바탕 화면\\과제제출용\\안녕하세여.txt","r",encoding='UTF8')


line = 0
line += 1


while True:
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(line,inStr,end="")
    line += 1




inFp.close()
