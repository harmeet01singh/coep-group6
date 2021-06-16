import random
import math
import os
from coep_package.latex import latex
from coep_package.csv_module import putInCsv, database_fn


signs = ['+', '-', '*', '/']

expression3 = ''
inter_solution2 = ''
inter_solution2_2 = ''
solution2 = ''
solution2_2 = ''
solution3 = ''
solution3_3 = ''
calc_ans3 = ''
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

    return expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, eval_exp, symbol3, var5
    

def generateExpressionBracket3():
    var6 = random.randint(1, 150)
    var7 = random.randint(-150, 150)
    expression2, inter_solution2, inter_solution2_2, solution2, solution2_2, calc_ans2, eval_expression, eval_exp, symbol3, var5 = generateExpressionBracket2()
    
    symbol1 = signs[random.randint(0,3)]
    symbol2 = signs[random.randint(0,3)]

    if var7 < 0:
        var7 = '(' + str(var7) + ')'

    expression3 = '{' + str(var6) + ' ' + symbol1 + ' ' + expression2 + ' }' + ' ' + symbol2 + ' ' + str(var7)

    eval_expression2 = '(' + str(var6) + ' ' + symbol1 + ' ' + eval_expression + ' )' + ' ' + symbol2 + ' ' + str(var7)
    calc_ans3 = round(eval(eval_expression2), 2)

    inter_solution2 = '{' + str(var6) + ' ' + symbol1 + ' ' + inter_solution2 + '}' + ' ' + symbol2 + ' ' + str(var7)
    inter_solution2_2 = '{' + str(var6) + ' ' + symbol1 + ' ' + inter_solution2_2 + '}' + ' ' + symbol2 + ' ' + str(var7)
    solution2 = '{' + str(var6) + ' ' + symbol1 + ' ' + solution2 + '}' + ' ' + symbol2 + ' ' + str(var7)
    solution2_2 = '{' + str(var6) + ' ' + symbol1 + ' ' + solution2_2 + '}' + ' ' + symbol2 + ' ' + str(var7)

    eval_expression = expression3.replace('[', '(')
    eval_expression = eval_expression.replace(']', ')')
    eval_expression = eval_expression.replace('{', '(')
    eval_expression = eval_expression.replace('}', ')')

    ans = None
    soln1 = None
    soln2 = None
    
    eval_exp = '(' + eval_exp + ')'
    if symbol1 in '*/':
        ans = round(eval(str(var6) + ' ' + symbol1 + str(eval_exp)), 2)
        soln1 = '{' + str(ans) + ' ' + symbol3 + ' ' + str(var5) + '} ' + symbol2 + ' ' + str(var7)
    elif symbol3 in '*/':
        ans = round(eval(str(eval_exp) + ' ' + symbol3 + ' ' + str(var5)), 2)
        soln2 = '{' + str(var6) + ' ' + symbol1 + ' ' + str(ans) + '} ' + symbol2 + ' ' + str(var7)
    else:
        ans = round(eval(str(var6) + ' ' + symbol1 + str(eval_exp)), 2)
        soln1 = '{' + str(ans) + ' ' + symbol3 + ' ' + str(var5) + '} ' + symbol2 + ' ' + str(var7)

    solution3 = ''
    eval_exp1 = None
    if soln2 == None:
        solution3 = soln1
        eval_exp1 = str(ans) + ' ' + symbol3 + ' ' + str(var5)
    else:
        solution3 = soln2
        eval_exp1 = str(var6) + ' ' + symbol1 + ' ' + str(ans)
    
    solution3_3 = None
    solution3_3 = str(round(eval(eval_exp1), 2)) + ' ' + symbol2 + ' ' + str(var7)

    calc_ans3 = round(eval(solution3_3), 2)

    expression3 = expression3.replace('*', '\\times')
    inter_solution2 = inter_solution2.replace('*', '\\times')
    inter_solution2_2 = inter_solution2_2.replace('*', '\\times')
    solution2 = solution2.replace('*', '\\times')
    solution2_2 = solution2_2.replace('*', '\\times')
    solution3 = solution3.replace('*', '\\times')
    solution3_3 = solution3_3.replace('*', '\\times')

    return expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression


def solution(expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression, correctIndex, allOptions, wrong_options):

    for i in range(0, 4):
        if i+1 != int(correctIndex):
            allOptions[i] = latex(allOptions[i])

    return f"= {latex(expression3)}<br/>\n= {latex(inter_solution2)}<br/>\n= {latex(inter_solution2_2)}<br/>\n= {latex(solution2)}<br/>\n= {latex(solution2_2)}<br/>\n= {latex(solution3)}<br/>\n= {latex(solution3_3)}<br/>\n= {latex(calc_ans3)}<br/>\nTherefore option {latex(correctIndex)} is right selection"

def question(expression3):
    return(f"Solve the given expression and round the decimal place up to 2 digits at each step\n{expression3}")

def options(calc_ans3, eval_expression):
    allOptions = []
    allOptions.append(calc_ans3)

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
        if allOptions[i-1] == calc_ans3:
            correctIndex = i
            latex(allOptions[i-1])
        else:
            wrong_options.append(latex(allOptions[i-1]))

    return correctIndex, allOptions, wrong_options

def changeValues():
    global expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression

    expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression = generateExpressionBracket3()

    correctIndex, allOptions, wrong_Options= options(calc_ans3, eval_expression)

    expression3 = expression3.replace('/', '\div')
    inter_solution2 = inter_solution2.replace('/', '\div')
    inter_solution2_2 = inter_solution2_2.replace('/', '\div')
    solution2 = solution2.replace('/', '\div')
    solution2_2 = solution2_2.replace('/', '\div')
    solution3 = solution3.replace('/', '\div')
    solution3_3 = solution3_3.replace('/', '\div')

    soln_print = solution(expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression, correctIndex, allOptions, wrong_Options)

    expression3 = latex(expression3)
    calc_ans3 = latex(calc_ans3)

    
    return expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression, correctIndex, allOptions, wrong_Options, soln_print


def main_function():
    expression3, inter_solution2, inter_solution2_2, solution2, solution2_2, solution3, solution3_3, calc_ans3, eval_expression, correctIndex, allOptions, wrong_Options, soln_print = changeValues()

    Question = question(expression3)
    Corr_op = calc_ans3
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
    Filename='v1_4.py',
    Create_Textfile=True,
    Remove_Duplicates=True
)
















