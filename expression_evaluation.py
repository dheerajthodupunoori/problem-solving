# Write a method which accepts a simple string mathematical expression, e.g. "1 - 3 + 2", which only contains + and -
# operators and valid integers, and returns the integer evaluation of the expression. Input: "12 - 19 + 2" Output: -5
# Input: "121" Output: 121


def evaluate_expression(expression):
    operands = []
    operators = []
    plus = "+"
    minus = "-"
    temp = ""
    for char in expression:
        if char not in (plus, minus):
            temp += char
        else:
            operands.append(int(temp))
            temp = ""
            operators.append(char)
    operands.append(int(temp))
    print(operands)
    print(operators)
    while operators:
        operand1 = operands.pop(0)
        operand2 = operands.pop(0)
        operator = operators.pop(0)
        result = evaluate(operand1, operand2, operator)
        operands.insert(0, result)
    print(operands[0])


def evaluate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2


evaluate_expression("12-19+2")
evaluate_expression("5+4-2")
evaluate_expression("9+4-7")
evaluate_expression("19-21+21-19")
