from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Obtener motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Configurar motores en modo velocidad
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Contador de tiempo
tiempo = 0

while robot.step(timestep) != -1:
    tiempo += 1

    # Caso 1: Movimiento recto
    if tiempo < 400:
        vl = 3.0
        vr = 3.0

    # Caso 2: Trayectoria curva
    elif tiempo < 800:
        vl = 2.0
        vr = 4.0

    # Caso 3: Rotación en el lugar
    else:
        vl = 3.0
        vr = -3.0

    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)