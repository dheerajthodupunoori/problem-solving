# https://leetcode.com/discuss/interview-question/1061028/Indeed-or-Phone-Screen-(
# Karat)-or-Parent-Child-Graph-and-Calculator Same aim as Q1 above, but this time the expression includes nested
# expressions, e.g. "12 + 2 + ((4 - 19) - 1)" containing ( and ) brackets only. Evaluate and return the answer to
# this expression. Input: "12 - (1 - 2)" Output: 13

def calculate(s):
    s = s.strip()
    if s[0] == "-":
        s = "0" + s
    operands = []
    operators = []
    temp_operands = []
    temp_operators = []
    temp = ""
    for index, char in enumerate(s):
        if char not in ("(", ")", "+", "-", " "):
            temp += char
        elif char in ("(", "+", "-"):
            if char == "-" and s[index - 1] == "(":
                operands.append(0)
            if temp != "":
                operands.append(int(temp))
                temp = ""
            operators.append(char)
        elif char == ")":
            if temp != "":
                operands.append(int(temp))
                temp = ""
            while operands and operators and operators[-1] != "(":
                temp_operands.append(operands.pop())
                temp_operators.append(operators.pop())
            operators.pop()
            temp_operands.append(operands.pop())
            result = evaluate_expression(temp_operands, temp_operators)
            operands.append(result)
            temp_operands = []
            temp_operators = []
    if temp != "":
        operands.append(int(temp))
    while operators:
        operand1 = operands.pop(0)
        operand2 = operands.pop(0)
        operator = operators.pop(0)
        result = evaluate(operand1, operand2, operator)
        operands.insert(0, result)
    return operands[0]


def evaluate_expression(operands, operators):
    while operators:
        operand1 = operands.pop()
        operand2 = operands.pop()
        operator = operators.pop()
        result = evaluate(operand1, operand2, operator)
        operands.append(result)
    return operands[0]


def evaluate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2


print(calculate("12 + 2 + ((4 - 19) - 1)"))
print(calculate("12 - (1 - 2)"))


expression2_1 = "5+16-((9-6)-(4-2))+1"
expression2_2 = "22+(2-4)"
expression2_3 = "6+9-12"
expression2_4 = "((1024))"
expression2_5 = "1+(2+3)-(4-5)+6"
expression2_6 = "255"


print(calculate(expression2_1))
print(calculate(expression2_2))
print(calculate(expression2_3))
print(calculate(expression2_4))
print(calculate(expression2_5))
print(calculate(expression2_6))
