import intcode
from copy import copy

tests = [
    [1,9,10,3,2,3,11,0,99,30,40,50],
    [1,1,1,4,99,5,6,0,99],
]

for test in tests:
    mem, index = intcode.run(test)
    intcode.pretty(mem, index)

my_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]

def runPart(mem, noun, verb):
    new_mem = copy(mem)
    new_mem[1] = noun
    new_mem[2] = verb
    return intcode.run(new_mem)

def part1(mem):
    mem, index = runPart(mem, 12, 2)
    intcode.pretty(mem, index)
    print(mem[0])

def part2(mem):
    for noun in range(100):
        for verb in range(100):
            result, index = runPart(mem, noun, verb)
            if result[0] == 19690720:
                answer = 100 * noun + verb
                print(f'100 * {noun} + {verb} = {answer}')
                return

part1(my_input)
part2(my_input)

