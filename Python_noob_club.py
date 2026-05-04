# Степик: 1.5 (Операции с целыми числами)
# // - деление целочисленное (остаток не покажет)
# % - остаток от деления
# ** - возведение в степень print(2014**14)

# Степик 1.6 (Операции с вещественными числами/плавающая точка)
# / - деление вещественное (числа после запятой тоже покажут)

# Степик 1.7 (Типы данных)
import os

print (int(2.99))
print (int(-1.6))
print(9**19 - int(float(9**19)))
# type() - определиние типа данных

# Степик 1.8 (Переменные. Ввод/Вывод)

name = input('Enter your name: ') #переменная name где инпут - ввод пользователя
print('Hello,', name)

number = int(input('Your age: '))
print('your age x2 = ',2 * number)
#Задание 2
x = int(input())
print(x//60)
print(x%60)
#Задание 3
x = int(input('минуты ')) #480/475
h = int(input())  #во сколько часов ляжет 1/1
m = int(input())  #во сколько минут ляжет 2/55
print((h*60 + x + m) // 60)
print((m+x) % 60)

# Степик 1.9 Логические операции

# true/false 1/0
# or/and/not - (нот имеет приоритет, потом энд и уже потом или)
# </>/<=/>=/!=/==
#Задание 1 расставить скобики a and b or not a and not b
((a and b) or ((not a) and (not b)))
#Задание 2 разобраться почему получился такой ответ:
x = 5
y = 10
y > x * x or y >= 2 * x and x < y
10 > 5 * 5 or 10 >= 2 * 5 and 5 < 10
#True or True and False = True
#Задание 3
a = True
b = False
a and b or not a and not b

True and False or not True and not False

#True and False = False
#not True = False
#not False = True

Ответ:False

# Степик 1.10 (Условия if/else/ilif)

a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    print('Деление невозможно')
    b = int(input('Введите не нулевое значение: '))
    if b == 0:
        print('Вы не справились')
    print(a/b)

#Задание 1
a = int(input('переменная А'))  #6/7/7 - это нормально
b = int(input('переменная B')) #10/9/9 - переспала
h = int(input('переменная H')) #8/10/2 - спала
if h > b:
    print('Пересып')
elif h < a <= b:
    print('Недосып')
else:
    print('Это нормально')

#Задание 2
a = int(input('Укажите год в период с 1900 до 3000 включительно: '))

if a % 4 == 0 and a % 100 != 0:
    print('Високосный')
elif a % 400 == 0:
    print('Високосный')
else:
    print('Обычный')

# Степик 1.11 (Строки)

#'abc' + 'def'  =  'abcdef'- конкатинация строк
# 'abc' * 3 = 'abcabcabc' - умножение строки
# len('abc') = 3 - длина
# 'abd' == '''abc''' = true/ 'abc' < 'ab' = поочередная проверка символов по порядку /'abc' > 'ab' = подсчет кол-ва символов по порядку
# '\n' - перевод строки (ентеры)


#Задание 1
print("239" < "30" and 239 < 30)
print("239" < "30" and 239 > 30)
print("239" > "30" and 239 < 30)
print("239" > "30" and 239 > 30)
#Задание 2
'12342'

# Степик 1.12 (Задачи по завершенному блоку)
#Задача 1
a = int(input('число a'))
b = int(input('число b'))
c = int(input('число c'))
p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
print(s)
#Задача 2
x = int(input('Число: '))
if -15 < x <= 12 or 14< x <17 or x >= 19:
    print(True)
else:
    print(False)
#Задача 3
a = float(input('Число первое: '))
b = float(input('Число второе: '))
c = input('Операция:')
#5.0 #0.0 #mod      Деление на 0!
#-12.0 #-8.0 #*     96
#5.0 #10.0 #/       0.5
if (c == 'div' or c == 'mod' or c == '/') and b == 0:
    print('Деление на 0!')
elif c == 'pow':
    print(a**b)
elif c == 'div':
    print(a//b)
elif c == 'mod':
    print(a % b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)

#Задача 4
z = input('Укажите фигуру: ')
if z == 'прямоугольник':
    a = int(input('Сторона А'))
    b = int(input('Сторона Б'))
    print(a * b)
elif z == 'треугольник':
    a = int(input('Сторона А'))
    b = int(input('Сторона Б'))
    c = int(input('Сторона Ц'))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif z == 'круг':
    r = int(input('Окружность'))
    pi = 3.14
    print(pi * r ** 2)
#Задача 5
a = int(input())
b = int(input())
c = int(input())
if (a, b, c):
    print(max(a,b,c))
    print(min(a,b,c))
    print((a + b + c) - (min(a,b,c) + max(a,b,c)))
#Задача 6
a = int(input('Введите кол-во человек в команте: '))
if a % 5 == 0 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9 or a == 11 or a == 12 or a == 13 or a == 14 or a % 100 == 11 or a % 100 ==12 or a % 100 ==13 or a % 100 ==14:
    print(a, 'программистов')
elif a % 10 == 1:
    print(a, 'программист')
else:
    print(a, 'программиста')
#Задача 7
z = int(input('Ввод цифр: '))
x = z // 1000 # число 123
d = x // 100 # число 1
a = x % 10 #  число 3
b = x // 10 # число 12
c = b % 10 # число 2
y = z % 1000 # 456
t = y //100 # число 4
e = z % 10 # число 6
w = z % 100 # число 56
r = w // 10 # число 5
if a + c + d == t + r + e:
    print('счастливый')
else:
    print('обычный')

# Степик 2.1 (Цикл while)
a = 5
while a > 0:
    print(a, '')
    a-=1
#Вывести все нечетные числа от 5 - 55
a = 5
while a <= 55:
    print(a)
    a += 2

a = 5
while a <= 55:
    if a % 2 == 1:
        print(a)
        a += 1

n = int(input('Напишите кол-во строк: '))
start = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'

#Задача 1
number = int(input('Число первое '))
s = 0
i = number
while i != 0:
    s += i
    i = int(input('Следующее число: '))
if i ==0:
    print(s)
#Задача 2
a = int(input('Биологи'))
b = int(input('Информатики'))
pices = 1
while pices % a != 0 or pices % b != 0:
    pices += 1
else:
    print(pices)

# Степик 2.2 (Операторы break/continue)
#break - оператор завершения цикла
#continue - оператор перехода к следующей итерации цикла(если она есть)

#Задача 1
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
# какое зачение будет иметь i, после завершения цикла( то есть сработает break) i = 7

#Задача 2
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
# определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы i = 10
# обратить внимане, когда срабатывает continue, i = i + 1 не работает и цикл начинается сверху

#Задача 3
while True:
    p = int(input('Вводим числа: '))
    if p < 10:
        continue
    elif 10 <= p <= 100:
        print(p)
    else:
        break
#12 4 2 58 112/// 12 58
#101 - пусто
#1 2 102 - пусто

# Степик 2.3 (Цикл for)

for i in 1,2,3:
    print(i * i) # 1/ 4/ 9
for i in range(10):
    print(i * i) # 0/ 1/ 4/ 9/ 16 и тд
# range(5):0, 1, 2, 3 ,4 (не включая 5)
# range(2, 5): 2, 3 ,4 (не включая 5) с шагом 1
# range(2, 15, 4): 2, 6, 10, 14 - все чсла от 2 до 15 (не включая 15) с шагом 4
# range(5+1): 0, 1, 2, 3, 4,5 (включая 5 так как +1)
# range(start=0, to, step=1) start  - по умолчанию 0, шаг по умполчанию - 1, to - обязательная
# Вывести квадрат из звездочек
n = int(input())
for i in range(n):
    print('*' * n)
# Вывести квадрат из звездочек с вложенным циклом
#n = int(input())
for i in range(n): #Количество строк
    for j in range(n): #Количество символов в строке
        print('*', end='')
    print()

#Задача 1
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1):
    print('\t',i, end='')
print()
for j in range(a, b + 1):
    print(j, end='')
    for g in range(c, d +1 ):
        print('\t', j * g, end='')
    print()

#Вывксти сумму всех нечетных числе от А - Б включая обе границы
#На вход изет цифра 3 и 7 , результат 15 ( 3+ 5 + 7)
#Решение 1
a,b = input('Введите 2 числа: ').split()
a = int(a)
b = int(b)
s = 0 #переменная для накопления чисел
for i in range(a, b+1):
    if i % 2 ==1:
        s += i
print(s)
#решение 2
a,b = input('Введите 2 числа: ').split()
a = int(a)
b = int(b)
s = 0 #переменная для накопления чисел
if a % 2 == 0:
    a += 1
for i in range(a, b+1, 2):
    s += i
print(s)
#Решение 3
a, b = (int(i) for i in input().split()) #
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)

#Задача 2
a = int(input('Первое число: '))
b = int(input('Второе число: '))
len = 0
sum = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum = sum + i
        len = len + 1
print(sum/len)

# Степик 2.4 (Строки и символы)
#genome = 'ATGG'
#genome[0] A genome[-1] G
#genome[1] T genome[-2] G
#genome[2] G genome[-3] T
#genome[3] G genome[-4] A
#i = 1, print(genome[1]) = T
genome = 'ATGG'
for i in genome:
    print(i)
#Найти кол-во С в строке
genome = input()
pint(genome.count('C'))

#s = 'aTGcc'  p = 'cc'
#s.upper() - все буквы делает большими
#s.lower() - все буквы делает маленькими
#s.count(p) - кол-во пар сс
#s.find(p) - ищет вхождение по индексу
#s.find('A') - -1, так как нет подходящих букв в строке
#s.replace('c','C') - aTGCC, заменить маленькие на большие
s = 'agTtcAGtc'
s.upper().count('gt'.upper()) #результат 2

#Задача 1
programm = input()
programmUp = programm.upper()
upG = programmUp.count('G')
upC = programmUp.count('C')
lengs = len(programmUp)
print(((upG + upC) / lengs) * 100)

#Slaicing
dna = 'ATTCGGAGCT'
dna[1] = 'T'
dna[1:4] = 'TTC' #4 индекс не влючительно
dna[:4] = 'ATTC' #Считается с 0 до 4 индекса не включительно
dna[4:] = 'GGAGCT' #Начиная с 4 индекса и до конца строки
dna[-4:] = 'AGCT' #Считается индекс с конца и потом опять слева на право
dna[1:-1] = 'TTCGGAGC' # с индекса один до конца индекса -1 не включительно
dna[1:-1:2] = 'TCGG' #индекса начала и индекс конца с шагом 2
dna[::-1] = 'ATTCGGAGCT'  #символы в обратном порядке с отрицательным шагом
# a = 'CAGGTGGAC'   b = 'GATTACA'
# Нужно выяснить является ли значение полиндромом
s = input()
i = 0
j = len(s-1)
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
    i += 1
    j -= 1
    if is_palindrome:
        print('YES')
    else:
        print('NO')

#Короткое решение поиска полиндрома
s =input()
r = s [::-1]
if s == r:
    print('YES')
else:
    print('NO')

#Задание 2
s = 'abcdefghijk'
s[3:6] = 'def'
s[:6] = 'abcdef'
s[3:] = 'defghijk'
s[::-1] = 'kjihgfedcba'
s[-3:] = 'ijk'
s[:-6] = 'abcde'
s[-1:-10:-2] = 'kigec'

#Задача 3
s = input('Введите буквы: ')
count = 1
n = len(s)
for i in range(n-1):
    if s[i] == s[i+1]:
        count += 1
    elif s[i] != s[i+1]:
        print(s[i] + str(count), end='')
        count = 1
print(s[-1] +str(count),end='' )

# Степик 2.5 (Список list)

students=['Ivan', 'Masha', 'Sasha']
for student in students:
    print('hello,' + student + '!' )
students[0] = Ivan
students[1] = Masha
students[2] = Sasha

#Доступ к элементам списка
students = ['ivan', 'Masha', 'Sasha']
len(student) #Длина списка
students[0] = Ivan, students[-1] = Sasha
students[1] = Masha, students[-2] = Masha
students[2] = Sasha, students[-3] = Ivan
students[:2] = 0,1 ,Ivan, Masha
students[::-1] #все элементы списка с конца в начало
#Операции со списком сложением и умножение
students1['Ivan']
techers1['Sergey']
students1 + teachers1 ['Ivan', 'Srgey']

[0, 1] * 4
[0, 1, 0, 1, 0, 1, 0, 1]

#Изменение значений элементов списка
students=['Ivan', 'Masha', 'Sasha']
students[1] = 'Oleg'
print(students) #['Ivan', 'Oleg', 'Sasha']

#Добавление элементов в список
students=['Ivan', 'Masha', 'Sasha']
students.append('Olga') #Элемент будет добавлен в конце списка
students+=['Olga'] #Добавит еще одну 'Olga' в список
students+=['Boris', 'Srgey'] #Добавлены оба элмента в конец
students = [] #Создание пустого списка
students.insert[1, 'Olga'] #Позиция в которую встовляем элемент и что вставляем

#Задача 1
#сколько элементов будет содержать список  students
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
#Ответ 8, последнее имя добавить каждую букву под своим индексом в конец

#Удаление элемента из списка
students = ['Ivan', 'Masha', 'Sasha']
students.remove('Sasha') #Удалит значение из списка первое с таким имененем
del students[0]  #Удалить именно тот индекс элемента в списке

#Поиск элементов в списке
students = ['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students: #Элемент в списке
    print('Ivan is here')
if 'Ann' not in students: #Элемент не в списке
    print('Ann is out')

ind=students.index('Sasha') #Поиска индекса в списке, если эл несколько, то первую позицию
ind=students.index('Ann') #Если нет в списке, получим ошибку

#Сортировка списка
students = ['Sasha', 'Ivan', 'Masha']
order_students=sorted(students) #результат ['Ivan', 'Masha', 'Sasha']
students.sort()  #min/max  #нужно что бы все элементы списка были сравнимы
students.reverse() #Список в обратном порядке  тоже самое students [::-1]

#Присвоение списков
a = [1, 'A', 2]
b = a
a[0] = [42]
значение
a: [42, 'А', 2]
b: [[42, 'А', 2]]
b[2]= [30]
значение
a = [42, 'А', 30]
b = [42, 'А', 30]

#Задание 2
a = [1, 2, 3]
b = a
# значения списка b?

a[1] = 10
# значения списка b?

b[0] = 20
# значения списка a?

a = [5, 6]
# значения списка b?

# 1 2 3; 1 10 3; 20 10 3; 20 10 3

#Генерация списоков
a = [0] * 5 #[0 0 0 0 0]
a = [0 for i in range(5)] # [0 0 0 0 0]
a = [i * i for i in range(5)] #квадрат каждого числа списка 0 = 0 1 = 2 2 = 4 3 =9 4 = 16
a = [int(i) for i in input().split()] #разделит строку по пробелам и дальше к каждой части применяем преобразование str в int

#Задача 3
a = input().split()
num = [int(i) for i in a]
plus = sum(num)
print(plus)

#Задача 4
a = [int(i) for i in input().split()]
n = len(a)
if len(a) == 1:
    print(a[0], end='')
else:
    for j in range(n - 1):
        print(a[j+1] + a[j-1], end=" ")
    print(a[-2] + a[0])

#Задача 5
a = [int(i) for i in input().split()]
count = 1
a.sort()
z = len(a)
for j in range(z - 1):
    if a[j] == a[j + 1]:
        if j == 0 or a[j] != a[j - 1]:
            print(a[j], end=' ')


#Генерация двумерных списков
a = [[1, 2 ,3 ], [4, 5 ,6], [7, 8 ,9]]
a[1] # =[4, 5, 6]
a[1][1]  # =5


n=3
a=[[0]*n] * n #Зависимый список
a[0][0] = 5
a   # 5 0 0
    # 5 0 0
    # 5 0 0
a = [[0]* n for i in range(n)] # Независимые списки
a = [[0 for j in range(n)] for i in range(n)] #Независимые списки

# Степик 2.6 (Поиск минимума в списке)
#5 8 4 3 5 7  =  min(m) = 3 или решение снизу
a = [int(i) for i in input().split()] #4 7 3 8
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)

#Сапер
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, kol = (int(i) - 1 for i in input().split())
    a[row][kol] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end ='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()

#Задача 1
s = res = 0
while True:
    n = int(input())
    s += n
    res += n ** 2
    if s == 0:
        break
print(res)

#Задача 2
a = int(input())
numbers = [[a] * a for a in range(1, a + 1)]
print(numbers)
flat_list = sum(numbers, [])
print(*flat_list[:a])

#Задача 3
a = [int(i) for i in input('Список чисел: ').split()]
b = int(input('Число два: '))
found = False
for i in range(len(a)):
    if b == a[i]:
        print(i, end=' ')
        found = True
if not found:
    print('Отсутствует')

#Задача 4
matrix = []
while True:
    line = input()
    if line == 'end':
        break
    matrix.append([int(x) for x in line.split()])
def sum_neighbors(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbor_sum = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = (i + di + rows) % rows
                nj = (j + dj + cols) % cols
                neighbor_sum += matrix[ni][nj]
            new_matrix[i][j] = neighbor_sum
    return new_matrix
result = sum_neighbors(matrix)
for row in result:
    print(*row)

#Задача 5
n = int(input())
matrix = [[0] * n for i in range(n)]
num = 1
top, bottom = 0, n - 1
left, right = 0, n - 1
while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    if top <= bottom:
        for i in range(right, left - 1, - 1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, - 1):
            matrix[i][left] = num
            num += 1
        left += 1
for row in matrix:
    print(*row)

# Степик 3.1 (Функции)
def min2(a, b):    #функция def потом название произвольное
    if a<=b:       # min(min(25,42),30)
        return a
    else:
        return
#Задание 1
def f(n):
    return n * 10 + 5
#Введите её в интерпретаторе и посчитайте, чему равно значение следующего выражения:
print(f(f(f(10)))) #10555

#Различные функции
#Без возвращения значения
#Без параметров
#Произвольное число параметров
def min(*a):
    m=a[0]
    for x in a:
        if m>x:
            m=x
    return m
#Параметры со значением поумолчанию
def my_range(start, stop, step=1):
    res=[]
    if step > 0:
        x=start
        while x< stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x> stop:
            res +=[x]
            x+= step
    return res
#Локальные переменные
def init_values():
    a = 100
    b = 100
init_values()
print(a + b)  #Вызовет ошибку а и b не объявлены
#Изменение локальных переменных
def init_values():
    a = 100
a = 0
init_values()
print(a) #ответ 0

def init_values(a):
    a = 100
b = 0
init_values(b)
print(b) #ответ 0

#Изменение объектов, связанных с локальными переменными
def appen_zero(xs):
    xs.append(0)
a=[]
appen_zer(a)
print(a) #ответ [0]

#Глобальные переменные
def print_value():
    print(a)
a=5
print_value() # ответ 5

def print_value():
    print(a)
    a = 10
    print(a)
a=5
print_value() # ответ будет ошибка

#Задача 2
def f(x):
    if x <= - 2:
        return 1 - (x+2) ** 2
    if -2 < x <= 2:
        return - x / 2
    if 2 < x:
        return (x - 2) ** 2 + 1

#Задача 3
def modify_list(l):
    new_list = []
    for x in l:
        if x % 2 == 0:
            new_list.append(x // 2)
    l[:] = new_list

# Степик 3.2 (Словари)
#Множества
s=set()
basket={'apple', 'orange', 'apple', 'pear', 'apple'}
print(basket) #распечатает тольео 1 элемент из множества
'orange' in basket #True
'python' in basket #False
#Операции с множеством
s.add(element)
s.remove(element)
s.discard(element)
s.clear(element)
#перебор элементов множества
basket={'apple', 'orange', 'apple', 'pear', 'apple'}
for x in basket:
    print(x)
# banana apple orange pear вывелось 1 значение из списка и не по порядку

#Словари
dict, {} #Создаие словаря
d = {'a': 239,10 : 100} #Словарь с 2 парами
print(d['a'])
print(d[10])
#Операции со словарями
dictionary = {...}
key in dictionary #Есть ли ключ в словаре True/False
key not in dictionary
dictionary[key] = value #Добавить ключ-значение в словарь
dictionary[key] #Если ключа нет, ошибка
dictionary.get(key) #Можем использовать тут, что бы не было ошибки
del dictionary[key] #Удалить элменты из словаря ключ-значение

#Перебор элементов словаря
d ={'c':14, 'A':12, 'T':9, 'G':18}
for key in d:
    print(key, end='') #получим все ключи словаря
for key in d.keys():
    print(key, end='') #получим все ключи словаря
for value in d.values():
    print(value, end='') #получим все элементы, 2 значение в паре
for key, value in d.items():
    peint(key,value, end=';') #получим пары элементов и разделим через точка запятая

#Задача 1
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif (2 * key) in d:
        d[key*2].append(value)
    else:
        d[key*2] = [value]

#Задача 2
from collections import Counter
a = input('Введите буквы: ').lower().split()
counter = Counter(a)
for word, count in counter.items():
    print(f"{word} {count}")

#Задача 3
my_dict = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x in my_dict:
        print(my_dict[x])
    else:
        result = f(x)
        my_dict[x] = result
        print(result)

# Степик 3.3 Интерпритатор (установка/Запуск)
# создаем текстовый файл расширения .py, через терминал в идее заходим в папку где лежит файл, и набираем
# python название файла ентер

# Степик 3.4 (Файловый ввод/вывод)
inf = open('text.file', 'r') #Открывает файл ключ r - открываем файл на прочтение
s1 = inf.readline() # чтение построчно
s2 = inf.readline()
inf.close() # Завершает чтение

with open('text.file') as inf: #Запуск чтения файла и автоматическое зарытие
    s1 = inf.readline()
    s2 = inf.readline()

s = inf.readline().strip() #Убирает служебные символы при чтении файла
'\t abc \n'.strip()   # 'abc'

os.path.join('.', 'dirname', 'filename.txt') #полный путь к файлу
'./dirname/filename.txt'

#Построчное чтение файлов
with open('input.text') as inf:
    for line in inf:
        line = line.strip()
        print(line)

#Запись в файл
ouf =open('file.text', 'w')  #ключ w - запись
ouf.write('some text \n')
ouf.write(str(25))
ouf.close()

with open('some.text', 'w') as ouf: #автоматически закроет после записи
    ouf.write('some text \n' )
    ouf.write(str(25))

#Задание 1
#Скачиваем файл ( каждый раз генерится с новыми данными)
#Пишем код что бы считать строку из файла
with open('/Users/c0ldeyes/IdeaProjects/Python_noob_project/dataset_3363_2-2.txt', 'r', encoding='utf-8') as inf:
    line = inf.readline()
    print(f"Считанная строка: {line.strip()}")
#Дальце циклом разбираем строку из файла обратно A2D3 = AADDD в таком виде
#Создаем файл руками или можно написать программу, которая создать файл с этими данными
#После генерации файла у вас есть 5 минут что бы загрузить новый файл для ответа в Степик

#Задача 2
def main():
    # Укажите имя вашего файла
    filename = "input.txt"

    try:
        with open('название_файла.txt', "r", encoding="utf-8") as f:
            # read() считывает весь файл, split() разбивает его на слова
            # по любым пробельным символам (пробел, \n, \t и т.д.)
            words = f.read().split()
    except FileNotFoundError:
        print(f"Ошибка: файл '{'название_файла'}' не найден.")
        return

    if not words:
        print("Файл пуст или не содержит слов.")
        return

    # Подсчёт частоты каждого слова
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Поиск слова с максимальной частотой
    best_word = None
    max_count = 0

    for word, count in counts.items():
        # Обновляем ответ, если нашли большую частоту
        # или такую же частоту, но слово лексикографически меньше
        if count > max_count or (count == max_count and word < best_word):
            max_count = count
            best_word = word

    print(f"{best_word} {max_count}")

if __name__ == "__main__":
    main()

#Задание 3
# Имена файлов
input_file = 'dataset_3363_4.txt'
output_file = 'answer.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, \
        open(output_file, 'w', encoding='utf-8') as f_out:

    sum_math = 0
    sum_phys = 0
    sum_rus = 0
    count = 0

    for line in f_in:
        line = line.strip()
        if not line:
            continue

        # Разделяем строку по точке с запятой
        parts = line.split(';')
        # parts[0] - фамилия, parts[1] - математика, parts[2] - физика, parts[3] - русский
        m = int(parts[1])
        p = int(parts[2])
        r = int(parts[3])

        # Средний балл абитуриента
        avg_student = (m + p + r) / 3
        f_out.write(f"{avg_student}\n")

        # Накопление сумм для общих средних
        sum_math += m
        sum_phys += p
        sum_rus += r
        count += 1

    # Итоговые средние баллы по предметам
    if count > 0:
        avg_math = sum_math / count
        avg_phys = sum_phys / count
        avg_rus = sum_rus / count
        f_out.write(f"{avg_math} {avg_phys} {avg_rus}")


# Степик 3.5 (Модули, подключение подулей)
