import random
from fractions import Fraction
import math
from coep_package.latex import latex, to_frac
from coep_package.csv_module import putInCsv, database_fn

a, b, c, d, e, f, g, h, ans = 0, 0, 0, 0, 0, 0, 0, 0, 0
symbol1, symbol2, symbol3, expression = '', '', '', ''


def getInnerExpression():
    p, q, r, s = random.sample(range(1, 10), k=4)
    symbol = random.choice(['-', '+'])

    inner_expression = str(p) + '/' + str(q) + ' ' + symbol + ' ' + str(r) + '/' + str(s)
    return p, q, r, s, symbol, inner_expression


def generateQuestion():
    global a, b, c, d, e, f, g, h, symbol1, symbol2, symbol3, expression

    a, b, c, d, symbol1, inner_expression1 = getInnerExpression()
    e, f, g, h, symbol3, inner_expression2 = getInnerExpression()
    symbol2 = random.choice(['-', '+'])

    expression = latex(
        '\\left(' + to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c,
                                                                  d) + '\\right)' + ' ' + symbol2 + ' ' + '\\left(' + to_frac(
            e, f) + ' ' + symbol3 + ' ' + to_frac(g, h) + '\\right)')


def getQuestion():
    generateQuestion()
    return f"Simplify the following expression<br/>{expression}"


def getCorrectOption():
    ans_expression = '(' + str(a / b) + ' ' + symbol1 + ' ' + str(c / d) + ')' + ' ' + symbol2 + ' ' + '(' + str(
        e / f) + ' ' + symbol3 + ' ' + str(g / h) + ')'
    ans = Fraction(eval(ans_expression)).limit_denominator()
    return f"{latex(ans)}"


def getWrongOptions():
    ans_expression = '(' + str(a / b) + ' ' + symbol1 + ' ' + str(c / d) + ')' + ' ' + symbol2 + ' ' + '(' + str(
        e / f) + ' ' + symbol3 + ' ' + str(g / h) + ')'
    ans = Fraction(eval(ans_expression)).limit_denominator()
    while True:
        p, q = random.sample(range(ans.numerator - 10, ans.numerator + 10), k=2)
        x, y = Fraction(p, ans.denominator), Fraction(q, ans.denominator)
        if x != ans and y != ans:
            break

    if symbol1 == symbol2 == symbol3 == '+' or symbol1 == symbol2 == symbol3 == '-':
        if symbol1 == symbol2 == symbol3 == '+':
            wrong_option_equation1 = ans_expression.replace('+', '-', 1)
            ans1 = Fraction(eval(wrong_option_equation1)).limit_denominator()
            wrong_option_equation2 = ans_expression.replace('+', '-', 2)
            ans2 = Fraction(eval(wrong_option_equation2)).limit_denominator()
            if '-' in str(ans1) or '-' in str(ans2):
                ans1 = abs(ans1)
                ans2 = abs(ans2)

        else:
            wrong_option_equation1 = ans_expression.replace('-', '+', 1)
            ans1 = Fraction(eval(wrong_option_equation1)).limit_denominator()
            wrong_option_equation2 = ans_expression.replace('-', '+', 2)
            ans2 = Fraction(eval(wrong_option_equation2)).limit_denominator()
    else:
        wrong_option_equation1 = ans_expression.replace('+', '-')
        ans1 = Fraction(eval(wrong_option_equation1)).limit_denominator()
        wrong_option_equation2 = ans_expression.replace('-', '+')
        ans2 = Fraction(eval(wrong_option_equation2)).limit_denominator()
    ans3 = Fraction(x, ans.denominator)

    if ans1 == ans:
        ans1 = y
    if ans2 == ans:
        ans2 = y

    options = [f"{latex(ans1)}", f"{latex(ans2)}", f"{latex(ans3)}"]
    random.shuffle(options)
    return options


