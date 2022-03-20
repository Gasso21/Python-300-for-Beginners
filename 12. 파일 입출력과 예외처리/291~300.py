#291
f = open("매수종목1.txt", 'wt')
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()

#292
#291
f = open("c:/Users/Jaehwan/Desktop/매수종목2.txt", 'wt')
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER")
f.close()

#293
import csv

f = open("C:/Users/Jaehwan/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()

#294
f = open("C:/Users/Jaehwan/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()   # python list

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)

f.close()

#295
f = open("C:/Users/Jaehwan/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v

print(data)
f.close()

#296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

#297
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)

#298
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")
#299
"""
try:
    실행코드
except 예외 as 변수:
    예외처리코드 
"""

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

#300
"""
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
-----
per = ["10.31", "", "8.00"]

for i in per:
    print(float(per))
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")