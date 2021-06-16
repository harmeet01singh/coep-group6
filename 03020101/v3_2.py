from PIL import Image,ImageDraw, ImageFont
import random
from coep_package.latex import latex,to_frac,superscript
from coep_package.csv import putInCsv, database_fn

given_term,pi= "",'\pi '
a = 0

def generate_image(relation):
    global image_no
    margin, multiple = 50, 50
    width = margin*2 + multiple*(a)
    height = multiple*(a) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    a_start_cordinate = (margin,margin)
    a_end_cordinate = (margin + a*multiple, margin + a*multiple)
    draw.text((margin + (a_end_cordinate[0] - margin)//2- 25, a_end_cordinate[1] + 50),"Fig. A", font=ImageFont.truetype("arial.ttf", size=20), fill="black")

    #For circle
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.ellipse([(a_start_cordinate[0]+((a/2)*multiple)-2,a_start_cordinate[1]+((a/2)*multiple)-2), (a_end_cordinate[0]-((a/2)*multiple)+2,a_end_cordinate[1]-((a/2)*multiple)+2)], fill="black", outline="black", width=1)
    if(given_term=="radius"):
        draw.line([(a_start_cordinate[0]+(a/2)*multiple , a_start_cordinate[1]+(a/2)*multiple), (a_start_cordinate[0]+a*multiple , a_start_cordinate[1]+(a/2)*multiple)], fill="black", width=1)
    elif(given_term=="diameter"):
        draw.line([(a_start_cordinate[0] , a_start_cordinate[1]+(a/2)*multiple), (a_start_cordinate[0]+a*multiple , a_start_cordinate[1]+(a/2)*multiple)], fill="black", width=1)

    draw.text([a_start_cordinate[0]+((3*a)/4)*multiple-25, a_start_cordinate[1]+(a/2)*multiple], f"{relation}", font=ImageFont.truetype("arial.ttf", size=20), fill="black")
    
    relation = relation.replace('/','-').replace('=','_').replace('\u03C0','(pi)')
    image_temp_name="03020101_CCX_"+relation
    image_name=image_temp_name+'.png'
    img.save('images/'+image_name, format="PNG")
    return image_name

def options(correct_option, answer_set ):
    wrong_options = answer_set[1:]
    random.shuffle(wrong_options)
    for i in range(1,5):
        if i == correct_option:
            print( str(i) + (". " + answer_set[0]))
        else:
            print( str(i) + ". " + wrong_options.pop())

def set_of_questions(given):
    #Sets where radius is given
    radius_subset1 = ["r=2x",latex("r=2x"),latex('4'+pi+'x'),latex('2'+pi+'x'),latex(pi+'x'),latex(to_frac(pi+'x',2))]
    radius_subset2 = ["r=x/2",latex("r="+to_frac('x',2)),latex(pi+'x'),latex(to_frac(pi+'x',2)),latex('2'+pi+'x'),latex(to_frac(pi+'x',4))]
    radius_subset3 = ["r=\u03C0x",latex("r="+pi+"x"),latex('2'+superscript(pi,2)+'x'),latex(superscript(f'({pi}x)',2)),latex(pi+'x'),latex('x')]
    radius_subset4 = ["r=x/\u03C0",latex("r="+to_frac('x',pi)),latex('2x'),latex(to_frac('2x',pi)),latex(superscript(pi,2)+'x'),latex('x')]
    radius_subset5 = ["r=3x",latex("r=3x"),latex('6'+pi+'x'),latex(to_frac('2'+pi+'x',3)),latex('9'+pi+'x'),latex(to_frac(pi+'x',3))]
    radius_subset6 = ["r=4x",latex("r=4x"),latex('8'+pi+'x'),latex(to_frac(pi+'x',2)),latex('16'+pi+'x'),latex(to_frac(pi+'x',4))]
    radius_subset7 = ["r=5x",latex("r=5x"),latex('10'+pi+'x'),latex(to_frac('2'+pi+'x',5)),latex('25'+pi+'x'),latex(to_frac(pi+'x',5))]
    radius_subset8 = ["r=x/3",latex("r="+to_frac('x',3)),latex(to_frac('2'+pi+'x',3)),latex('6'+pi+'x'),latex('3'+pi+'x'),latex(to_frac(pi+'x',3))]
    radius_subset9 = ["r=x/4",latex("r="+to_frac('x',4)),latex(to_frac(pi+'x',2)),latex('8'+pi+'x'),latex('4'+pi+'x'),latex(to_frac(pi+'x',4))]
    radius_subset10 = ["r=x/5",latex("r="+to_frac('x',5)),latex(to_frac('2'+pi+'x',5)),latex('10'+pi+'x'),latex('5'+pi+'x'),latex(to_frac(pi+'x',5))]

    #Sets where diameter is given
    diameter_subset1 = ["d=2x",latex("d=2x"),latex('2'+pi+'x'),latex('4'+pi+'x'),latex(to_frac(pi+'x',2)),latex(pi+'x')]
    diameter_subset2 = ["d=x",latex("d=x"),latex(pi+'x'),latex('2'+pi+'x'),latex(to_frac(pi+'x',2)),latex('4'+pi+'x')]
    diameter_subset3 = ["d=2\u03C0x",latex("d=2"+pi+"x"),latex('2'+superscript(pi,2)+'x'),latex(superscript(f'({pi}x)',2)),latex(pi+'x'),latex('4'+superscript(pi,2)+'x')]
    diameter_subset4 = ["d=2x/\u03C0",latex("d="+to_frac('2x',pi)),latex('2x'),latex(to_frac('2x',pi)),latex('4x'),latex('2'+pi+'x')]
    diameter_subset5 = ["d=4x",latex("d=4x"),latex('4'+pi+'x'),latex('2'+pi+'x'),latex(pi+'x'),latex(to_frac(pi+'x',2))]
    diameter_subset6 = ["d=6x",latex("d=6x"),latex('6'+pi+'x'),latex(to_frac('2'+pi+'x',3)),latex('9'+pi+'x'),latex(to_frac(pi+'x',3))]
    diameter_subset7 = ["d=8x",latex("d=8x"),latex('8'+pi+'x'),latex(to_frac(pi+'x',2)),latex('16'+pi+'x'),latex(to_frac(pi+'x',4))]
    diameter_subset8 = ["d=x/2",latex("d="+to_frac('x',2)),latex(to_frac(pi+'x',2)),latex('8'+pi+'x'),latex('4'+pi+'x'),latex(to_frac(pi+'x',4))]
    diameter_subset9 = ["d=x/3",latex("d="+to_frac('x',3)),latex(to_frac(pi+'x',3)),latex('12'+pi+'x'),latex('3'+pi+'x'),latex(to_frac(pi+'x',6))]
    diameter_subset10 = ["d=x/4",latex("d="+to_frac('x',4)),latex(to_frac(pi+'x',4)),latex('16'+pi+'x'),latex('4'+pi+'x'),latex(to_frac(pi+'x',8))]

    radius_set= [radius_subset1 , radius_subset2 , radius_subset3 , radius_subset4,radius_subset5,radius_subset6,radius_subset7,radius_subset8,radius_subset9,radius_subset10]
    diameter_set = [diameter_subset1 , diameter_subset2 , diameter_subset3 , diameter_subset4,diameter_subset5,diameter_subset6,diameter_subset7,diameter_subset8,diameter_subset9,diameter_subset10]

    if(given=="radius"):
        return random.choice(radius_set)
    elif(given=="diameter"):
        return random.choice(diameter_set)

def getSolution(relation , answer):
    if(given_term=="diameter"):
        return f"""\n--------------------------------------SOLUTION-------------------------------------------
                Here {given_term} of the circle is given as {relation}.
                Formula of Circumference = {latex('2'+pi+'r')}.
                \n               {latex('r='+to_frac('d',2))}
                Therefore, Circumference = {latex(pi+'d')}.
                \nSubstitute {relation} in the formula .
                Therefore,
                           Circumference = {answer} ."""
    elif(given_term=="radius"):
        return f"""\n--------------------------------------SOLUTION-------------------------------------------
                Here {given_term} of the circle is given as {relation}.
                Formula of Circumference = {latex('2'+pi+'r')}..
                \nSubstitute {relation} in the formula .
                Therefore,
                           Circumference = {answer} ."""

def getQuestion():
    return f"For the given {given_term} what is the circumference of the circle in terms of {latex('x')} ?"

def changequestion():
    global given_term,a
    q_on = ("radius","diameter")
    given_term = random.choice(q_on)
    a = random.randint(2, 5)*2

def Main_function():
    changequestion()
    question = getQuestion()
    question_set = set_of_questions(given_term)
    correct_op = question_set[2]
    wrong_op = question_set[3:]
    random.shuffle(wrong_op)
    wrong_op1, wrong_op2, wrong_op3 = wrong_op[0:]
    imagepath=generate_image(question_set[0])
    solution = getSolution(question_set[1],question_set[2])

    database_dict = database_fn(
        Question_Type='image',
	    Answer_Type='text',
	    Topic_Number='03020101',
	    Variation='v3',
	    Question=question,
	    Correct_Answer_1=correct_op,
	    Wrong_Answer_1=wrong_op1,
	    Wrong_Answer_2=wrong_op2,
	    Wrong_Answer_3=wrong_op3,
        Question_IAV=imagepath,
        ContributorMail = '2019chinmay.thakur@ves.ac.in', 
	    Solution_text=solution)
    return database_dict

putInCsv(
	Topic_Number='03020101',
	Number_Of_Iterations=5,
	Main_Function = Main_function,
	Filename="v3_2.py"
)