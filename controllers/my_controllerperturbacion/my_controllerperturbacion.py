from controller import Robot
import random

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

tiempo = 0
pert_l = 0
pert_r = 0

while robot.step(timestep) != -1:
    tiempo += 1

    if tiempo % 10 == 0:
        pert_l = random.uniform(-0.5, 0.5)
        pert_r = random.uniform(-0.5, 0.5)

    if tiempo < 400:
        vl = 3.0 + pert_l
        vr = 3.0 + pert_r
    elif tiempo < 800:
        vl = 2.0 + pert_l
        vr = 4.0 + pert_r
    else:
        vl = 3.0 + pert_l
        vr = -3.0 + pert_r

    if tiempo % 50 == 0:
        print(f"vl: {vl:.2f}, vr: {vr:.2f}")

    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)