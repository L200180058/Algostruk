##Modul 1
##Latihan
##
##LatReview1
a = 4
b = 5
c = a + b
print('Nilai a = ', a)
print('Nilai b = ', b)
print('Sekarang c = a + b = ', a, '+', b, '=', c)
print('')
print('Sudah Selesai')


##LatReview 2
print('Kita perlu bicara sebentar ...')
nm = input('Siapa namamu? (ketik disini)> ')
print('Selamat belajar, ', nm)
angkaStr = input('Masukkan sebuah angka antara 1 sampai 100> ')
a = int(angkaStr)
kuadratnya = a*a
print(nm + ', tahukah kamu bahwa', a, 'kuadrat adalah', kuadratnya, '?')


##LatReview 3
def ucapkanSalam():
    print("Assalamu'alaikum!")

def sapa(nama):
    ucapkanSalam()
    print('Halo, ', nama)
    print('Selamat belajar!')

def kuadratkan(b):
    h = b*b
    return h

##LatReview 4
from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    x1 = (-b + akar(D))/(2*a)
    x2 = (-b - akar(D))/(2*a)
    hasil = (x1, x2)
    return hasil


##LatReview 5
def apakahGenap(x):
    if (x%2 == 0):
        return True
    else :
        return False


##LatReview 6
def tigaAtauLima(x):
    if (x%3 == 0 and x%5 == 0):
        print('Bilangan itu adalah kelipatan 3 dan 5 sekaligus')
    elif x%3 == 0:
        print('Bilangan itu dalah kelipatan 3')
    elif x%5 == 0:
        print('Bilangan itu adlah kelipatan 5')
    else:
        print('Bilangan itu bukan kelipatan 3 maupun 5')
        

##LatReview 7
staff = {'Santi' : 'santi@ums.ac.id',\
         'Jokowi' : 'jokowi@solokab.go.id',\
         'Endang' : 'Endang@yahoo.com',\
         'Sualstri' : 'Sulastri3@gmail.com'}

yangDiCari = 'Santi'
if yangDiCari in staff :
    print('emailnya', yangDiCari, 'adalah', staff[yangDiCari])
else :
    print('Tidak ada yang namanya', yangDiCari)


##LatReview 8
for i in range(0,10):
    print(i)

##LatReview 9
for i in s:
    print(i)


##LatReview 10
dd = {'nama':'joko', 'umur':21, 'asal':'surakarta'}
for kunci in dd:
    print(kunci, '<---->', dd[kunci])


##LatReview 11
bil = 0
while(bil*bil<200):
    print(bil, bil*bil)
    bil = bil + 1

