def run(program):
    variables = {chr(ord('A')+i): 0 for i in range(26)}
    output = []
    i = 0

    while i < len(program):
        line = program[i]
        parts = line.split(' ')

        if parts[0] == 'PRINT':
            value = evaluate_expression(parts[1], variables)
            output.append(value)
        elif parts[0] == 'MOV':
            variable = parts[1]
            value = evaluate_expression(parts[2], variables)
            variables[variable] = value
        elif parts[0] == 'ADD':
            variable = parts[1]
            value = evaluate_expression(parts[2], variables)
            variables[variable] += value
        elif parts[0] == 'SUB':
            variable = parts[1]
            value = evaluate_expression(parts[2], variables)
            variables[variable] -= value
        elif parts[0] == 'MUL':
            variable = parts[1]
            value = evaluate_expression(parts[2], variables)
            variables[variable] *= value
        elif parts[0].endswith(':'):
            pass  # No action needed for labels
        elif parts[0] == 'JUMP':
            label = parts[1]
            i = find_label(program, label) - 1  # Subtract 1 because we increment later
        elif parts[0] == 'IF':
            condition = parts[1]
            label = parts[3]
            if evaluate_condition(condition, variables):
                i = find_label(program, label) - 1  # Subtract 1 because we increment later
        elif parts[0] == 'END':
            break

        i += 1

    return output

def evaluate_expression(expression, variables):
    if expression.isdigit():
        return int(expression)
    else:
        return variables[expression]

def evaluate_condition(condition, variables):
    value1, comp_op, value2 = condition.split()
    value1 = evaluate_expression(value1, variables)
    value2 = evaluate_expression(value2, variables)

    if comp_op == '==':
        return value1 == value2
    elif comp_op == '!=':
        return value1 != value2
    elif comp_op == '<':
        return value1 < value2
    elif comp_op == '<=':
        return value1 <= value2
    elif comp_op == '>':
        return value1 > value2
    elif comp_op == '>=':
        return value1 >= value2

def find_label(program, label):
    for i, line in enumerate(program):
        if line.rstrip(':') == label:
            return i
    return -1

