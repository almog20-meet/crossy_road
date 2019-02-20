import turtle
from turtle import Turtle
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

turtle.setup(screen_width *2, screen_height*2)
minimum_speed = -10
maximum_speed = 10
minimum_widht = 3
maximum_widht = 8
running = True 

class Car(Turtle):
	def __init__(self,speed,color,pos,width):
		Turtle.__init__(self)
		self.penup()
		self.speed(speed)
		self.color(color)
		self.shape("square")
		self.goto(pos)
		self.shapesize(1,width,None)
	def move(self):
		if self.car_pos[0]<screen_width+(self.car_width*10) and self.car_pos[0]>-(screen_width+(self.car_width*10)):
			self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
			self.car_pos = self.pos()
		else:
			print("out of screen")
			if self.speed > 0:
				self.new_car((-(screen_width+(self.car_width*10)),self.car_pos[1]))
				while self.car_pos[0]<-screen_width:
					self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
					self.car_pos = self.pos()
			else:
				self.new_car((screen_width+(self.car_width*10),self.car_pos[1]))
				while self.car_pos[0]>screen_width:
					self.goto(self.car_pos[0]+self.speed, self.car_pos[1])
					self.car_pos = self.pos()
	def new_car(self,pos):
		self.car_pos = pos


def show_coordination(x, y):
	print(str(x)+","+str(y))

turtle.onscreenclick(show_coordination)
def pick_color():
    colors = ["purple","lime","lavender","cyan","salmon","gold","lawngreen"]
    random.shuffle(colors)
    return colors[0]
colors = ["purple","lime","lavender","cyan","salmon","gold","lawngreen"]

CARS = []
y_pos = [281, 132, -19, -170, -300]
random.shuffle(y_pos)

for i in range(20):
	rSPEED =  random.randint(minimum_speed, maximum_speed)
	while rSPEED == 0:
		rSPEED = random.randint(mminimum_speed, maximum_speed)
	rCOLOR =  (random.random(), random.random(), random.random()) 
	rPOSITION_X =
	rPOSITION_Y = y_pos[0]
	rPOSITION = (rPOSITION_X, rPOSITION_Y)
	rWIDTH =  random.randint(minimum_widht, maximum_widht)
	
	car = Car(rSPEED, rCOLOR, rPOSITION, rWIDTH)
	CARS.append(car)

while running == True:
	for car in CARS:
		car.move()


turtle.mainloop()
