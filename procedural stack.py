stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)
push(5)
push(10)
push(5)
push(12)
print(stack)


print(pop())
print(pop())
print(pop())

print(stack)
