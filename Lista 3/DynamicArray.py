import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0  # liczba elementów
        self._capacity = 1  # rozmiar tablicy
        self._A = self._make_array(self._capacity)  # właściwa tablica

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c*ctypes.py_object)()

    def insert(self, k, value):
        if not 0 <= k <= self._n: #sprawdzam, czy k jest w moim przedziale indeksów
            raise IndexError

        if self._n == self._capacity:
            self._resize(2 * self._capacity) #mnoże dwa razy odrazu, bo dla n przesunięć mam wtedy O(1), a przy dokładaniu jednego dod miejsca za każdym razem miałabym O(n)
        for j in range(self._n, k, -1): #idę od końca, stąd krok = -1
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1
        return

def remove(self, value):
    for k in range(self._n):
        if self._A[k] == value:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j + 1]
            self._A[self._n - 1] = None #element ostatni powtórzony lub usuwana wartość
            self._n -= 1
            return
    raise ValueError

def expand(self, seq):
    for item in seq:
        self.append(item)

def __str__(self):
    elements = [str(self._A[k]) for k in range(self._n)]
    return '[' + ','.join(elements) + ']'



