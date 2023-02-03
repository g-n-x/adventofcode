instructions = open('./puzzle_input.txt', 'r')

current_floor = 0

for instruction in instructions.readline():
    if instruction == '(':
        current_floor += 1
    if instruction == ')':
        current_floor -= 1

instructions.close()

print(current_floor)
