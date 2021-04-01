from PIL import Image, ImageDraw, ImageFont
import random


def generate_image():
    width = 500
    height = 500
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    size, generator1 = selectTriangle1()
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=(255, 0, 0), outline='black')
    draw.text((150, 425), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    size, generator2 = selectTriangle2()
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill='yellow', outline='black')
    draw.text((350, 425), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    img.show()
    if generator1 == generator2:
        return True
    else:
        return False


def selectTriangle1():
    equilateral1 = [150, 70, 100, 300, 200, 300]
    equilateral2 = [100, 70, 150, 300, 200, 70]

    normal1 = [175, 70, 75, 250, 225, 250]
    normal2 = [75, 70, 175, 250, 225, 70]

    rightAngled1 = [60, 70, 60, 300, 175, 300]
    rightAngled2 = [175, 70, 60, 300, 175, 300]
    rightAngled3 = [60, 70, 175, 300, 175, 70]
    rightAngled4 = [60, 70, 60, 300, 175, 70]

    triangleSelector = random.randint(1, 8)

    if triangleSelector == 1:
        return equilateral1, triangleSelector
    elif triangleSelector == 2:
        return equilateral2, triangleSelector
    elif triangleSelector == 3:
        return normal1, triangleSelector
    elif triangleSelector == 4:
        return normal2, triangleSelector
    elif triangleSelector == 5:
        return rightAngled1, triangleSelector
    elif triangleSelector == 6:
        return rightAngled2, triangleSelector
    elif triangleSelector == 7:
        return rightAngled3, triangleSelector
    elif triangleSelector == 8:
        return rightAngled4, triangleSelector


def selectTriangle2():
    equilateral1 = [350, 70, 300, 300, 400, 300]
    equilateral2 = [300, 70, 350, 300, 400, 70]

    normal1 = [375, 70, 275, 250, 425, 250]
    normal2 = [275, 70, 375, 250, 425, 70]

    rightAngled1 = [260, 70, 260, 300, 375, 300]
    rightAngled2 = [375, 70, 260, 300, 375, 300]
    rightAngled3 = [260, 70, 375, 300, 375, 70]
    rightAngled4 = [260, 70, 260, 300, 375, 70]

    triangleSelector = random.randint(1, 8)

    if triangleSelector == 1:
        return equilateral1, triangleSelector
    elif triangleSelector == 2:
        return equilateral2, triangleSelector
    elif triangleSelector == 3:
        return normal1, triangleSelector
    elif triangleSelector == 4:
        return normal2, triangleSelector
    elif triangleSelector == 5:
        return rightAngled1, triangleSelector
    elif triangleSelector == 6:
        return rightAngled2, triangleSelector
    elif triangleSelector == 7:
        return rightAngled3, triangleSelector
    elif triangleSelector == 8:
        return rightAngled4, triangleSelector


def options(correctAns):
    allOptions = ['Yes', 'No', 'Maybe', "Can't Tell"]
    random.shuffle(allOptions)
    correctIndex = None
    if correctAns:
        correctIndex = allOptions.index('Yes')
    else:
        correctIndex = allOptions.index('No')

    for i in range(1, 5):
        print(f'{i}. {allOptions[i - 1]}')

    return correctIndex + 1


def solution(correctAns):
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    equal = "Yes" if correctAns is True else "No"


correctAns = generate_image()
correctOption = options(correctAns)
selectedOption = int(input("Select the correct option : "))
if selectedOption == correctOption:
    print("You have selected the right option!")
else:
    print("You have selected the wrong option!")
solution(correctAns)