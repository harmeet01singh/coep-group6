import os
from PIL import Image, ImageDraw, ImageFont
import random
import math
import string
from coep_package.latex import latex
from coep_package.csv import putInCsv, database_fn

variables = "abcmnpqxyz"

correctAnswer = 0
wrong_Options = []
soln_print = ""
i = 1

def generate_image():
    width = 500
    height = 500
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    x1, y1, x2, y2, x3, y3, text = triangleGenerate()

    random_edge_selection = random.randint(1, 3)

    distance1 = None
    distance2 = None
    distance3 = None
    ans_distance = None
    perimeter_ans = None

    answerList = []

    variable = variables[random.randint(0, len(variables)-1)]

    if random_edge_selection == 1:
        distance2 = round(math.dist([x2, y2], [x3, y3])/3)
        distance3 = round(math.dist([x1, y1], [x3, y3])/3)
        perimeter_ans = str(distance2 + distance3) + " + " + variable
        answerList.append(distance2)
        answerList.append(distance3)

    elif random_edge_selection == 2:
        distance1 = round(math.dist([x1, y1], [x2, y2])/3)
        distance3 = round(math.dist([x1, y1], [x3, y3])/3)
        perimeter_ans = str(distance1 + distance3) + " + " + variable
        answerList.append(distance1)
        answerList.append(distance3)
    else:
        distance1 = round(math.dist([x1, y1], [x2, y2])/3)
        distance2 = round(math.dist([x1, y1], [x2, y2])/3)
        perimeter_ans = str(distance1 + distance2) + " + " + variable
        answerList.append(distance1)
        answerList.append(distance2)

    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=(255, 0, 0), outline='black')

    if random_edge_selection == 1:
        draw.text((text[0], text[1]), f"{distance3}",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[2], text[3]), f"{variable}",
            font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[4], text[5]), f"{distance2}",
            font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    elif random_edge_selection == 2:
        draw.text((text[0], text[1]), f"{distance3}",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[2], text[3]), f"{distance1}",
        font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[4], text[5]), f"{variable}",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    else:
        draw.text((text[0], text[1]), f"{variable}",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[2], text[3]), f"{distance1}",
        font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((text[4], text[5]), f"{distance2}",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")


    image_name = f"03020101_TPV_{answerList[0]}_{answerList[1]}" + '.png'
    img.save('images/' + image_name, format="PNG")
    return perimeter_ans, answerList, variable, image_name

def triangleGenerate():
    x1 = random.randint(100, 300)
    y1 = random.randint(50, 150)

    x2 = random.randint(50, 200)
    y2 = random.randint(250, 400)

    x3 = random.randint(250, 400)
    y3 = random.randint(250, 400)

    text_side1x = None
    text_side2x = None
    text_side3x = None

    text_side1y = None
    text_side2y = None
    text_side3y = None

    text = []

    if x1 > x3:
        text_side3x = x1 + 10
        text_side3y = (y1 + y3) // 2
    else:
        text_side3x = x3 + 10
        text_side3y = (y1 + y3) // 2

    text.append(text_side3x)
    text.append(text_side3y)

    if x1 < x2:
        text_side1x = x1 - 10
        text_side1y = (y1 + y2) // 2
    else:
        text_side1x = x2 - 10
        text_side1y = (y1 + y2) // 2

    text.append(text_side1x)
    text.append(text_side1y)

    if y2 > y3:
        text_side2x = (x2 + x3) // 2
        text_side2y = y2 + 10
    else:
        text_side2x = (x2 + x3) // 2
        text_side2y = y3 + 10

    text.append(text_side2x)
    text.append(text_side2y)

    return x1, y1, x2, y2, x3, y3, text

def options(correctAns, distances):
    correctAns = latex(correctAns)
    allOptions = []
    allOptions.append(correctAns)

    value = correctAns.split(" + ")
    secondOption = (str(value[0]) + " - " + str(value[1]))
    thirdOption = (str('$') + str(distances[0])) + " + " + str(value[1])
    fourthOption = (str('$') + str(distances[1])) + " - " + str(value[1])

    allOptions.append(secondOption)
    allOptions.append(thirdOption)
    allOptions.append(fourthOption)
    random.shuffle(allOptions)
    correctIndex = None
    wrong_options = []

    for i in range(1, 5):
        if allOptions[i-1] == correctAns:
            correctIndex = i
        else:
            wrong_options.append(allOptions[i-1])

    return correctIndex, allOptions, wrong_options

def solution(correctAns, distances, correctOption):
    value = correctAns.split(" + ")
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    print(f"Formula of Perimeter = Sum of all sides of triangle")
    print(f"Therefore Sum of All Sides = {latex(distances[0])} + {latex(distances[1])} + {latex(value[1])}")
    ans = distances[0] + distances[1]
    print(f"Perimeter = {latex(ans)} + {latex(value[1])}")
    print(f'ThereFore Option {latex(correctOption)} is right selection')

    soln = "\n--------------------------------------SOLUTION-------------------------------------------\n" + f"Formula of Perimeter = Sum of all sides of triangle\n" + f"Therefore Sum of All Sides = {latex(distances[0])} + {latex(distances[1])} + {latex(value[1])}\n" + f"Perimeter = {latex(ans)} + {latex(value[1])}\n" + f'ThereFore Option {latex(correctOption)} is right selection'
    return soln


#this function generates question
def getQuestion(variable):
    return f"For given triangle, Find the perimeter of the triangle in terms of {latex(variable)}"

#ths function generates correct option
def getCorrOption():
    return correctAnswer

#this function generates wrong options
def getWrongOptions():
    return wrong_Options

#this function generates Solution
def getSolution(correctAns, distances, correctOption):
    value = correctAns.split(" + ")
    ans = distances[0] + distances[1]
    return f"\n--------------------------------------SOLUTION-------------------------------------------\nFormula of Perimeter = Sum of all sides of triangle\nTherefore Sum of All Sides = {latex(distances[0])} + {latex(distances[1])} + {latex(value[1])}\nPerimeter = {latex(ans)} + {latex(value[1])}\nThereFore Option {latex(correctOption)} is right selection"

def changeValues():
    global correctAnswer, wrong_Options, soln_print, i

    correctAnswer, answerList, variable, image_name = generate_image()
    correctIndex, allOptions, wrong_Options = options(correctAnswer, answerList)
    soln_print = getSolution(correctAnswer, answerList, correctIndex)
    correctAnswer = latex(correctAnswer)
    i+=1
    return variable, image_name


#When this main_function runs 1 time it creates one Question and its solution
def main_function():
    variable, image_path = changeValues()
    Question = getQuestion(variable)
    Corr_op = getCorrOption()
    wrong_op1,wrong_op2,wrong_op3 = getWrongOptions()
    Solution = soln_print


    #this database_fn
    #for understanding the parameters used refer to the DST_Lot_2 Excel sheet shared in the Readme file
    #all the attributes mentioned in DST_lot_2 file are implemented in this function.
    database_dict= database_fn(
        Question_Type='image',
        Answer_Type='1',
        Topic_Number='03020101',
        Variation='v3',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Question_IAV=image_path,
        ContributorMail = '2019yash.kumthekar@ves.ac.in', 
        Solution_text=Solution
    )
    return database_dict


#if you want N questions in your csv file pass N as the value for Number of Iteraions
putInCsv(
    Topic_Number='03020101',
    Number_Of_Iterations=5,
    Main_Function=main_function,
    Filename='v3_7.py'
)
