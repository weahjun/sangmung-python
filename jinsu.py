a = int(input("입력 진수 결정(16/10/8/2):"))
v = input("값 입력:")
j = int(v,a)
print("16진수==>", hex(j))
print("10진수==>", j)
print("8진수==>", oct(j))
print("2진수==>", bin(j))
