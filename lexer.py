import math

def read(text):
    stack = []
    with open(text, 'r') as f:
        diction = {}
        for line in f:
            stack = line.split()
            test(stack, diction)
            
def test(stack, variables):
    if len(stack) > 1:
        for i in range(len(stack)):
            if stack[i] == '+':
                stack[i] = str(int(stack[i-1]) + int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == '-':
                stack[i] = str(int(stack[i-1]) - int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == '*':
                stack[i] = str(int(stack[i-1]) * int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == '/':
                stack[i] = str(int(stack[i-1]) / int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == '//':
                stack[i] = str(int(stack[i-1]) // int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == 'print':
                print(stack[i-1])
                del stack[i]
                del stack[i-1]
                break
            elif stack[i] == '^':
                stack[i] = str(int(stack[i-1]) ** int(stack[i-2]))
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == '=':
                varname = stack[i-1]
                nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                if varname[0] in nums:
                    print('All variables must start with a letter. Error: '+stack[i-1])
                else:
                    variables[stack[i-1]] = stack[i-2]
                del stack[i]
                del stack[i-1]
                del stack[i-2]
                break
            elif stack[i] == 'sqrt':
                stack[i] = math.sqrt(int(stack[i-1]))
                del stack[i-1]
                break
            elif stack[i] in variables:
                stack[i] = variables[stack[i]]
        test(stack, variables)

read("test.txt")
