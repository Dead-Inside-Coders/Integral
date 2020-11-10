import math
import time


def y(x):
    return math.exp(3 * x) * math.sin(2 * x)


def trapezoidal(a, b, n):
    h = (b - a) / n
    s = (y(a) + y(b))
    i = 1
    while i < n:
        s += 2 * y(a + i * h)
        i += 1
    return ((h / 2) * s)

x0 = 0
xn = math.pi / 4
n = 150
s_time = time.time()
time.sleep(1)# программа зысыпает на 1 секунду
#засыпание вставлено для того, чтобы таймер засчитал время
I = trapezoidal(x0, xn, n)
print("Результат обычного: %.4f" % (I))
en_time = time.time()
print("Время обычного: %0.6f сек" % (en_time - s_time-1))#отнимаем добавленную секунду
