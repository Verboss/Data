import numpy as np
#sprawdzamy jaka mamy wersje
wersja=np.__version__ 
print(wersja)
#wyswietlamy funkcje
################print(dir(np))
#wywietlamy pomoc
################help(np.array)

#tworzymy tablice
x=np.array([1,3])
print(x)
print(type(x))

#ilo wymiarowa
print(x.ndim)

#rozmiary tablicy
print(x.shape)

#ile jest liczb w tablicy
print(x.size)

#typ danych - liczba całkowita 32-bitowa
print(x.dtype)

#tworzymy tablice zmienno przecinkową
y=np.array([1.3,2.3,1.4])
print(y)
#zmiennoprzecinkowa 64-bitowa
print(y.dtype)

#tworzymy tablice dwuwymiarową
z=np.array([[1,2], [-3,1]])
print(z)
print(z.ndim)
print(z.shape)

#inna tablica dwuwymiarowa
q=np.array([[1,2,4],[4,2,1]])
print(q)
print(q.shape)

a=np.array([[[4,3,1],
             [3,1,2]],
            
            [[4,1,3],
             [4,2,1]],
            
            [[2,4,1],
             [5,8,1]]])

print(a)
print(a.shape)
print(a.ndim)


#                       TYP DANYCH
print('TYP DANYCH')
print(end='\n')

#dane całkowite
a=np.array([1,2,3])
print(a.dtype)

#dane zmiennoprzeinkowe
a=np.array([1.1,2.2,3.3])
print(a.dtype)

#ustawiamy typ zmiennych
a=np.array([1,2,3], dtype='float')
print(a.dtype)
a=np.array([1,2,3], dtype='complex')
print(a.dtype)
a=np.array([1,2,3], dtype='int')
print(a.dtype)
a=np.array([True, False]) #bool
print(a.dtype)
a=np.array([24,120,230], dtype=np.int8)
print(a.dtype)

#                   TWORZENIE TABLIC
print('TWORZENIE TABLIC')
print(end='\n')

#tworzenie tablicy z samymi zerami - 4 wiersze, 10 kolumn
a=np.zeros(shape=(4,10))
print(a)
a=np.zeros(shape=(4,10), dtype='int') # intem

#tworzenie tablicy z samymi jedynkami - 5 wierszy, 5 kolumn
a=np.ones(shape=(5,5))
print(a)

#wypelniamy tablice konkretną wartocią 4 - 3 wiersze, 3 kolumny
a=np.full(shape=(3,3), fill_value=4, dtype='int')
print(a)

#wygenerowanie liczb od 0 włączenie do 9
a=np.arange(10)
print(a)

#wyznaczamy od jakiej liczby zaczynami i na jakiej kończymy (tej nie ma w tablicy)
a=np.arange(start=5, stop=10)
print(a)

#dodajemy krok
a=np.arange(start=10, stop=100, step=10)

#od wiekszej do mniejszej
a=np.arange(start=100, stop=10, step=-10)
print(a)

#nastepny przyklad
a=np.arange(start=0, stop=5, step=0.5)
print(a)

#dostajemy 11 elementów równo rozłożonych po przedziale od 0 do 1
a=np.linspace(start=0, stop=1, num=11)
print(a)

#zmieniamy rozmiar tablicy z jednowymiarowej na dwu - 3 wiersze, 5 kolumn
a=np.arange(15)
b=a.reshape((3,5))
print(b)

#python sam dostosuje długosc kolumny dajac parametr -1
c=a.reshape((3,-1))
print(c)

#analogicznie dla wiersza
c=a.reshape((-1,3))
print(c)

#                       PODSTAWOWE OPERACJE NA TABLICACH
print('PODSTAWOWE OPERACJE NA TABLICACH')
print(end='\n')

#tworzymy 2 tablice
a=np.array([3,1,4,2])
b=np.array([3,-1,3,2])
print(a)
print(b)

#dodajemy macierze po elementach
c=a+b
print(c)

#odejmujemy
c=a-b
print(c)

#mnozymy
c=a*b
print(c)

#dzielimy, nie możemy dzielić przez 0!
c=a/b
print(c)

#dodajemy 3 do każdego elementu
c=a+3
print(c)

#mnożymy każdy element razy 2
c=a*2
print(c)

#inne
c=a+3*b
print(c)

#teraz bedziemy uzywac dedykowane funkcje z biblioteki NumPy
#dodawanie
c=np.add(a,b)
print(c)

#odejmowanie
c=np.subtract(a,b)
print(c)

#mnozenie
c=np.multiply(a,b)
print(c)

#dzielenie
c=np.divide(a,b)
print(c)

x=np.array([[1,3],[-2,0]])
y=np.array([[6,0],[-1,2]])
print(x,'\n')
print(y)

#mnożenie macierzy czyli macierz razy macierz, a nie po elementach
z=np.dot(x,y)
print(z)

#mozna tez zapisac
z=x.dot(y)
print(z)

#mozna tez zapisac
z=x @ y

#                   GENEROWANIE LICZB PSEUDOLOSOWYCH
print('GENEROWANIE LICZB PSEUDOLOSOWYCH')
print(end='\n')

