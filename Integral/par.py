import math
import time
from queue import Queue
from threading import Thread

# I(func) = integ(func, a, b)

workers = 4
task_queue = Queue()
I = 0


def method(func, a, b, tol):
    S = []
    S.append((a, b))
    global I
    while S:
        a, b = S.pop()
        I1 = ((b - a) / 2) * (func(a) + func(b))  # метод трапеций
        m = (a + b) / 2
        I2 = ((b - a) / 4) * (func(a) + func(b) + 2 * func(m))
        if abs(I1 - I2) < 3 * (b - a) * tol:
            I += I2
        else:
            S.append((a, m))
            S.append((m, b))


def func(x):
    return math.exp(3 * x) * math.sin(2 * x)


a = 0
b = math.pi / 4
xPoints = []
for i in range(workers):
    xPoints.append(a + i * (b - a) / 4)
xPoints.append(b)
# Создаём рабочие потоки
start_time = time.time()
threads = [Thread(target=method(func, xPoints[i], xPoints[i + 1], (math.pi / 4) * .0001)) for i in range(workers)]
# for thread in threads:
#     print(thread.start())
[thread.start() for thread in threads]
[thread.join() for thread in threads]
print("Результат с потоками: %0.4f" % (I))
end_time = time.time()

print("Время с потоками: %0.6f сек" %(end_time - start_time))


