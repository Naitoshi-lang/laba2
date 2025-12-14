class Stack:
    """Стек (LIFO) на статическом массиве"""
    def __init__(self):
        self.MAX = 20
        self.data = [None] * self.MAX
        self.top = -1
    
    def push(self, x):
        if not (0 < x < 100): 
            return print(f"Ошибка: {x} должно быть 0 < x < 100")
        if self.top == self.MAX - 1: 
            return print("Ошибка: стек переполнен")
        self.top += 1
        self.data[self.top] = x
    
    def pop(self):
        if self.top == -1: 
            print("Ошибка: стек пуст")
            return None
        val = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return val
    
    def peek(self): 
        return None if self.top == -1 else self.data[self.top]
    def size(self): return self.top + 1
    def clear(self): 
        self.data = [None] * self.MAX
        self.top = -1
    def display(self):
        print(f"Стек({self.size()}):", [self.data[i] for i in range(self.top, -1, -1)])

class Queue:
    """Очередь (FIFO) на статическом массиве"""
    def __init__(self):
        self.MAX = 20
        self.data = [None] * self.MAX
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def enqueue(self, x):
        if not (0 < x < 100): 
            return print(f"Ошибка: {x} должно быть 0 < x < 100")
        if self.count == self.MAX: 
            return print("Ошибка: очередь переполнена")
        self.rear = (self.rear + 1) % self.MAX
        self.data[self.rear] = x
        self.count += 1
    
    def dequeue(self):
        if self.count == 0: 
            print("Ошибка: очередь пуста")
            return None
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.MAX
        self.count -= 1
        return val
    
    def front(self): 
        return None if self.count == 0 else self.data[self.front]
    def size(self): return self.count
    def clear(self): 
        self.data = [None] * self.MAX
        self.front = 0
        self.rear = -1
        self.count = 0
    def display(self):
        lst = []
        idx = self.front
        for _ in range(self.count):
            lst.append(self.data[idx])
            idx = (idx + 1) % self.MAX
        print(f"Очередь({self.size()}):", lst)

class MinHeap:
    """Минимальная двоичная куча на статическом массиве"""
    def __init__(self):
        self.MAX = 20
        self.data = [None] * self.MAX
        self.size = 0
    
    def _sift_up(self, i):
        while i > 0 and self.data[i] < self.data[(i-1)//2]:
            self.data[i], self.data[(i-1)//2] = self.data[(i-1)//2], self.data[i]
            i = (i-1)//2
    
    def _sift_down(self, i):
        while 2*i+1 < self.size:
            left = 2*i+1
            right = 2*i+2
            smallest = i
            if self.data[left] < self.data[smallest]:
                smallest = left
            if right < self.size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i: break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest
    
    def insert(self, x):
        if not (0 < x < 100): 
            return print(f"Ошибка: {x} должно быть 0 < x < 100")
        if self.size == self.MAX: 
            return print("Ошибка: куча переполнена")
        self.data[self.size] = x
        self._sift_up(self.size)
        self.size += 1
    
    def extract_min(self):
        if self.size == 0: 
            print("Ошибка: куча пуста")
            return None
        min_val = self.data[0]
        self.data[0] = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size -= 1
        if self.size > 0: 
            self._sift_down(0)
        return min_val
    
    def get_min(self): 
        return None if self.size == 0 else self.data[0]
    def size(self): return self.size
    def clear(self): 
        self.data = [None] * self.MAX
        self.size = 0
    def display(self):
        print(f"Куча({self.size()}):", self.data[:self.size])
