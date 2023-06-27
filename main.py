class Stack:
    def __init__(self, stack_list1):
        self.stack_list = stack_list1

    def is_empty(self):
        if self.stack_list:
            return 'False'
        else:
            return 'True'

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def bracket_balance(text, brackets='()[]{}'):
    open = brackets[::2]
    close = brackets[1::2]
    list_ = []
    for i in text:
        if i in open:
            line = Stack(list_)
            line.push(open.index(i))
        elif i in close:
            line = Stack(list_)
            if list_ and line.peek() == close.index(i):
                line.pop()
            else:
                print('Несбалансированно')
                return 'Несбалансированно'
    print('Сбалансированно')
    return 'Сбалансированно'


if __name__ == '__main__':
    text1 = input('Введите строку с скобками: ')
    bracket_balance(text1)