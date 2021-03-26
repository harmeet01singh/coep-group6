from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import putInCsv, database_fn

i = 0

def generate_image(l1, b1):
    global image_name
    margin, multiple = 50, 50
    width = margin*3 + multiple*(b1)
    height = multiple*(l1) + margin*3
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + b1*multiple, margin + l1*multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate],
                   fill="red", outline="black", width=1)
    
    draw.text((margin + a_end_cordinate[0],margin + (a_end_cordinate[1] - margin)//2),
              str(l1), font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    
    draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),
              "x", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    # Display Image
    image_temp_name="rectangle_area_variable"
    image_name = image_temp_name + str(i)+'.png'
    img.save(image_name, format="PNG")
    img.show() 
     
def options(correctAns,l1,b1):
    allOptions = []
    
    allOptions.append(correctAns)
    secondOption = latex("x" + "-" + str(l1))
    thirdOption = latex(str(l1) + "+" + "x")
    fourthOption = latex("x" + "/" + str(l1))

    # Appending Other Options
    allOptions.append(secondOption)
    allOptions.append(thirdOption)
    allOptions.append(fourthOption)
    
    # Shuffling Options
    random.shuffle(allOptions)
    correctIndex = None
    wrong_options = []
    correct_option = []
    
    # Getting Index of Correct Option 
    for i in range(1, 5):
        if allOptions[i-1] == correctAns:
            correctIndex = i
            correct_option.append(allOptions[i-1])
        else:
            wrong_options.append(allOptions[i-1])
        print(f'{i}. {allOptions[i - 1]}')

    return correctIndex,correct_option,wrong_options


def solution(correctAns, correctOption,l1,b1):
    return f'''\n--------------------------------------SOLUTION------------------------------------------- => Area of Rectangle = length * breadth => {latex(l1)}*x => {latex(correctAns)} => ThereFore Option {latex(correctOption)} is right selection'''
            
        
def getQuestion():
    return "Q) What will be the area of given rectangle ?"      

def changeValues():
    global correctAnswer, wrong_Options, soln_print, i
    
    # Getting random value oflength and breadth
    l1 = random.randint(3, 6)
    b1 = random.randint(5, 10) 
    area = latex(str(l1)+"x")
    i +=1
    return l1,b1,area
    
def getCorrectOption(correctAns):
    return correctAns

def getWrongOptions(wrong_Options):
    return wrong_Options
 
def main_function():
    l1,b1,area = changeValues()
    Question = getQuestion()
    print(Question)
    correctAns,correct_option,wrong_Options = options(area,l1,b1)
    generate_image(l1, b1)
    selected_option = int(input("Select one option: "))
    if selected_option == correctAns:
        print("You have selected the right option!")
    else:
        print("You have selected the wrong option!")
    Solution = solution(area,correctAns,l1,b1)
    print(Solution)
    
    database_dict= database_fn(
        Question_Type='image',
	    Answer_Type='text',
	    Topic_Number='03020101',
	    Variation='v1',
	    Question=Question,
        Correct_Answer_1=correct_option[0],
        Wrong_Answer_1=wrong_Options[0],
        Wrong_Answer_2=wrong_Options[1],
        Wrong_Answer_3=wrong_Options[2],
        Question_IAV=image_name,
        ContributorMail = '2019mangesh.sokalwar@ves.ac.in',
        Solution_text=Solution
    )
    return database_dict
    
    
#if you want N questions in your csv file pass N as the value for Number of Iteraions
putInCsv(
    Topic_Number='03020101',
    Number_Of_Iterations=5,
    Main_Function=main_function,
    Filename='rectangle_area_variable.py'
)
 


    