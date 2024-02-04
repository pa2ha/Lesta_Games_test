class ListFIFO:
    def __init__(self, list_length):
        self.list_length = list_length
        self.queue = [None] * list_length
        self.size = 0
        self.head = 0
        self.tail = 0

    def put(self, item):
        if self.size == self.list_length:
            return print("Очередь заполненна")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.list_length
        self.size += 1

    def get(self):
        if self.size == 0:
            return print("Очередь пуста")
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.list_length
        self.size -= 1
        return print(item)


"""
Обе операции добавления и удаления элементов
выполняются законстантное время O(1).


Буфер имеет ограниченный размер, что может быть
недостаточно гибким в некоторых сценариях.
Использование статического массива может привести к избыточному
использованию памяти при создании буфера с большим размером,
даже если не все ячейки используются.
"""


class LinkedListFIFO:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, x):
        new_node = self.Node(x)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def get(self):
        if self.size == 0:
            return print("Очередь пуста")
        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return print(result)


"""
Не имеет ограничения на размер буфера,
что делает его более гибким.
Удаление элемента из начала буфера происходит за
константное время O(1), что делает эту операцию эффективной.


Элементы могут быть распределены по разным участкам памяти,
что может привести к фрагментации памяти и небольшому
увеличению накладных расходов на управление памятью.

Использование связного списка требует
дополнительной логики для управления указателями,
что может усложнить реализацию по сравнению с массивом.
"""
