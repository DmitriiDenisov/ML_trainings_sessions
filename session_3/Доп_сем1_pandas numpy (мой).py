import numpy as np
#numpy - основной объект массив, матричные операции - основное.
#в Юпитеире shift+tab - открыть подсказку
x = np.arange(10).reshape(2,5)
print x
print np.random.rand(2, 5)
print np.exp(np.eye(5))
#если нужны не поэлементные функции => linalg
print np.linalg.inv(np.eye(5)*10)
#там же можно вычислять определитнель, решать лин системы уравнений

###Индексация:
A = np.arange(15).reshape(5,3)
print A
A[[3,4]]#обращение к 3 и 4 строке
print A[:, [1,2]] #обращение к 1, 2 столбцу
print A[3:5, 1:3] #обращение к подматрице, второе число - не включает
A[:, 0]#первый столбец
print A[A[:, 0] % 2 == 1] #возвращаем только строки, у которых первый элемент нечетный

choise = np.arange(A.shape[1]) % 2 == 0#возвращаем массив четных чисел, до кол-ва столбцов А
A[:, choise] #выбираем только четные столбцы

b = np.arange(3)
b[:, np.newaxis] #сделали из вектора длины 3 матрицу 3x1 (или 1x3 - надо глянуть)
A * b#поэлементно умножили: первую строку на b[0], вторую b[1], третью на b[2]

a = np.random.randint(5, size = 3)#найдем все попарные произведения
b = np.random.randint(4, size = 2)
#a.reshape(1,5) #то же самое, что a[:, np.newaxis]
a[:, np.newaxis] @ b[np.newaxis, :] #матрицное умножение как в Линале: умножаем столбец 3x1 на строку 1x2
np.sum(A, axis = 0)#сумма
np.min(A, axis = 0)#минимум
np.cumsum(a) #возвращает вектор - на i-ом месте сумма до i-го элемента
np.cumsum(A, axis = 0)

#добавляем новый столбец
#tuple - котртеж из массивов
b = A[:, -1]#обращаемся к посл стобцу
b = A[:, -1][:, np.newaxis] # делаем из вектора 5 матрицу 5x1
#вместо newaxis() можно np.arange(5).reshape(5,1)
A[:, -1]#обращение к последнему столбцу
A[:, -2:]#обращение к предпоследнему и до конца
np.concatenate((A, b), axis = 1)
np.hstack((A, ))
#можно вставлять с помощью np.insert
np.insert(a, 2, np.arange(3), axis = 1)# можно так добавить в конец
np.delete()#удалять столбец
#---------------
#Задача 1: есть матрица X - матрица, y - вектор (машинка). Найти w - ?
def linregr(X, y)
#Задача 2:
#X - матрица, поделить каждую строку на сумму элементов в ней
def fun1(X):
    a = np.sum(X, axis = 1)
    X / a[:, np.newaxis]#сделали из вектора a -  матрицу, после разделили
    X / a.reshape(len(a), 1)#то же самое
    X / a.reshape(-1,1)#то же самое

a.reshape(-1, 2) # 2 - он делает два столбца, -1 => автоматически считает число строк

#запрогать Roc-Auc
#1 сортируем
a = np.random.rand(100)
y = np.random.randint(2, size = 100)
indx = np.argsort(a) #возвращаем индексы от мысленно отсортированного массива
a [indx] #отсорт массив
y [indx] #параллельно с a - отсортировали y

def revers_cumsum(x):
    c = x[::-1]#переворачиваем массив   начало:до куда:шаг
    b = np.cumsum(c)
    return b[::-1]#обратно разворачиваем


def roc_auc(y, a):
    l_plus = y.sum()
    l_minus = len(y) - y.sum()
    indexes = np.argsort(a)
    y_sorted = y[indexes]
    ones_right = reverse_cumsum(y_sorted)
    return np.sum(ones_right[y_sorted == 0]) / l_plus / l_minus

from sklearn.metrics import roc_auc_score
roc_auc_score(y, a)

import pandas as pd
#основной объект - датафрейм, одномерный - Series.
df = pd.DataFrame({"a":[1, 2, 3], "b": [1, 1, 1]}) #передаем словарь в создание датафрейма
df.describe()#статистику вычисляет
df = pd.read_csv("...csv", sep = ';')
head(7)
df[['age', 'sex']]#обращаемся к двум столбцам, чтобы не превратился в Series
df.loc[[2, 3, 4]]#выбираем строки
df['Name'] + df['Sex'] #можно сложить два столбца

