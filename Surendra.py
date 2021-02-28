from PIL import Image, ImageDraw, ImageFont
import random

margin, multiple = 50, 50
width = 800
height = 600


def generate_image_square1(a):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a * multiple, margin + a * multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img


def generate_image_square2(img, b):
    draw = ImageDraw.Draw(img)

    # For B matrix
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b * multiple, margin + b * multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2, b_end_cordinate[1] + 50), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.show()


def generate_image_rectangle1(l1, b1):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + b1 * multiple, margin + l1 * multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate],
                   fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50),
              "A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img


def generate_image_rectangle2(img, l2, b2):
    draw = ImageDraw.Draw(img)

    # For B Matrx
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b2 * multiple, margin + l2 * multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate],
                   fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2,
               b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.show()


def generate_image_circle1(a):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A circle
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a * multiple, margin + a * multiple)
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img


def generate_image_circle2(img, b):
    draw = ImageDraw.Draw(img)

    # For B circle
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b * multiple, margin + b * multiple)
    draw.ellipse([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2, b_end_cordinate[1] + 50), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.show()


def generate_image_triangle1(triangle):
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # for A triangle
    size = triangle
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill="red", outline="black")
    draw.text((175, 400), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img


def generate_image_triangle2(img, triangle):
    draw = ImageDraw.Draw(img)

    # for B triangle
    size = triangle
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1 + 400, y1), (x2 + 400, y2), (x3 + 400, y3)], fill="green", outline="black")
    draw.text((575, 400), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.show()


def options(correct_option, x, y):
    wrong_options = ["No" if x == y else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    for i in range(1, 5):
        if i == correct_option:
            print(str(i) + (". Yes" if x == y else ". No"))
        else:
            print(str(i) + ". " + wrong_options.pop())


def sol(x, y):
    shape = "equal" if x == y else "different"
    answer = "Yes" if x == y else "No"
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    print(
        f"Since they are {shape} shapes, the correct answer is {answer}.")


print("Whether A and B are identical: A = B?")
x, y = (random.randint(1, 4), random.randint(1, 4))

if x == 1:
    img = generate_image_square1(5)
elif x == 2:
    img = generate_image_rectangle1(8, 5)
elif x == 3:
    img = generate_image_circle1(6)
else:
    triangle = [175, 50, 50, 300, 300, 300]
    img = generate_image_triangle1(triangle)
if y == 1:
    generate_image_square2(img, 5)
elif y == 2:
    generate_image_rectangle2(img, 8, 5)
elif y == 3:
    generate_image_circle2(img, 6)
else:
    triangle = [175, 50, 50, 300, 300, 300]
    generate_image_triangle2(img, triangle)

correct_option = random.randint(1, 4)
options(correct_option, x, y)

selcted_option = int(input("Select one option: "))
if selcted_option == correct_option:
    print("You have selected the right option!")
else:
    print("You have selected the wrong option!")

sol(x, y)
