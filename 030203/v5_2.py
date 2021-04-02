from PIL import Image,ImageDraw, ImageFont
import random
from os import path
from coep_package.latex import latex,to_frac,superscript
from coep_package.csv import putInCsv, database_fn

given_term,pi,multiple_q = '','\pi ',''
a,circum,image_no = 0,0,1

def generate_image():
    global image_no
    margin, multiple = 50, 50
    width = margin*2 + multiple*(a)
    height = multiple*(a) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    a_start_cordinate = (margin,margin)
    a_end_cordinate = (margin + a*multiple, margin + a*multiple)
    draw.text((margin + (a_end_cordinate[0] - margin)//2- 25, a_end_cordinate[1] + 50),"Fig. A", font=ImageFont.truetype("arial.ttf", size=20), fill="black")
    multi=multiple_q
    if(multiple_q[0]=='1'):
        multi=multiple_q[1:]

    #For circle
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.ellipse([(a_start_cordinate[0]+((a/2)*multiple)-2,a_start_cordinate[1]+((a/2)*multiple)-2), (a_end_cordinate[0]-((a/2)*multiple)+2,a_end_cordinate[1]-((a/2)*multiple)+2)], fill="black", outline="black", width=1)
    if(given_term=="radius"):
        relation='r=x'+multi
        draw.line([(a_start_cordinate[0]+(a/2)*multiple , a_start_cordinate[1]+(a/2)*multiple), (a_start_cordinate[0]+a*multiple , a_start_cordinate[1]+(a/2)*multiple)], fill="black", width=1)
        draw.text([a_start_cordinate[0]+((3*a)/4)*multiple-25, a_start_cordinate[1]+(a/2)*multiple], f"{relation}", font=ImageFont.truetype("arial.ttf", size=20), fill="black")
    elif(given_term=="diameter"):
        relation='d=x'+multi
        draw.line([(a_start_cordinate[0] , a_start_cordinate[1]+(a/2)*multiple), (a_start_cordinate[0]+a*multiple , a_start_cordinate[1]+(a/2)*multiple)], fill="black", width=1)
        draw.text([a_start_cordinate[0]+((3*a)/4)*multiple-25, a_start_cordinate[1]+(a/2)*multiple], f"{relation}", font=ImageFont.truetype("arial.ttf", size=20), fill="black")

    relation = relation.replace('/','-').replace('=','_')
    image_temp_name="030203_CCV_"+relation[0]+'_'+str(circum)+relation[1:]
    image_name=image_temp_name+'.png'
    img.save('images/'+image_name, format="PNG")
    return image_name

def divider(num1,num2):
    floati = num1/num2
    inti = int(floati)
    if(inti-floati==0):
        return inti
    return round(floati,2)

def multiplier(num1,num2):
    floati = num1*num2
    inti = int (floati)
    if(inti-floati==0):
        return inti
    return round(floati,2)

def make_options():
    value=int(a)
    r=int(value/2)
    multi=eval(multiple_q)
    if(given_term=="radius"):
        return [latex(divider(r,multi)),latex(r),latex(multiplier(r,multi)),latex(value-1)]
    elif(given_term=="diameter") :
        return [latex(divider(value,multi)),latex(value),latex(multiplier(value,multi)),latex(r+1)]


def options(correct_option, answer_set ):
    wrong_options = answer_set[1:]
    random.shuffle(wrong_options)
    for i in range(1,5):
        if i == correct_option:
            print( str(i) + (f".  {answer_set[0]}"))
        else:
            print( str(i) + (f".  {wrong_options.pop()}"))

def getSolution(answer):
    r=circum/3.14
    if(given_term=="diameter"):
        d=2*r
        return f"""\n--------------------------------------SOLUTION-------------------------------------------
                The circumfernece of circle is given as {latex(circum)}.
                Formula of Circumference = {latex('2'+pi+'r')}.
                                       {latex('r')} ={latex(to_frac(circum,'2'+pi))}
                    Therefore, {latex('r')}={latex(r)}\n
                Now for {latex('x')},
                               {latex('x')}={latex(to_frac('d',multiple_q))}
                           {latex('d=2*r')}={latex(d)}
                     Therefore,{latex('x')}={answer}"""
                    
    elif(given_term=="radius"):
        return f"""\n--------------------------------------SOLUTION-------------------------------------------
                The circumfernece of circle is given as {latex(circum)}.
                Formula of Circumference = {latex('2'+pi+'r')}.
                                       {latex('r')} ={latex(to_frac(circum,'2'+pi))}
                    Therefore, {latex('r')}={latex(r)}\n
                Now for {latex('x')}, 
                               {latex('x')}={latex(to_frac('r',multiple_q))}
                     Therefore,{latex('x')}={answer}"""

def getQuestion():
    return f"Find the value of {latex('x')} if the circumference of the circle is {latex(circum)}?"

def changequestion():
    global given_term,a,circum,multiple_q
    q_on = ("radius","diameter")
    given_term = random.choice(q_on)
    multiples = ['5','4','3','2','1/2','1/3','1/4','1/5']
    multiple_q = random.choice(multiples)
    a = random.randint(2, 5)*2
    circum = round(3.14*a,2)

def Main_function():
    changequestion()
    question = getQuestion()
    option_set = make_options()
    correct_op = option_set[0]
    wrong_op = option_set[1:]
    random.shuffle(wrong_op)
    wrong_op1, wrong_op2, wrong_op3 = wrong_op[0:]
    imagepath=generate_image()
    solution = getSolution(option_set[0])

    database_dict = database_fn(
	    Question_Type='image',
	    Answer_Type='text',
	    Topic_Number='030203',
	    Variation='v5',
	    Question=question,
	    Correct_Answer_1=correct_op,
	    Wrong_Answer_1=wrong_op1,
	    Wrong_Answer_2=wrong_op2,
	    Wrong_Answer_3=wrong_op3,
        Question_IAV=imagepath,
        ContributorMail = '2019chinmay.thakur@ves.ac.in',
	    Solution_text = solution)
    return database_dict

putInCsv(
	Topic_Number='030203',
	Number_Of_Iterations=5,
	Main_Function = Main_function,
	Filename="v5_2.py"
)