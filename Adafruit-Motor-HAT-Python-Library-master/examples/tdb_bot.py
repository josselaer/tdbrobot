import Robot
import time
from random import randint

LEFT_TRIM   = 0
RIGHT_TRIM  = 0


# Create an instance of the self.robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.

#self.robot = self.robot.self.robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

class tdb_bot:
	"""docstring for tdb_bot"""
	curr_x = 0
	curr_y = 0


	def __init__(self, x, y):
		self.LEFT_TRIM   = 0
		self.RIGHT_TRIM  = 0
		self.curr_x = x
		self.curr_y = y
		self.robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
		self.quarterTurnTime = 0.21
		self.halfTurnTime = 0.39
		self.oneFootTime = 0.92
		self.robotSpeed = 200
		
	def go_to_origin(self):
		origin = [0,0]
		print("going home")
		self.move_robot(origin)

	def generate_ball(self):
		x = randint(0,9)
		y = randint(0,9)
		ball = []
		ball.append(x)
		ball.append(y)
		return ball

	def move_robot(self, ball):
		diff_x = ball[0] - self.curr_x
		diff_y = ball[1] - self.curr_y
		print(diff_x)
		print(diff_y)
		if(diff_x > 0):
			print("turnng right")
			self.robot.right(self.robotSpeed,self.quarterTurnTime)
		elif(diff_x < 0):
			print("left")
			self.robot.left(self.robotSpeed,self.quarterTurnTime)
		self.robot.forward(self.robotSpeed,(self.oneFootTime * abs(diff_x)))
		print("forward")
		if(diff_x > 0):
			self.robot.left(self.robotSpeed,self.quarterTurnTime)
			print("straitening to left")
		elif(diff_x < 0):
			self.robot.right(self.robotSpeed,self.quarterTurnTime)
			print("straitending to right")

		if(diff_y < 0):
			self.robot.right(self.robotSpeed,self.halfTurnTime)
			print("turn around")

		self.robot.forward(self.robotSpeed,(self.oneFootTime*abs(diff_y)))
		print("froward again")

		if(diff_y < 0):
			self.robot.right(self.robotSpeed,self.halfTurnTime)
			print("straiten if backwards")

		self.curr_x = ball[0]
		self.curr_y = ball[1]



