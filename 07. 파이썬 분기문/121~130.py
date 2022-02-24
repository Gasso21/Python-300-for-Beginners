#121
x = input()
if x.islower():
    x = x.upper()
else:
    x = x.lower()
print(x)

#122
x = int(input("score: "))
print("grade is ", end="")
if 81<=x<=100:
    print("A")
elif 61<=x<=80:
    print("B")
elif 41<=x<=60:
    print("C")
elif 21<=x<=40:
    print("D")
elif 0<=x<=20:
    print("E")

#123
x = input("입력: ")
x = x.split(" ")
if x[1] == "달러":
    result = 1167 * int(x[0])
elif x[1] == "엔":
    result = 1.096 * int(x[0])
elif x[1] == "유로":
    result = 1268 * int(x[0])
elif x[1] == "위안":
    result = 171 * int(x[0])
print("%0.2d 원" %result)

#124

#125

#126

#127

#128

#129

#130