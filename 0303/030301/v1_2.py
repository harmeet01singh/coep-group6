import random
import math
import os
from coep_package.latex import latex
from coep_package.csv_module import putInCsv, database_fn



def getQuestion(expression):
    return f"Q)Simplify the following expression by applying the BODMAS rule : {expression}"

def solution(first_operator,second_operator,correctAns,p,q,r,s,t):
    return f'''\n--------------------------------------SOLUTION-------------------------------------------
As per the BODMAS rule:
Rule 1 - B : First solve the brackets,hence the expression becomes {latex("(" +str(q+r-s)+")")}
Rule 2 - DM: If more than one operation is to be carried out, then multiplication and division are carried out first,
             in the order in which they occur from left to right,hence the expression becomes {latex("("+str(p)+ second_operator +str(q+r-s)+")")}
Rule 3 - AS: After that, addition and subtraction are carried out in the order in which they occur from left to right,
             hence the expression becomes {latex("["+"("+str(p)+ second_operator +str(q+r-s)+")"+ first_operator + str(t)+"]")}
Therefore option {latex(correctAns)} is right selection
  '''

def options(other_operators, operators,second_operator,first_operator,correctAns,p,q,r,s,t):
    allOptions = []
    
    allOptions.append(correctAns)
    secondOption = latex("["+"("+str(p)+second_operator+str(q+r-s+t)+")"+"]")
    thirdOption = latex("["+str(q+r-s)+second_operator+"("+str(p)+first_operator+str(t)+")"+"]")
    fourthOption =  latex("["+"("+str(p)+ other_operators+str(t)+")"+second_operator+str(q+r-s)+"]")

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

def getCorrectOption(correctAns):
    return correctAns

def getWrongOptions(wrong_Options):
    return wrong_Options

   

def main_function():
    p = random.randint(30, 100)
    q = random.randint(10, 100) 
    r = random.randint(3, 10)
    s = random.randint(5, 20)
    t = random.randint(30, 70)

    operators = ["+","-"]
    first_operator = random.choice(operators)
    operators.remove(first_operator)
    other_operators = [latex("\\times"),latex("\\div")]
    second_operator = random.choice(other_operators)
    other_operators.remove(second_operator)

    expression = latex(str(p)+second_operator + "(" +str(q)+ operators[0] +str(r) + first_operator+str(s)+")"+ first_operator +str(t))
    correctAns = latex("["+"("+str(p)+ second_operator +str(q+r-s)+")"+ first_operator + str(t)+"]")
    
    Question = getQuestion(expression)
    print(Question)
    correctAns,correct_option,wrong_Options = options(other_operators[0],operators[0] ,second_operator,first_operator,correctAns,p,q,r,s,t)
    selected_option = int(input("Select one option: "))
    if selected_option == correctAns:
        print("You have selected the right option!")
    else:
        print("You have selected the wrong option!")
    Solution = solution(first_operator,second_operator,correctAns,p,q,r,s,t)
    print(solution(first_operator,second_operator,correctAns,p,q,r,s,t))
    
    database_dict= database_fn(
        Question_Type='text',
	    Answer_Type='text',
	    Topic_Number='030301',
	    Variation='v1',
	    Question=Question,
        Correct_Answer_1=correct_option[0],
        Wrong_Answer_1=wrong_Options[0],
        Wrong_Answer_2=wrong_Options[1],
        Wrong_Answer_3=wrong_Options[2],
        ContributorMail = '2019mangesh.sokalwar@ves.ac.in',
        Solution_text=Solution
    )
    return database_dict

putInCsv(
    Topic_Number='030301',
    Number_Of_Iterations=5,
    Main_Function=main_function,
    Filename='v1_2.py',
     Create_Textfile = True,
    Remove_Duplicates = True
)

