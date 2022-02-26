import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.ion()

fig = plt.figure()

# checks if a given number is prime or not
def isPrime(num):
    if(num == 1):
        return False

    for x in range(2, num):
        if(num % x == 0):
            return False

    return True

#change the x/y coordinates based on the state
def march(state, x, y):
    if(state == 0):
        x += 1
    if(state == 1):
        y += 1
    if(state == 2):
        x -= 1
    if(state == 3):
        y -= 1

    return x,y


l_x = 1
l_y = 0

x = 0
y = 0

state = -1
factor = -1
steps = 1
currentSteps = 0

for i in range(1, 26):
    l_x = x
    l_y = y

    currentSteps += 1
    if(currentSteps >= steps):
        factor += 1
        currentSteps = 0

        x, y = march(state, x, y)

        state += 1
        if(state > 3):
            state = 0

        if(factor == 2):
            factor = 0
            steps += 1

    if(currentSteps != 0):
        x, y = march(state, x, y)


    point1 = [x, y]
    point2 = [l_x, l_y]

    xValues = [point1[0], point2[0]]
    yValues = [point1[1], point2[1]]

    plt.plot(xValues, yValues, 'r-')


    if(isPrime(i)):
        plt.text(x, y, str(i), color='white')
        plt.plot([x], [y], 'ro')
    # else:
        #plt.plot([x], [y], 'b.')

    fig.canvas.draw()
    fig.canvas.flush_events()

plt.pause(180)
