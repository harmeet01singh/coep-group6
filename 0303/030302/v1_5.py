import random
from fractions import Fraction
import math
from coep_package.latex import latex, to_frac
from coep_package.csv_module import putInCsv, database_fn

a, b, c, d, e, f, g, h, questionVariationg, numerator, denominator = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
symbol1, symbol2, symbol3, expression, symbol1_dup, symbol2_dup, symbol3_dup = '', '', '', '', '', '', ''


def changeValues():
    global a, b, c, d, e, f, g, h
    a, b, g, h = random.sample(range(1, 10), k=4)
    c, d, e, f = random.sample(range(1, 10), k=4)


def getQuestionVariation1():
    global symbol1, symbol2, symbol3
    symbol1 = random.choice(['+', '-'])
    symbol2 = random.choice(['*', '/'])
    symbol3 = random.choice(['*', '/'])


def getQuestionVariation2():
    global symbol1, symbol2, symbol3
    symbol1 = random.choice(['*', '/'])
    symbol2 = random.choice(['+', '-'])
    symbol3 = random.choice(['*', '/'])


def getQuestion():
    global expression, symbol1, symbol2, symbol3, symbol1_dup, symbol2_dup, symbol3_dup, questionVariation
    changeValues()
    questionVariation = random.choice([1, 2])

    if questionVariation == 1:
        getQuestionVariation1()
    else:
        getQuestionVariation2()

    symbol1_dup = symbol1
    symbol2_dup = symbol2
    symbol3_dup = symbol3

    if symbol1 == '*':
        symbol1 = '\\times'
    elif symbol1 == '/':
        symbol1 = '\\div'
    if symbol2 == '*':
        symbol2 = '\\times'
    elif symbol2 == '/':
        symbol2 = '\\div'
    if symbol3 == '*':
        symbol3 = '\\times'
    elif symbol3 == '/':
        symbol3 = '\\div'

    expression = latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + symbol2 + ' ' + to_frac(e,
                                                                                                           f) + ' ' + symbol3 + ' ' + to_frac(
        g, h))
    return f"Simplify the following expression<br/>{expression}"


def getCorrectOption():
    ans = Fraction(numerator, denominator)
    return f"{latex(ans)}"


def getWrongOptions():
    ans = Fraction(numerator, denominator)
    while True:
        p, q, r = random.sample(range(ans.numerator - 50, ans.numerator + 50), k=3)
        ans1, ans2, ans3 = Fraction(p, ans.denominator), Fraction(q, ans.denominator), Fraction(r, ans.denominator)
        if ans1 != ans and ans2 != ans and ans3 != ans:
            break

    options = [f"{latex(ans1)}", f"{latex(ans2)}", f"{latex(ans3)}"]
    random.shuffle(options)
    return options


