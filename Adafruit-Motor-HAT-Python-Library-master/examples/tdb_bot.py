import Robot
import time
from random import randint

LEFT_TRIM   = 0
RIGHT_TRIM  = 0


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.

#robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

class tdb_bot:
	"""docstring for tdb_bot"""
	curr_x = 0
	curr_y = 0
	robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


	def __init__(self, x, y):
		self.LEFT_TRIM   = 0
		self.RIGHT_TRIM  = 0
		self.curr_x = x
		self.curr_y = y


		
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
			robot.right(200,0.3)
		elif(diff_x < 0:
			robot.left(200,0.3)
		robot.forward(200,(0.917 * abs(diff_x)))
		if(diff_x > 0):
			robot.left(200,0.3)
		elif(diff_x < 0:
			robot.right(200,0.3)

		if(diff_y < 0):
			robot.right(200,0.44)

		robot.forward(200,(0.917*abs(diff_y)))

		if(diff_y < 0):
			robot.right(200,0.44)

		self.curr_x = ball[0]
		self.curr_y = ball[1]



