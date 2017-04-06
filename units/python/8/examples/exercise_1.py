class Stack:
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def stack_top(self):
        return self.__list[-1]

    def size(self):
        return len(self.__list)

    def to_list(self):
        return self.__list

