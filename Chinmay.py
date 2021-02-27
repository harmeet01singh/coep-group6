from PIL import Image,ImageDraw, ImageFont
import random

def generate_image( a, b):
    margin, multiple = 50, 50
    width = margin*3 + multiple*(a+b)
    height = multiple*(a if a > b else b) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    if(a>b):
        a_start_cordinate = (margin,margin)
        a_end_cordinate = (margin + a*multiple, margin + a*multiple)
        b_start_cordinate = (2*margin + a*multiple , margin+((a-b)/2)*multiple)
        b_end_cordinate = (2*margin + a*multiple + b*multiple, b_start_cordinate[1] + b*multiple)
        draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, a_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    else:
        b_start_cordinate = (2*margin + a*multiple , margin)
        b_end_cordinate = (2*margin + a*multiple + b*multiple, margin + b*multiple)
        a_start_cordinate = (margin,margin+((b-a)/2)*multiple)
        a_end_cordinate = (margin + a*multiple, a_start_cordinate[1] + a*multiple)
        draw.text((margin + (a_end_cordinate[0] - margin)//2, b_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    
    #For A circle
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    """ for i in range(1,a):
        draw.ellipse([(a_start_cordinate[0]+(i*multiple),a_start_cordinate[1]+(i*multiple)), (a_end_cordinate[0]-(i*multiple),a_end_cordinate[1]-(i*multiple))], fill="red", outline="black", width=1) """
    
    #For B circle
    draw.ellipse([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    """ for i in range(1,b):
        draw.ellipse([(b_start_cordinate[0]+(i*multiple),b_start_cordinate[1]+(i*multiple)), (b_end_cordinate[0]-(i*multiple),b_end_cordinate[1]-(i*multiple))], fill="green", outline="black", width=1) """

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
    print(f"Here we have A as a circle of diameter {a} and B as a circle of diameter {b}. Since they are {is_equal}, the correct answer is {answer}.")

print("Whether A and B are identical: A = B?")
a, b = ( random.randint(2, 5)*2, random.randint(2, 5)*2)
generate_image( a, b)
correct_option = random.randint(1, 4)
options(correct_option, a, b)
selcted_option = int(input("Select one option: "))
if selcted_option == correct_option:
    print("You have selected the right option!")
else:
    print("You have selected the wrong option!")
sol( a, b)