import turtle
import math

screenWidth = 900
screenHeight = 450
windowTitle = "Code and Seek!"

turtle.setup(screenWidth, screenHeight)
screen = turtle.Screen()
screen.title(windowTitle)

screen.tracer(0)

t = turtle.Turtle()
t.fillcolor('red')

def splashScreen():
    t.up()
    t.goto(0,100)
    t.write("CODE AND SEEK!", align='center', font=('Arial','40'))
    screen.update()
    screen.textinput(" ","Press OK to begin")

def setLocation():
    # Get hider pos
    xPos = screen.numinput("HIDER", "Enter an x-Position:")
    yPos = screen.numinput("HIDER", "Enter a y-Position:")
    return xPos,yPos

def guessAndCompare(hiderPos):
    # Grab seeker guess
    xGuess = screen.numinput("SEEKER", "Enter an x-Position:")
    yGuess = screen.numinput("SEEKER", "Enter a y-Position:")

    # Compare to hider pos and return all info
    score = 0
    distanceToHider = math.sqrt(math.fabs(hiderPos[0]-xGuess)**2 + math.fabs(hiderPos[1]-yGuess)**2)
    if 200-distanceToHider < 0:
        score = 0
    else:
        score = (200-distanceToHider)**2/4000
    return distanceToHider, score, xGuess, yGuess

def drawGuess(distanceToHider, score, xGuess, yGuess):
    # Draw the guessed point
    t.goto(xGuess, yGuess+10)
    t.down()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.up()
    t.goto(xGuess + 15,yGuess+20)
    t.write(f"{round(distanceToHider,2)} pixels away")
    t.goto(xGuess + 15,yGuess+10)
    t.write(f"Score: {round(score,2)}")
    screen.update()

splashScreen()
screen.clear()
hiderLocation = setLocation()
guessInfo = guessAndCompare(hiderLocation)
drawGuess(guessInfo[0],guessInfo[1],guessInfo[2],guessInfo[3])


turtle.done()