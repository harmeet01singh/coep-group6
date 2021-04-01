from PIL import Image, ImageDraw, ImageFont
import random


def generate_image(l1, b1, l2, b2):
    margin, multiple = 50, 50
    width = margin*3 + multiple*(b1+b2)
    height = multiple*(l1 if l1 > l2 else l2) + margin*3
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    #For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + b1*multiple, margin + l1*multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate],
                   fill="red", outline="black", width=1)
    for i in range(1, b1):
        draw.line([margin + i*multiple, margin, margin + i*multiple,
                   margin + l1*multiple], fill="black", width=1)  # Vertical Lines
    for i in range(1, l1):
        draw.line([margin, margin + i*multiple, margin + b1*multiple,
                   margin + i*multiple], fill="black", width=1)  # Horizontal Lines
    draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),
              "A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # For B Matrx
    b_start_cordinate = (2*margin + b1*multiple, margin)
    b_end_cordinate = (2*margin + b1*multiple + b2 *
                       multiple, margin + l2*multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate],
                   fill="green", outline="black", width=1)
    for i in range(1, b2):
        draw.line([b_start_cordinate[0] + i*multiple, margin, b_start_cordinate[0] +
                   i*multiple, margin + l2*multiple], fill="black", width=1)  # Vertical Lines
    for i in range(1, l2):
        draw.line([b_start_cordinate[0], b_start_cordinate[1] + i*multiple, b_end_cordinate[0],
                   b_start_cordinate[1] + i*multiple], fill="black", width=1)  # Horizontal Lines
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2,
               b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.show()
    

def options(correct_option,l1, b1, l2, b2):
    wrong_options = ["No" if l1 == l2 and b1 == b2 else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    for i in range(1, 5):
        if i == correct_option:
            print(str(i) + (". Yes" if l1 == l2 and b1 == b2 else ". No"))
        else:
            print(str(i) + ". " + wrong_options.pop())


def sol(l1,b1,l2,b2):
    is_equal = "equal" if l1 == l2 and b1 == b2 else "not equal"
    answer = "Yes" if  l1 == l2 and b1 == b2 else "No"
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    print(
        f"Here we have A as a matrix of {l1}x{b1} and B as a matrix of {l2}x{b2}. Since they are {is_equal}, the correct answer is {answer}.")


print("Whether A and B are identical: A = B?")
l1 = random.randint(3, 10)
b1 = random.randint(3, 10)
l2 = random.randint(3, 10)
b2 = random.randint(3, 10)
# l1,b1,l2,b2
generate_image(l1, b1, l2, b2)
correct_option = random.randint(1, 4)
options(correct_option, l1, b1, l2, b2)
selcted_option = int(input("Select one option: "))
if selcted_option == correct_option:
    print("You have selected the right option!")
else:
    print("You have selected the wrong option!")
sol(l1, b1, l2, b2)
