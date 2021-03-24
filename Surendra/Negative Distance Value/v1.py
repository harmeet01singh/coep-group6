from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import putInCsv, database_fn


total_dist = 0
place_name = []
a, b, c = 0, 0, 0
x, y = 0, 0
i = 0


def changeValues():
	global total_dist, place_name, a, b, c, x, y, i
	total_dist = random.randint(200, 300)
	place_name = ["school", "house", "park", "hospital", "metro"]
	a, b, c = random.sample(place_name, k=3)
	x = random.randint(50, 150)
	y = total_dist - x
	i += 1


def generate_img():
	margin = 100
	width = (margin + total_dist) * 2
	height = 300
	img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
	draw = ImageDraw.Draw(img)

	start_coordinate = (margin, 150)
	end_coordinate = (margin + total_dist * 2, 150)
	# Line
	draw.line([start_coordinate, end_coordinate], fill="black", width=2)
	draw.line([margin, 200, margin + total_dist * 2, 200], fill="black", width=1)
	# 5 Points
	draw.ellipse([margin - 5, 145, margin + 5, 155], fill="green", outline="black", width=2)
	draw.ellipse([margin - 2, 198, margin + 2, 202], fill="black", outline="black", width=2)
	draw.ellipse([margin + total_dist * 2- 5, 145, margin + total_dist * 2 + 5, 155], fill="green", outline="black", width=2)
	draw.ellipse([margin + total_dist * 2- 2, 198, margin + total_dist * 2 + 2, 202], fill="black", outline="black", width=2)
	draw.ellipse([margin + x * 2 - 5, 145, margin + x * 2 + 5, 155], fill="green", outline="black", width=2)
	# ? and numbers
	draw.text([margin + x - 20, 155], f"{x}", font=ImageFont.truetype("arial.ttf", size=25), fill="black")
	draw.text([margin + total_dist * 2 - y - 20, 155], "?", font=ImageFont.truetype("arial.ttf", size=25), fill="black")
	draw.text([margin + total_dist - 25, 205], f"{total_dist}", font=ImageFont.truetype("arial.ttf", size=25), fill="black")
	# Places name
	draw.text([margin - 30, 110], f"{a}", font=ImageFont.truetype("arial.ttf", size=25), fill="black")
	draw.text([margin + total_dist * 2 - 30, 110], f"{c}", font=ImageFont.truetype("arial.ttf", size=25), fill="black")
	draw.text([margin + x * 2 - 30, 110], f"{b}", font=ImageFont.truetype("arial.ttf", size=25), fill="black")

	#Display Image
	# img.show()
	image_name = f"Negative Distance Value ({i}).png"
	img.save(image_name, format="PNG")


def getQuestion():
	return f"If total distance between {a} and {c} is {latex(total_dist)}, then what is the distance between {b} and {c} ?"


def getCorrOption():
	return f"{latex(y)}"


def getWrongOptions():
	while True:
		a, b = random.sample(range(y - 10, y + 10), k=2)
		if a != y and b != y:
			break
	options = [f"{latex(total_dist + x)}", f"{latex(a)}", f"{latex(b)}"]
	random.shuffle(options)
	return options


def getSolution():
	return f"\n--------------------------------------SOLUTION-------------------------------------------\n=> distance between {b} and {c} = distance between {a} and {c} - distance between {a} and {b} \n=> distance between {b} and {c} = {latex(str(total_dist) + ' - ' + str(x))}\n=> distance between {b} and {c} = {latex(y)}\nHence the correct answer is {latex(y)}."


def main_function():
	changeValues()
	generate_img()
	Question = getQuestion()
	Corr_op = getCorrOption()
	wrong_op1, wrong_op2, wrong_op3 = getWrongOptions()
	Solution = getSolution()

	database_dict = database_fn(
		Answer_Type='1',
		Topic_Number='030203',
		Variation='1',
		Question=Question,
		Correct_Answer_1=Corr_op,
		Wrong_Answer_1=wrong_op1,
		Wrong_Answer_2=wrong_op2,
		Wrong_Answer_3=wrong_op3,
		Solution_text=Solution)
	return database_dict


putInCsv(
	Topic_Number='030203',
	Number_Of_Iterations=5,
	Main_Function=main_function,
	Filename="v1.py"
)