#ustawiamy ziarno, żeby za każdym odpaleniem programu dostawać ten sam wynik
np.random.seed(0)
#losujemy liczbe pseudolosową z rozkładu normalnego
a=np.random.randn()
print(a)

#losujemy dziesięć liczb roz. norm. (o sredniej 0 i odchyleniu standardowym 1)
a=np.random.randn(10)
print(a)

#losujemy tablice
a=np.random.randn(10,4)
print(a)

#rozkład jednostajny na przedziale, działa tak samo jak rozklad normalny
a=np.random.rand()
print(a)

#losuje nam liczby od 0 do 10
a=np.random.randint(10)
print(a)

#losujemy liczbe z przedziału 10 do 100
a=np.random.randint(low=10, high=101)
print(a)

#losuje nam 1 liczb z przedziału 10 do 100
a=np.random.randint(low=10, high=101, size=10)
print(a)

#wybiera nam liczbe z tablicy
a=np.random.choice([4,2,1,3,5])
print(a)

#losowo od tekstu

a=np.random.choice(['python','java','sql'])
print(a)

#tworzymy tablice
a=np.arange(10)
print(a)

#tasujemy losowo dane
np.random.shuffle(a)
print(a)

#                           PODSTAWOWE FUNKCJE
print('PODSTAWOWE FUNKCJE')
print(end='\n')

#funkcja exp
a=np.exp(1)
print(a)

#pierwiastek
a=np.sqrt(3)
print(a)

#jesli mamy 0 w tablicy to zwroci nam False
a=np.all([2,1,3])
print(a)
a=np.all([2,0,3])
print(a)

#sprawdza czy jaka liczba jest prawdą (czyli różna od 0)
a=np.any([1,0,2])
print(a)
a=np.any([0,0,0])
print(a)

#generujemy tablice
a=np.random.rand(5)
print(a)

#szukamy najwiekszej (zrwaca numer komorki)
b=np.argmax(a)
print(b)

#wartosc najwiekszej
c=a[np.argmax(a)]
print(c)

#analogicznie dla najmniejszej
b=np.argmin(a)
print(b)

#wartosc najmniejszej
c=a[np.argmin(a)]
print(c)

#sortowanie roznąco, zwraca nam numer indexu
c=np.argsort(a)
print(c)

#zwracamy najwieksza wartosc
c=np.max(a)
print(c)

#najmniejsza
c=np.min(a)
print(c)

#srednia
c=np.mean(a)
print(c)

#mediana
c=np.median(a)
print(c)

#odchylenie standardowe
c=np.std(a)
print(c)

#                   INDEKSOWANIE I WYCINANIE TABLIC
print('INDEKSOWANIE I WYCINANIE TABLIC')
print('\n')

#tworzymy tablice
a=np.arange(20)
print(a)

"""a[idx], a[start:stop], a[:stop], a[start:]"""

b=a[2]
print(b)
b=a[2:]
print(b)
b=a[:2]
print(b)
b=a[[0,2]]
print(b)
b=a[-1]
print(b)
b=a[10:15]
print(b)

#tworzymy z tablicy jednowymiarowej dwuwymiarową
a=a.reshape(4,5)
print(a)

#mamy pierwszy wiersz
b=a[0]
print(b)

#kolumna - dajemy dwukropek, przecinek i potem piszemy ktora kolumna nas interesuje
b=a[:,0]
print(b)

#chcemy konkretna komorke
b=a[1,1]
print(b)

#chcemy wyciąć tragment
#pamietać że 3 wierz i 4 kolumna nam nie wchodzi w to!
b=a[1:3,1:4]
print(b)

#podmiana liczby
a[1,2]=14
print(a)

#                       ITERACJA PO TABLICACH
print('ITERACJA PO TABLICACH')
print('\n')

#iteracje po wierszu
for row in a:
    print(row)

#iteracja po kolumnie 3
for row in a:
    print(row[:3])

#iteracje po każdym elemencie
for item in a.flat:
    print(item)

#                       ZMIANA ROZMIARU TABLIC
print('ZMIANA ROZMIARU TABLIC')
print('\n')

#wyswietlamy wymiar tablicy
print(a.shape)

print(a.reshape(5,4))

#odwrotna operacja dp reshape (zwraca tablica do postaci jednowymiarowej)
print(a.ravel())

#transponowanie
print(a.T)

#                       MASKI LOGICZNE
print('MASKI LOGICZNE')
print('\n')

#ustawiamy tablice 
a=np.arange(start=-10, stop=10, step=0.5)
print(a)
a=a.reshape(10,-1)
print(a)

#maska logiczna - jesli wieksze od 0 to True
print(a>0)

#możemy wyciąc wartosci False i wyswietlic tablice tylko z wartosciami komórek z True
b=a[a>0]
print(b)

#modyfikacja
b=np.bitwise_and(a>-5,a<5)
print(b)
b=a[np.bitwise_and(a>-5,a<5)]
print(b)

#alternatywa
b=np.bitwise_or(a<-5,a>5)
print(b)