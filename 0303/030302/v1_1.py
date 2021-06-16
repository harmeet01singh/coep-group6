import random
from coep_package.latex import latex
from coep_package.csv_module import putInCsv, database_fn

div='\div'
mul='\\times'
br='<br/>'
correct_option=''
question_list = []

def changequestion():
    global question_list
    plusminus = random.choice(['+','-'])
    operators = [div,mul,plusminus]
    numbers = [str(random.randint(2,50)),str(random.randint(2,50)),str(random.randint(2,50))]
    divnumber = str(random.randint(2,10))
    random.shuffle(operators)
    n=0
    question_list = [numbers[n]]
    for i in operators:
        question_list = question_list + [i]
        if i == div:
            question_list = question_list + [divnumber]
        else:
            n+=1
            question_list = question_list + [numbers[n]]

def mod(num_in_float,r):
    num_in_int = int(num_in_float)
    if(num_in_int-num_in_float==0):
        return str(num_in_int)
    return str(round(num_in_float,r))

def getQuestion():
    question = ''.join(question_list)
    return f"Simplify The Given Expression :{latex(question)}"

def make_options():
    global correct_option
    evaluate=''.join(question_list)
    evaluate = evaluate.replace(div,'/').replace(mul,'*')
    correct_option=latex(mod(float(eval(evaluate)),2))
    question=question_list

    #Wrong option 1
    if '+' in question :
            index_of_sign = question.index('+')
    elif '-' in question :
            index_of_sign = question.index('-')
    temp_question = question[:index_of_sign-1]+['(']+question[index_of_sign-1:]
    temp_question = temp_question[:index_of_sign+3]+[')']+temp_question[index_of_sign+3:]
    evaluate=''.join(temp_question)
    evaluate = evaluate.replace(div,'/').replace(mul,'*')
    wrong_option = [latex(mod(float(eval(evaluate)),2))]

    #Wrong option 2
    evaluate=''.join(question)
    evaluate = evaluate.replace(div,'/').replace(mul,'*')
    index_of_mul = evaluate.index('*')
    index_of_div = evaluate.index('/')
    evaluate = evaluate[:index_of_mul]+'/'+evaluate[index_of_mul+1:]
    evaluate = evaluate[:index_of_div]+'*'+evaluate[index_of_div+1:]
    wrong_option = wrong_option+[latex(mod(float(eval(evaluate)),2))]

    #Wrong option 3
    evaluate=''.join(question)
    evaluate = evaluate.replace(div,'/').replace(mul,'*')
    multi_div = random.choice(['*','/'])
    if '+' in question :
            plusminus='+'
    elif '-' in question :
            plusminus='-'
    evaluate = evaluate.replace(multi_div,plusminus).replace(plusminus,multi_div)
    wrong_option = wrong_option+[latex(mod(float(eval(evaluate)),2))]

    return correct_option,wrong_option


def getsol():
    question=question_list
    solution="-------SOLUTION-------"+br
    solution = solution +'\n'+ latex(''.join(question))+br
    while len(question) != 1:
        index_of_div=index_of_mul=100
        
        if mul in question :
            index_of_mul = question.index(mul)

        if div in question :
            index_of_div = question.index(div)

        if index_of_mul<index_of_div :
            question.pop(index_of_mul)
            first_no = question.pop(index_of_mul-1)
            second_no = question.pop(index_of_mul-1)
            operation = '*'
            ans_index = index_of_mul-1
        
        elif index_of_div!=100 :
            question.pop(index_of_div)
            first_no = question.pop(index_of_div-1)
            second_no = question.pop(index_of_div-1)
            operation = '/'
            ans_index = index_of_div-1

        else :
            first_no = question.pop(0)
            operation = question.pop(0)
            second_no = question.pop(0)
            ans_index = 0
        
        ans = mod(float(eval(first_no+operation+second_no)),4)
        if float(ans)<0 and len(question) > 1:
            ans = '('+ans+')'
        question.insert(ans_index,ans)

        evaluate=''.join(question)
        solution=solution+'\n'+latex('='+evaluate)+br
        if len(question) == 1:
            num_in_float = eval(question[0])
            num_in_float2 = round(num_in_float,2)
            if(num_in_float2-num_in_float!=0):
                solution=solution+'\n'+latex('='+mod(eval(question[0]),2))+br

    solution = solution+'\n'+f'Hence, the correct option is {correct_option}.'
    return solution


def Main_function():
    changequestion()
    question = getQuestion()
    correct_op,wrong_op = make_options()
    wrong_op1, wrong_op2, wrong_op3 = wrong_op[0:]
    solution = getsol()

    database_dict = database_fn( 
	    Question_Type='text',
	    Answer_Type='text',
	    Topic_Number='030302',
	    Variation='v1',
	    Question=question,
	    Correct_Answer_1=correct_op,
	    Wrong_Answer_1=wrong_op1,
	    Wrong_Answer_2=wrong_op2,
	    Wrong_Answer_3=wrong_op3,
        ContributorMail = '2019chinmay.thakur@ves.ac.in',
	    Solution_text = solution)
    return database_dict

putInCsv(
	Topic_Number='030302',
	Number_Of_Iterations=5,
	Main_Function = Main_function,
	Filename = "v1_1.py",
    Create_Textfile = True,
    Remove_Duplicates = True
)