def getSolution():
    expression1 = latex(
        to_frac('(' + str(a) + '\\times' + str(d) + ')' + ' ' + symbol1 + ' ' + '(' + str(c) + '\\times' + str(b) + ')',
                str(b) + '\\times' + str(d)) + ' ' + symbol2 + ' ' + to_frac(
            '(' + str(e) + '\\times' + str(h) + ')' + ' ' +
            symbol3 + ' ' + '(' + str(g) + '\\times' + str(f) + ')',
            str(f) + '\\times' + str(h)))

    expression2 = latex(to_frac('(' + str(a * d) + ' ' + symbol1 + ' ' + str(c * b) + ')', str(
        b * d)) + ' ' + symbol2 + ' ' + to_frac('(' + str(e * h) + ' ' + symbol3 + ' ' + str(g * f) + ')', str(f * h)))

    p, q, r, s = str(a * d + c * b) + '/' + str(b * d), str(a * d - c * b) + '/' + str(b * d), str(
        e * h + g * f) + '/' + str(f * h), str(e * h - g * f) + '/' + str(f * h)

    if symbol1 == '+' and symbol3 == '+':
        expression3 = latex(
            to_frac(str(a * d + c * b), str(b * d)) + ' ' + symbol2 + ' ' + to_frac(str(e * h + g * f), str(f * h)))
        expression4 = latex(to_frac('(' + str(Fraction(p).numerator) + '\\times' + str(
            Fraction(r).denominator) + ')' + ' ' + symbol2 + ' ' + '(' + str(
            Fraction(r).numerator) + '\\times' + str(Fraction(p).denominator) + ')', '(' + str(
            Fraction(p).denominator) + '\\times' + str(Fraction(r).denominator) + ')'))
        expression5 = latex(
            to_frac('(' + str(Fraction(p).numerator * Fraction(r).denominator) + ' ' + symbol2 + ' ' + str(
                Fraction(r).numerator * Fraction(p).denominator) + ')', str(
                Fraction(p).denominator * Fraction(r).denominator)))
        if symbol2 == '+':
            numerator, denominator = Fraction(p).numerator * Fraction(r).denominator + Fraction(r).numerator * Fraction(
                p).denominator, Fraction(p).denominator * Fraction(r).denominator
        else:
            numerator, denominator = Fraction(p).numerator * Fraction(r).denominator - Fraction(r).numerator * Fraction(
                p).denominator, Fraction(p).denominator * Fraction(r).denominator

    elif symbol1 == '+' and symbol3 == '-':
        expression3 = latex(
            to_frac(str(a * d + c * b), str(b * d)) + ' ' + symbol2 + ' ' + to_frac(str(e * h - g * f), str(f * h)))
        expression4 = latex(to_frac('(' + str(Fraction(p).numerator) + '\\times' + str(
            Fraction(s).denominator) + ')' + ' ' + symbol2 + ' ' + '(' + str(
            Fraction(s).numerator) + '\\times' + str(Fraction(p).denominator) + ')', '(' + str(
            Fraction(p).denominator) + '\\times' + str(Fraction(s).denominator) + ')'))
        expression5 = latex(
            to_frac('(' + str(Fraction(p).numerator * Fraction(s).denominator) + ' ' + symbol2 + ' ' + str(
                Fraction(s).numerator * Fraction(p).denominator) + ')', str(
                Fraction(p).denominator * Fraction(s).denominator)))
        if symbol2 == '+':
            numerator, denominator = Fraction(p).numerator * Fraction(s).denominator + Fraction(s).numerator * Fraction(
                p).denominator, Fraction(p).denominator * Fraction(s).denominator
        else:
            numerator, denominator = Fraction(p).numerator * Fraction(s).denominator - Fraction(s).numerator * Fraction(
                p).denominator, Fraction(p).denominator * Fraction(s).denominator

    elif symbol1 == '-' and symbol3 == '+':
        expression3 = latex(
            to_frac(str(a * d - c * b), str(b * d)) + ' ' + symbol2 + ' ' + to_frac(str(e * h + g * f), str(f * h)))
        expression4 = latex(to_frac('(' + str(Fraction(q).numerator) + '\\times' + str(
            Fraction(r).denominator) + ')' + ' ' + symbol2 + ' ' + '(' + str(
            Fraction(r).numerator) + '\\times' + str(Fraction(q).denominator) + ')', '(' + str(
            Fraction(q).denominator) + '\\times' + str(Fraction(r).denominator) + ')'))
        expression5 = latex(
            to_frac('(' + str(Fraction(q).numerator * Fraction(r).denominator) + ' ' + symbol2 + ' ' + str(
                Fraction(r).numerator * Fraction(q).denominator) + ')', str(
                Fraction(q).denominator * Fraction(r).denominator)))
        if symbol2 == '+':
            numerator, denominator = Fraction(q).numerator * Fraction(r).denominator + Fraction(r).numerator * Fraction(
                q).denominator, Fraction(q).denominator * Fraction(r).denominator
        else:
            numerator, denominator = Fraction(q).numerator * Fraction(r).denominator - Fraction(r).numerator * Fraction(
                q).denominator, Fraction(q).denominator * Fraction(r).denominator

    else:
        expression3 = latex(
            to_frac(str(a * d - c * b), str(b * d)) + ' ' + symbol2 + ' ' + to_frac(str(e * h - g * f), str(f * h)))
        expression4 = latex(to_frac('(' + str(Fraction(q).numerator) + '\\times' + str(
            Fraction(s).denominator) + ')' + ' ' + symbol2 + ' ' + '(' + str(
            Fraction(s).numerator) + '\\times' + str(Fraction(q).denominator) + ')', '(' + str(
            Fraction(q).denominator) + '\\times' + str(Fraction(s).denominator) + ')'))
        expression5 = latex(
            to_frac('(' + str(Fraction(q).numerator * Fraction(s).denominator) + ' ' + symbol2 + ' ' + str(
                Fraction(s).numerator * Fraction(q).denominator) + ')', str(
                Fraction(q).denominator * Fraction(s).denominator)))
        if symbol2 == '+':
            numerator, denominator = Fraction(q).numerator * Fraction(s).denominator + Fraction(s).numerator * Fraction(
                q).denominator, Fraction(q).denominator * Fraction(s).denominator
        else:
            numerator, denominator = Fraction(q).numerator * Fraction(s).denominator - Fraction(s).numerator * Fraction(
                q).denominator, Fraction(q).denominator * Fraction(s).denominator

    expression6 = latex(to_frac(str(numerator), str(denominator)))

    if math.gcd(numerator, denominator) != 1:
        expression7 = latex(
            to_frac(Fraction(numerator, denominator).numerator, Fraction(numerator, denominator).denominator))

    return f"""--------------------------------------SOLUTION-------------------------------------------<br/>
= {expression}<br/>
= {expression1}<br/>
= {expression2}<br/>
= {expression3}<br/>
= {expression4}<br/>
= {expression5}<br/>
= {expression6}<br/>
{'=' + expression7 if math.gcd(numerator, denominator) != 1 else ''}<br/>
Hence the correct answer is {expression7 if math.gcd(numerator, denominator) != 1 else expression6}."""


def main_function():
    Question = getQuestion()
    Corr_op = getCorrectOption()
    wrong_op1, wrong_op2, wrong_op3 = getWrongOptions()
    Solution = getSolution()

    database_dict = database_fn(
        Question_Type='text',
        Answer_Type='text',
        Topic_Number='030302',
        Variation='v1',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        ContributorMail='2019surendra.totre@ves.ac.in',
        Solution_text=Solution)
    return database_dict


putInCsv(
    Topic_Number='030302',
    Number_Of_Iterations=5,
    Main_Function=main_function,
    Filename="v1_6.py",
    Create_Textfile=True,
    Remove_Duplicates=True
)
