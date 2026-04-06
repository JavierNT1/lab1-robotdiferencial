from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Modo velocidad
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Contador de tiempo
tiempo = 0

while robot.step(timestep) != -1:
    tiempo += 1

    # 1. Línea recta
    if tiempo < 400:
        vl = 3.0
        vr = 3.0

    # 2. Curva
    elif tiempo < 800:
        vl = 2.5
        vr = 4.0

    # 3. Círculo
    else:
        vl = 2.0
        vr = 4.0

    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)