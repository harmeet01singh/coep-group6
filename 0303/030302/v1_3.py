import random
import math
import os
from coep_package.latex import latex
from coep_package.csv_module import putInCsv, database_fn

signs = ['+', '-', '*', '/']

expression2 = ''
inter_solution2 = ''
inter_solution2_2 = ''
solution2 = ''
solution2_2 = ''
calc_ans2 = ''
eval_expression = ''
correctIndex = ''
allOptions = []
wrong_Options = []
soln_print = ''

def generateExpressionBracket1():
    var1 = random.randint(-150, 150)
    var2 = random.randint(1, 150)
    var3 = random.randint(-150, 150)
    symbol1 = signs[random.randint(0,3)]
    symbol2 = signs[random.randint(0,3)]
    if var1 < 0:
        var1 = '(' + str(var1) + ')'
    if var3 < 0:
        var3 = '(' + str(var3) + ')'

    expression1 = '(' + str(var1) + ' ' + symbol1 + ' ' + str(var2) + ' ' + symbol2 + ' ' + str(var3) + ')'
    calc_ans1 = str(round(eval(expression1), 2))
    ans = None
    soln1 = None
    soln2 = None
    if symbol1 in '*/':
        ans = round(eval(str(var1) + ' ' + symbol1 + ' ' + str(var2)), 2)
        soln1 = str(var1) + ' ' + symbol1 + ' ' + str(var2)
    else:
        ans = round(eval(str(var2) + ' ' + symbol2 + ' ' + str(var3)), 2)
        soln2 = str(var2) + ' ' + symbol2 + ' ' + str(var3)

    solution1 = ''
    if soln2 == None:
        soln2 = symbol2 + ' ' + str(var3)
        solution1 = '(' + str(ans) + ' ' + soln2 + ')'
    else:
        soln1 =  str(var1) + ' ' + symbol1
        solution1 = '(' + soln1 + ' ' + str(ans) + ')'
    return expression1, solution1, calc_ans1

def generateExpressionBracket2():
    var3 = random.randint(1, 150)
    var4 = random.randint(-150, 150)
    var5 = random.randint(1, 150)
    expression1, solution1, calc_ans1 = generateExpressionBracket1()
    symbol1 = signs[random.randint(0,3)]
    symbol2 = signs[random.randint(0,3)]
    symbol3 = signs[random.randint(0,3)]

    if var4 < 0:
        var4 = '(' + str(var4) + ')'

    expression2 = '[' + expression1 + ' ' + symbol1 + ' ' + str(var3) + ' ' + symbol2 + ' ' + str(var4) + ']' + ' ' + symbol3 + ' ' + str(var5)
    eval_expression = '(' + expression1 + ' ' + symbol1 + ' ' + str(var3) + ' ' + symbol2 + ' ' + str(var4) + ')' + ' ' + symbol3 + ' ' + str(var5)
    calc_ans2 = round(eval(eval_expression), 2)
    ans = None
    soln1 = None
    soln2 = None

    inter_solution2 = '[' + solution1 + ' ' + symbol1 + ' ' + str(var3) + ' ' + symbol2 + ' ' + str(var4) + ']' + ' ' + symbol3 + ' ' + str(var5)
    inter_solution2_2 = '[' + calc_ans1 + ' ' + symbol1 + ' ' + str(var3) + ' ' + symbol2 + ' ' + str(var4) + ']' + ' ' + symbol3 + ' ' + str(var5)
    if symbol1 in '*/':
        ans = round(eval(str(calc_ans1) + ' ' + symbol1 + ' ' + str(var3)), 2)
        soln1 = symbol2 + ' ' + str(var4)
    elif symbol2 in '*/':
        ans = round(eval(str(var3) + ' ' + symbol2 + ' ' + str(var4)), 2)
        soln2 = str(calc_ans1) + ' ' + symbol1
    else:
        ans = round(eval(str(calc_ans1) + ' ' + symbol1 + ' ' + str(var3)), 2)
        soln1 = symbol2 + ' ' + str(var4)

    solution2 = ''
    if soln2 == None:
        soln2 = symbol2 + ' ' + str(var4)
        solution2 = '[' + str(ans) + ' ' + soln2 + ']' + ' ' + symbol3 + ' ' + str(var5)
        eval_exp = str(ans) + ' ' + soln2
    else:
        soln1 =  str(calc_ans1) + ' ' + symbol1
        solution2 = '[' + soln1 + ' ' + str(ans) + ']' + ' ' + symbol3 + ' ' + str(var5)
        eval_exp = soln1 + ' ' + str(ans)

    solution2_2 = str(round(eval(eval_exp), 2)) + ' ' + symbol3 + ' ' + str(var5)

    calc_ans2 = round(eval(solution2_2), 2)

    expression2 = expression2.replace('*', '\\times')
    inter_solution2 = inter_solution2.replace('*', '\\times')
    inter_solution2_2 = inter_solution2_2.replace('*', '\\times')
    solution2 = solution2.replace('*', '\\times')
    solution2_2 = solution2_2.replace('*', '\\times')

    return expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression
    

