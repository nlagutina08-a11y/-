#Занятие 2. Числа

#1 task 
a = float(input())
b = float(input())
c = float(input())
temp = a
a = c
c = b
b = temp
print(a, b, c)

#2 task 
a = float(input())
b = float(input())
c = float(input())
temp = a
a = b
b = c
c = temp
print(a, b, c)

#3 task 
x = float(input())
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print(y)

#4 task 
a = float(input())
a2 = a * a
a4 = a2 * a2
a8 = a4 * a4
print(a2, a4, a8)

#5 task 
a = float(input())
a2 = a * a
a3 = a2 * a
a5 = a3 * a2
a10 = a5 * a5
a15 = a10 * a5
print(a2, a3, a5, a10, a15)

#6 task 
alpha = float(input())
pi = 3.14
degrees = alpha * 180 / pi
print(degrees)

#7 task 
tf = float(input())
tc = (tf - 32) * 5 / 9
print(tc)

#8 task 
tc = float(input())
tf = tc * 9 / 5 + 32
print(tf)

#9 task 
x = float(input())
a = float(input())
y = float(input())
cena_1kg = a / x
stoimost_kg = cena_1kg * y
print(cena_1kg, stoimost_kg)

#10 task 
x = float(input())
a = float(input())
y = float(input())
b = float(input())
cena_shokolada = a / x
cena_irisa = b / y
raznica = cena_shokolada / cena_irisa
print(cena_shokolada, cena_irisa, raznica)

#11 task 
v = float(input())
u = float(input())
t1 = float(input())
t2 = float(input())
s1 = v * t1
s2 = (v - u) * t2
s = s1 + s2
print(s)

#12 task 
v1 = float(input())
v2 = float(input())
s = float(input())
t = float(input())
total_s = s + (v1 + v2) * t
print(total_s)

# Integer2
m = int(input())
tons = m // 1000
print(tons)

# Integer3
bytes_size = int(input())
kbytes = bytes_size // 1024
print(kbytes)

# Integer4
a = int(input())
b = int(input())
count = a // b
print(count)