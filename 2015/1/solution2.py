puzzle_input = open('./puzzle_input.txt', 'r')
instructions = puzzle_input.readline()

ins_list = [1 if i == '(' else -1 if i == ')' else 0 for i in instructions]
current_floor = sum(ins_list)
print(current_floor)