def solution(expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, correctIndex, allOptions, wrong_Options):
    

    for i in range(0, 4):
        if i+1 != int(correctIndex):
            allOptions[i] = latex(allOptions[i])

    return f"= {latex(expression2)}<br/>\n= {latex(inter_solution2)}<br/>\n= {latex(inter_solution2_2)}<br/>\n= {latex(solution2)}<br/>\n= {latex(solution2_2)}<br/>\n= {latex(calc_ans2)}<br/>\nTherefore option {latex(correctIndex)} is right selection"

def question(expression2):
    return(f"Solve the given expression and round the decimal place up to 2 digits at each step\n{expression2}")

def options(calc_ans2, eval_expression):
    allOptions = []
    allOptions.append(calc_ans2)

    wrong_options_expression1 = eval_expression.replace('+', '*')
    allOptions.append(round(eval(wrong_options_expression1), 2) + random.randint(1, 4))

    wrong_options_expression2 = eval_expression.replace('/', '-')
    allOptions.append(round(eval(wrong_options_expression2), 2) + random.randint(1, 4))

    wrong_options_expression3 = eval_expression.replace('*', '/')
    allOptions.append(round(eval(wrong_options_expression3), 2) + random.randint(1, 4))

    wrong_options = []
    random.shuffle(allOptions)
    correctIndex = None
    wrong_options = []
    for i in range(1, 5):
        if allOptions[i-1] == calc_ans2:
            correctIndex = i
            latex(allOptions[i-1])
        else:
            wrong_options.append(latex(allOptions[i-1]))

    return correctIndex, allOptions, wrong_options

def changeValues():
    global expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression

    expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression = generateExpressionBracket2()

    correctIndex, allOptions, wrong_Options= options(calc_ans2, eval_expression)

    expression2 = expression2.replace('/', '\div')
    inter_solution2 = inter_solution2.replace('/', '\div')
    inter_solution2_2 = inter_solution2_2.replace('/', '\div')
    solution2 = solution2.replace('/', '\div')
    solution2_2 = solution2_2.replace('/', '\div')

    soln_print = solution(expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, correctIndex, allOptions, wrong_Options)

    expression2 = latex(expression2)
    calc_ans2 = latex(calc_ans2)
    
    return expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, correctIndex, allOptions, wrong_Options, soln_print


def main_function():
    expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, correctIndex, allOptions, wrong_Options, soln_print = changeValues()

    Question = question(expression2)
    Corr_op = calc_ans2
    wrong_op1, wrong_op2, wrong_op3 = wrong_Options
    Solution = soln_print

    database_dict= database_fn(
        Question_Type='text',
        Answer_Type='text',
        Topic_Number='030302',
        Variation='v1',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        ContributorMail = '2019yash.kumthekar@ves.ac.in', 
        Solution_text=Solution
    )
    return database_dict


putInCsv(
    Topic_Number='030302',
    Number_Of_Iterations=5,
    Main_Function=main_function,
    Filename='v1_3.py',
    Create_Textfile=True,
    Remove_Duplicates=True
)














