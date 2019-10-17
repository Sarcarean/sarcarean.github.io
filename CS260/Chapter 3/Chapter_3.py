from Stack import Stack

def do_math(op, op1, op2):
    if op == "*":
        result = op1 * op2
    elif op == "/":
        result = op1 / op2
    elif op == "**":
        result = op1 ** op2
    elif op == "//":
        result = op1 // op2
    elif op == "+":
        result = op1 + op2
    elif op == "-":
        result = op1 - op2
    return result

def isNumeric(chr):
    return chr.isnumeric()

def get_valid_operators():
    oper_dict = {}
    oper_dict["**"] = 3
    oper_dict["*"] = 3
    oper_dict["/"] = 3
    oper_dict["//"] = 3
    oper_dict["+"] = 2  
    oper_dict["-"] = 2
    oper_dict["("] = 1
    return oper_dict

def infix_to_postfix(exp):
    oper_dict = get_valid_operators()
    postfix_list = []
    chr_arr = list(exp)
    op_stack = Stack()
    i = 0
    while (i<len(chr_arr)):
        if isNumeric(chr_arr[i]):
            num = ''.join(chr_arr[i])
            while (i<len(chr_arr)-1) and isNumeric(chr_arr[i+1]):
                i = i + 1
                num = num + ''.join(chr_arr[i])
            postfix_list.append(num)
        elif ''.join(chr_arr[i]) == '(':
            op_stack.push('(')
        elif ''.join(chr_arr[i]) == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        elif (chr_arr[i] in oper_dict):
            oper = ''.join(chr_arr[i])
            while (i<len(chr_arr)-1) and (chr_arr[i+1] in oper_dict):
                i = i + 1
                oper = oper + ''.join(chr_arr[i])
            if (oper in oper_dict):
                while (not op_stack.isEmpty()) and (oper_dict[op_stack.peek()] >= oper_dict[oper]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(oper)
        i = i + 1
    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return postfix_list

def postfix_eval(exp):
    operand_stack = Stack()
    for token in exp:
        if isNumeric(token):
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

if __name__=="__main__":
    postfix_str = infix_to_postfix('12*2 + (5 * 10)')
    x = postfix_eval(postfix_str)
    print(x)        #The result should be 74