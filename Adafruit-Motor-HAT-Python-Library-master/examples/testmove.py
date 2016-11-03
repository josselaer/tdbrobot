import tdb_bot


rob = tdb_bot.tdb_bot(0,0)

ball1 = rob.generate_ball()
ball2 = rob.generate_ball()
ball3 = rob.generate_ball()

print(ball1)
rob.move_robot(ball1)