''' Intcode module '''
from copy import copy

def add(mem, index):
    ''' Opcode 1 adds together numbers read from two positions and stores the
    result in a third position '''
    addr1 = mem[index + 1]
    addr2 = mem[index + 2]
    dest = mem[index + 3]

    new_mem = copy(mem)
    new_mem[dest] = mem[addr1] + mem[addr2]
    return (new_mem, index + 4)

def multiply(mem, index):
    ''' Opcode 2 multiplies together numbers read from two positions and stores the
    result in a third position '''
    addr1 = mem[index + 1]
    addr2 = mem[index + 2]
    dest = mem[index + 3]

    new_mem = copy(mem)
    new_mem[dest] = mem[addr1] * mem[addr2]

    return (new_mem, index + 4)

def step(mem, index):
    ''' step through the code '''
    operation = mem[index]
    if operation == 1:
        return add(mem, index)
    if operation == 2:
        return multiply(mem, index)
    raise Exception(f'Unknown op {operation} at {index}')

def pretty(mem, index):
    printable = copy(mem)
    printable[index] = '*' + str(printable[index]) + '*'
    print(printable)

def run(mem):
    ''' Runs the code '''
    index = 0
    while mem[index] != 99:
        # pretty(mem, index)
        mem, index = step(mem, index)
    return (mem, index)
