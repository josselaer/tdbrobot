import tdb_bot.py


rob = tdb_bot.tdb_bot()

ball1 = rob.generate_ball()
ball2 = rob.generate_ball()
ball3 = rob.generate_ball()

print(ball1)
rob.move_robot(ball1)