def getSolution():
    global numerator, denominator

    if questionVariation == 1:
        conversion1 = ''
        if symbol2 == '\\div' and symbol3 == '\\div':
            conversion1 = latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + '\\times' + ' ' + to_frac(f,
                                                                                                                      e) + ' ' + '\\times' + ' ' + to_frac(
                h, g))
            expression1 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac('(' + str(c) + '\\times' + str(f) + ')', '(' + str(
                    d) + '×' + str(e) + ')') + ' ' + '\\times' + ' ' + to_frac(h, g))
            expression2 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c * f, d * e) + ' ' + '\\times' + ' ' + to_frac(h, g))
            expression3 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(
                    '(' + str(Fraction(str(c * f) + '/' + str(d * e)).numerator) + '\\times' + str(h) + ')',
                    '(' + str(Fraction(str(c * f) + '/' + str(d * e)).denominator) + '\\times' + str(g) + ')'))
            expression4 = Fraction(str(Fraction(Fraction(str(c * f) + '/' + str(d * e)).numerator * h)) + '/' + str(
                Fraction(str(c * f) + '/' + str(d * e)).denominator * g))

        elif symbol2 == '\\div':
            conversion1 = latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + '\\times' + ' ' + to_frac(f,
                                                                                                                      e) + ' ' + '\\times' + ' ' + to_frac(
                g, h))
            expression1 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac('(' + str(c) + '\\times' + str(f) + ')', '(' + str(
                    d) + '\\times' + str(e) + ')') + ' ' + '\\times' + ' ' + to_frac(g, h))
            expression2 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c * f, d * e) + ' ' + '\\times' + ' ' + to_frac(g, h))
            expression3 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(
                    '(' + str(Fraction(str(c * f) + '/' + str(d * e)).numerator) + '\\times' + str(g) + ')',
                    '(' + str(Fraction(str(c * f) + '/' + str(d * e)).denominator) + '\\times' + str(h) + ')'))
            expression4 = Fraction(str(Fraction(Fraction(str(c * f) + '/' + str(d * e)).numerator * g)) + '/' + str(
                Fraction(str(c * f) + '/' + str(d * e)).denominator * h))

        elif symbol3 == '\\div':
            conversion1 = latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + '\\times' + ' ' + to_frac(e,
                                                                                                                      f) + ' ' + '\\times' + ' ' + to_frac(
                h, g))
            expression1 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + '\\times' + ' ' + to_frac(
                    '(' + str(e) + '\\times' + str(h) + ')', '(' + str(
                        f) + '\\times' + str(g) + ')'))
            expression2 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c, d) + ' ' + '\\times' + ' ' + to_frac(e * h, f * g))
            expression3 = latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac('(' + str(c) + '\\times' + str(
                Fraction(str(e * h) + '/' + str(f * g)).numerator) + ')', '(' + str(
                d) + '\\times' + str(Fraction(str(e * h) + '/' + str(f * g)).denominator) + ')'))
            expression4 = Fraction(str(Fraction(c * Fraction(str(e * h) + '/' + str(f * g)).numerator)) + '/' + str(
                d * Fraction(str(c * f) + '/' + str(d * e)).denominator))

        else:
            expression1 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac('(' + str(c) + '\\times' + str(e) + ')', '(' + str(
                    d) + '\\times' + str(f) + ')') + ' ' + '\\times' + ' ' + to_frac(g, h))
            expression2 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(c * e, d * f) + ' ' + '\\times' + ' ' + to_frac(g, h))
            expression3 = latex(
                to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(
                    '(' + str(Fraction(str(c * e) + '/' + str(d * f)).numerator) + '\\times' + str(g) + ')',
                    '(' + str(Fraction(str(c * e) + '/' + str(d * f)).denominator) + '\\times' + str(h) + ')'))
            expression4 = Fraction(str(Fraction(str(c * e) + '/' + str(d * f)).numerator * g) + '/' + str(
                Fraction(str(c * e) + '/' + str(d * f)).denominator * h))

        expression5 = latex(to_frac('(' + str(a) + '\\times' + str(expression4.denominator) + ' ' + symbol1 + ' ' + str(
            expression4.numerator) + '\\times' + str(b) + ')', '(' + str(b) + '\\times' + str(
            expression4.denominator) + ')'))
        expression6 = latex(to_frac('(' + str(a * expression4.denominator) + ' ' + symbol1 + ' ' + str(
            expression4.numerator * b) + ')', str(b * expression4.denominator)))

        if symbol1 == '+':
            expression7 = latex(to_frac(str(a * expression4.denominator + expression4.numerator * b), str(
                b * expression4.denominator)))
            numerator = a * expression4.denominator + expression4.numerator * b
        else:
            expression7 = latex(to_frac(str(a * expression4.denominator - expression4.numerator * b), str(
                b * expression4.denominator)))
            numerator = a * expression4.denominator - expression4.numerator * b
        denominator = b * expression4.denominator

        if math.gcd(numerator, denominator) != 1:
            expression8 = latex(
                to_frac(Fraction(numerator, denominator).numerator, Fraction(numerator, denominator).denominator))

        return f"""--------------------------------------SOLUTION-------------------------------------------<br/>
{expression}
{'<br/>=' + conversion1 + '  ...(convert division to multiplication)<br/>' if conversion1.find('ti') != -1 else '<br/>'}
= {expression1}<br/>
= {expression2}<br/>
= {expression3}<br/>
= {latex(to_frac(a, b) + ' ' + symbol1 + ' ' + to_frac(expression4.numerator, expression4.denominator))}    ...(multiplication first)<br/>
= {expression5}  {'  ...(then, addition)' if symbol1 == '+' else '  ...(then, subtraction)'}<br/>
= {expression6}<br/>
= {expression7}
{'<br/>=' + expression8 if math.gcd(numerator, denominator) != 1 else ''}<br/>
Hence the correct answer is {expression8 if math.gcd(numerator, denominator) != 1 else expression7}."""

    else:
        expression1 = ''
        if symbol1 == '\\div' and symbol3 == '\\div':
            expression1 = latex(to_frac(a, b) + ' ' + '\\times' + ' ' + to_frac(d, c) + ' ' + symbol2 + ' ' + to_frac(e,
                                                                                                                      f) + ' ' + '\\times' + ' ' + to_frac(
                h, g))
            expression2 = latex(to_frac('(' + str(a) + '\\times' + str(d) + ')',
                                        '(' + str(b) + '\\times' + str(c) + ')') + symbol2 + to_frac('(' + str(
                e) + '\\times' + str(h) + ')', '(' + str(f) + '×' + str(g) + ')'))
            x, y = Fraction(str(a * d) + '/' + str(b * c)), Fraction(str(e * h) + '/' + str(f * g))

        elif symbol1 == '\\div':
            expression1 = latex(to_frac(a, b) + ' ' + '\\times' + ' ' + to_frac(d, c) + ' ' + symbol2 + ' ' + to_frac(e,
                                                                                                                      f) + ' ' + '\\times' + ' ' + to_frac(
                g, h))
            expression2 = latex(to_frac('(' + str(a) + '\\times' + str(d) + ')',
                                        '(' + str(b) + '\\times' + str(c) + ')') + symbol2 + to_frac('(' + str(
                e) + '\\times' + str(g) + ')', '(' + str(f) + '×' + str(h) + ')'))
            x, y = Fraction(str(a * d) + '/' + str(b * c)), Fraction(str(e * g) + '/' + str(f * h))

        elif symbol3 == '\\div':
            expression1 = latex(to_frac(a, b) + ' ' + '\\times' + ' ' + to_frac(c, d) + ' ' + symbol2 + ' ' + to_frac(e,
                                                                                                                      f) + ' ' + '\\times' + ' ' + to_frac(
                h, g))
            expression2 = latex(to_frac('(' + str(a) + '\\times' + str(c) + ')',
                                        '(' + str(b) + '\\times' + str(d) + ')') + symbol2 + to_frac('(' + str(
                e) + '\\times' + str(h) + ')', '(' + str(f) + '×' + str(g) + ')'))
            x, y = Fraction(str(a * c) + '/' + str(b * d)), Fraction(str(e * h) + '/' + str(f * g))
        else:
            expression2 = latex(to_frac('(' + str(a) + '\\times' + str(c) + ')',
                                        '(' + str(b) + '\\times' + str(d) + ')') + ' ' + symbol2 + ' ' + to_frac(
                '(' + str(
                    e) + '\\times' + str(g) + ')', '(' + str(f) + '×' + str(h) + ')'))
            x, y = Fraction(str(a * c) + '/' + str(b * d)), Fraction(str(e * g) + '/' + str(f * h))

        p, q, r, s = x.numerator, x.denominator, y.numerator, y.denominator
        expression3 = latex(to_frac(p, q) + ' ' + symbol2 + ' ' + to_frac(r, s))
        expression4 = latex(
            to_frac('(' + str(p) + '\\times' + str(s) + ' ' + symbol2 + ' ' + str(r) + '\\times' + str(q) + ')',
                    '(' + str(q) + '\\times' + str(s) + ')'))

        if symbol2 == '+':
            numerator = p * s + r * q
        else:
            numerator = p * s - r * q
        denominator = q * s

        expression5 = latex(to_frac('(' + str(p * s) + ' ' + symbol2 + ' ' + str(r * q) + ')', '(' + str(q * s) + ')'))
        expression6 = latex(to_frac(numerator, denominator))

        if math.gcd(numerator, denominator) != 1:
            expression7 = latex(
                to_frac(Fraction(numerator, denominator).numerator, Fraction(numerator, denominator).denominator))

        return f"""--------------------------------------SOLUTION-------------------------------------------<br/>
{expression}
{'<br/>=' + expression1 + '  ...(convert division to multiplication)<br/>' if expression1.find('ti') != -1 else '<br/>'}
= {expression2}<br/>
= {expression3}    ...(multiplication first)<br/>
= {expression4}  {'  ...(then, addition)' if symbol2 == '+' else '  ...(then, subtraction)'}<br/>
= {expression5}<br/>
= {expression6}
{'<br/>=' + expression7 if math.gcd(numerator, denominator) != 1 else ''}<br/>
Hence the correct answer is {expression7 if math.gcd(numerator, denominator) != 1 else expression6}."""



def main_function():
    Question = getQuestion()
    Solution = getSolution()
    Corr_op = getCorrectOption()
    wrong_op1, wrong_op2, wrong_op3 = getWrongOptions()

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
    Filename="v1_5.py",
    Create_Textfile=True,
    Remove_Duplicates=True
)
