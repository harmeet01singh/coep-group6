from PIL import Image,ImageDraw, ImageFont
import random

def generate_image( a, b):
    margin, multiple = 50, 50
    width = margin*3 + multiple*(a+b)
    height = multiple*(a if a > b else b) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    #For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a*multiple, margin + a*multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    for i in range(1,a):
        draw.line([margin + i*multiple , margin, margin + i*multiple , margin + a*multiple], fill="black", width=1)     #Vertical Lines
        draw.line([margin , margin + i*multiple, margin + a*multiple , margin + i*multiple], fill="black", width=1)     #Horizontal Lines
    draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    
    #For B matrix
    b_start_cordinate = (2*margin + a*multiple , margin)
    b_end_cordinate = (2*margin + a*multiple + b*multiple, margin + b*multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    for i in range(1,b):
        draw.line([b_start_cordinate[0] + i*multiple , margin, b_start_cordinate[0]+ i*multiple , margin + b*multiple], fill="black", width=1)      #Vertical Lines
        draw.line([b_start_cordinate[0] , b_start_cordinate[1] + i*multiple, b_end_cordinate[0] , b_start_cordinate[1] + i*multiple], fill="black", width=1)     #Horizontal Lines
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    #Display Image
    img.show()
    # img.save("shape.png", format="PNG")

def options(correct_option, a, b):
    wrong_options = ["No" if a==b else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    for i in range(1,5):
        if i == correct_option:
            print( str(i) + (". Yes" if a == b else ". No"))
        else:
            print( str(i) + ". " + wrong_options.pop())

def sol(a, b):
    is_equal = "equal" if a == b else "not equal"
    answer = "Yes" if a == b else "No"
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    print(f"Here we have A as a matrix of {a}x{a} and B as a matrix of {b}x{b}. Since they are {is_equal}, the correct answer is {answer}.")

print("Whether A and B are identical: A = B?")
a, b = ( random.randint(3, 10), random.randint(3, 10))
generate_image( a, b)
correct_option = random.randint(1, 4)
options(correct_option, a, b)
selcted_option = int(input("Select one option: "))
if selcted_option == correct_option:
    print("You have selected the right option!")
else:
    print("You have selected the wrong option!")
sol( a, b)