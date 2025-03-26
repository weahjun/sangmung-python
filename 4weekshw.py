a = int(input("1. 입력한 수식 계산   2. 두 수 사이의 합계 :"))
if a == 1:
    s = input("수식을 입력하세요:")
    r = eval(s)
    print("결과는 ",r, "입니다")
     
elif a == 2:
    n1 = int(input("***첫번째 수를 입력하세요:"))
    n2 = int(input("***두번째 수를 입력하세요:"))
    print(n1,"+...+",n2,"까지의 합은",(n1+n2)*(n2-n1+1)/2,"입니다")
else :
    print("다시 입력해주세요")
