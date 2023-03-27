#x = -4
#if x < 0:
#    x = -x

#a = float(input("a:"))
#b = float(input("b:"))

#if a < b:
#    a,b = b,a #меняем местами
#print(a,b)

#marks = [3,3,3,2,4]

#if 2 in marks:
#    print("fuck")
#else:
#    print("yeee")

'''x = int(input())

if x % 2 == 0:
    if 0 <= x <= 9:
        print("character")
    else:
        print("number")
else:
    print("not passed")'''


#max number among three numbers

'''a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b:
    if a > c:
        print("a is max")
    else:
        print("c is max")
else:
    if b > c:
        print("b is max")
    else:
        print("c is max")'''


#choose the option

'''item = int(input("item: "))

if item == 1:
    print("1 is chosen")
elif item == 2:
    print("2 is chosen")
elif item == 3:
    print("3 is chosen")
elif item == 4:
    print("4 is chosen")
else:
    print("not passed")'''


'''x = int(input())

if x < 0:
    print("x needs to be +")
elif 0 <= x <= 9:
    print("1 character")
elif 10 <= x <= 99:
    print("2 character")
elif 100 <= x <= 999:
    print("3 character")
else:
    print("more than 3 character")'''


'''
year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = list(map(int,input().split()))

m = s[0]
d = s[1]

if d == year[m]:
    print(f"01.{str(m+1).rjust(2,'0')} {str(d-1).rjust(2,'0')}.{str(m).rjust(2,'0')}")
elif d == 1:
    print(f"{str(d+1).rjust(2,'0')}.{str(m).rjust(2,'0')} {str(year[m]).rjust(2,'0')}.{str(m-1).rjust(2,'0')}")
else:
    print(f"{str(d + 1).rjust(2,'0')}.{str(m).rjust(2,'0')} {str(d-1).rjust(2,'0')}.{str(m).rjust(2,'0')}")

if d == year[m]:
    print(f"01.{m+1} {d-1}.{m}")
elif d == 1:
    print(f"{d+1}.{m} {year[m]}.{m-1}")
else:
    print(f" {d + 1}.{m} {d-1}.{m}")'''


'''a = 12
b = 7

res = a if a>b else b #if a > b -> res= a, else res=b; мы как бы присваеваем результат операции переменной
print(res)'''


'''
s = 'python'
a = 'upper'

res = s.upper() if a == 'upper' else s
print(res)'''


a = 5
b = 7
c = -4
#lst = [1,2, a if a < b else b, 4, 5]
#print("a - " + ("четное" if a % 2 == 0 else "нечетное") + " число")
#print(max(1, 2, a if a > b else b, 4, 5))

#find max of 3 numbers: used very rare in practice
'''d = (a if a > c else c) if a > b else (b if b > c else c)
print(d)'''
